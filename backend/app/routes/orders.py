"""
订单路由模块

提供订单的 CRUD 操作和状态流转 API：
- 创建订单（点菜）
- 获取订单列表
- 获取订单详情
- 更新订单状态（流转）
- 删除订单
"""

from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Query

from ..database import orders_collection
from ..models import OrderCreate, OrderResponse, StatusUpdate

router = APIRouter(prefix="/api/orders", tags=["订单"])

# 订单状态流转规则
STATUS_FLOW = {
    "pending": "confirmed",      # 待确认 → 已确认
    "confirmed": "cooking",      # 已确认 → 制作中
    "cooking": "ready",          # 制作中 → 已出锅
    "ready": "completed"         # 已出锅 → 已完成
}

# 状态中文名称映射
STATUS_NAMES = {
    "pending": "待确认",
    "confirmed": "已确认",
    "cooking": "制作中",
    "ready": "已出锅",
    "completed": "已完成"
}


def generate_order_no() -> str:
    """生成订单号：ORD + 日期时间 + 随机数"""
    now = datetime.now()
    return f"ORD{now.strftime('%Y%m%d%H%M%S')}"


def order_doc_to_response(doc: dict) -> dict:
    """将数据库文档转换为响应格式"""
    doc["_id"] = str(doc["_id"])
    # 转换 items 中的 recipe_id
    if "items" in doc:
        for item in doc["items"]:
            if "recipe_id" in item and isinstance(item["recipe_id"], ObjectId):
                item["recipe_id"] = str(item["recipe_id"])
    return doc


@router.get("", summary="获取订单列表")
async def get_orders(
    status: str = Query(None, description="按状态筛选"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=50, description="每页数量")
):
    """
    获取订单列表

    支持按状态筛选，返回分页结果。
    按创建时间倒序排列（最新的在前）。
    """
    query = {}
    if status:
        query["status"] = status

    skip = (page - 1) * page_size

    cursor = orders_collection.find(query).sort("created_at", -1).skip(skip).limit(page_size)
    orders = []
    async for doc in cursor:
        orders.append(order_doc_to_response(doc))

    total = await orders_collection.count_documents(query)

    return {
        "items": orders,
        "total": total,
        "page": page,
        "page_size": page_size
    }


@router.get("/{order_id}", summary="获取订单详情")
async def get_order(order_id: str):
    """根据ID获取订单详情"""
    try:
        doc = await orders_collection.find_one({"_id": ObjectId(order_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="无效的订单ID")

    if not doc:
        raise HTTPException(status_code=404, detail="订单不存在")

    return order_doc_to_response(doc)


@router.post("", summary="创建订单", status_code=201)
async def create_order(order: OrderCreate):
    """
    创建新订单（点菜）

    自动生成订单号，计算总爱心数，初始化状态为 pending。
    """
    # 计算总爱心数
    total_hearts = sum(item.get("price_hearts", 0) * item.get("quantity", 1) for item in order.items)

    # 构建订单文档
    doc = {
        "order_no": generate_order_no(),
        "customer_name": order.customer_name,
        "items": order.items,
        "total_hearts": total_hearts,
        "status": "pending",
        "status_history": [
            {
                "status": "pending",
                "time": datetime.now(),
                "note": "已下单"
            }
        ],
        "remark": order.remark,
        "created_at": datetime.now()
    }

    result = await orders_collection.insert_one(doc)
    doc["_id"] = str(result.inserted_id)

    return doc


@router.patch("/{order_id}/status", summary="更新订单状态")
async def update_order_status(order_id: str, update: StatusUpdate):
    """
    更新订单状态

    按照状态流转规则更新：
    pending → confirmed → cooking → ready → completed
    """
    try:
        object_id = ObjectId(order_id)
    except Exception:
        raise HTTPException(status_code=400, detail="无效的订单ID")

    # 获取当前订单
    order = await orders_collection.find_one({"_id": object_id})
    if not order:
        raise HTTPException(status_code=404, detail="订单不存在")

    current_status = order["status"]

    # 验证状态流转是否合法
    if update.status not in STATUS_FLOW.values():
        raise HTTPException(status_code=400, detail="无效的状态值")

    # 检查是否是下一个合法状态
    expected_next = STATUS_FLOW.get(current_status)
    if expected_next != update.status:
        raise HTTPException(
            status_code=400,
            detail=f"当前状态为{STATUS_NAMES.get(current_status, current_status)}，"
                   f"不能直接变更为{STATUS_NAMES.get(update.status, update.status)}"
        )

    # 添加状态历史记录
    status_record = {
        "status": update.status,
        "time": datetime.now(),
        "note": update.note or f"状态变更为{STATUS_NAMES.get(update.status, update.status)}"
    }

    result = await orders_collection.update_one(
        {"_id": object_id},
        {
            "$set": {"status": update.status},
            "$push": {"status_history": status_record}
        }
    )

    return {"message": "状态更新成功", "new_status": update.status}


@router.delete("/{order_id}", summary="删除订单")
async def delete_order(order_id: str):
    """删除订单"""
    try:
        object_id = ObjectId(order_id)
    except Exception:
        raise HTTPException(status_code=400, detail="无效的订单ID")

    result = await orders_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="订单不存在")

    return {"message": "删除成功"}
