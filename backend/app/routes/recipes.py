"""
菜谱路由模块

提供菜谱的 CRUD 操作 API：
- 获取菜谱列表（支持分类筛选和搜索）
- 获取菜谱详情
- 创建新菜谱
- 更新菜谱
- 删除菜谱
"""

from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Query

from ..database import recipes_collection, categories_collection
from ..models import RecipeCreate, RecipeResponse

router = APIRouter(prefix="/api/recipes", tags=["菜谱"])


def recipe_doc_to_response(doc: dict) -> dict:
    """将数据库文档转换为响应格式"""
    doc["_id"] = str(doc["_id"])
    return doc


@router.get("", summary="获取菜谱列表")
async def get_recipes(
    category: str = Query(None, description="按分类筛选"),
    search: str = Query(None, description="搜索关键词"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=50, description="每页数量")
):
    """
    获取菜谱列表

    支持按分类筛选和关键词搜索，返回分页结果。
    """
    # 构建查询条件
    query = {}
    if category:
        query["category"] = category
    if search:
        query["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
            {"tags": {"$regex": search, "$options": "i"}}
        ]

    # 计算跳过的记录数
    skip = (page - 1) * page_size

    # 查询数据库
    cursor = recipes_collection.find(query).skip(skip).limit(page_size)
    recipes = []
    async for doc in cursor:
        recipes.append(recipe_doc_to_response(doc))

    # 获取总数
    total = await recipes_collection.count_documents(query)

    return {
        "items": recipes,
        "total": total,
        "page": page,
        "page_size": page_size
    }


@router.get("/{recipe_id}", summary="获取菜谱详情")
async def get_recipe(recipe_id: str):
    """根据ID获取菜谱详情"""
    try:
        doc = await recipes_collection.find_one({"_id": ObjectId(recipe_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="无效的菜谱ID")

    if not doc:
        raise HTTPException(status_code=404, detail="菜谱不存在")

    return recipe_doc_to_response(doc)


@router.post("", summary="创建菜谱", status_code=201)
async def create_recipe(recipe: RecipeCreate):
    """创建新的菜谱"""
    doc = recipe.model_dump()
    doc["created_at"] = datetime.now()

    result = await recipes_collection.insert_one(doc)
    doc["_id"] = str(result.inserted_id)

    return doc


@router.put("/{recipe_id}", summary="更新菜谱")
async def update_recipe(recipe_id: str, recipe: RecipeCreate):
    """更新菜谱信息"""
    try:
        object_id = ObjectId(recipe_id)
    except Exception:
        raise HTTPException(status_code=400, detail="无效的菜谱ID")

    doc = recipe.model_dump()
    result = await recipes_collection.update_one(
        {"_id": object_id},
        {"$set": doc}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="菜谱不存在")

    return {"message": "更新成功"}


@router.delete("/{recipe_id}", summary="删除菜谱")
async def delete_recipe(recipe_id: str):
    """删除菜谱"""
    try:
        object_id = ObjectId(recipe_id)
    except Exception:
        raise HTTPException(status_code=400, detail="无效的菜谱ID")

    result = await recipes_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="菜谱不存在")

    return {"message": "删除成功"}


# ==================== 分类路由 ====================

@router.get("/categories/all", summary="获取所有分类", tags=["分类"])
async def get_categories():
    """获取所有菜谱分类"""
    cursor = categories_collection.find().sort("order", 1)
    categories = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        categories.append(doc)
    return categories
