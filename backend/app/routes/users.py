"""
用户路由模块

提供微信用户相关的 API：
- 微信登录（获取/创建用户）
- 获取用户信息
- 更新用户信息
"""

from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException

from ..database import users_collection
from ..models import UserCreate, UserResponse

router = APIRouter(prefix="/api/users", tags=["用户"])


def user_doc_to_response(doc: dict) -> dict:
    """将数据库文档转换为响应格式"""
    doc["_id"] = str(doc["_id"])
    return doc


@router.post("/login", summary="微信登录")
async def wx_login(user: UserCreate):
    """
    微信小程序登录

    根据 openid 查找或创建用户：
    - 已存在：更新昵称和头像
    - 不存在：创建新用户
    """
    now = datetime.now()

    # 查找现有用户
    existing = await users_collection.find_one({"openid": user.openid})

    if existing:
        # 更新用户信息
        await users_collection.update_one(
            {"openid": user.openid},
            {"$set": {
                "nickname": user.nickname,
                "avatar": user.avatar,
                "updated_at": now
            }}
        )
        existing["_id"] = str(existing["_id"])
        return existing
    else:
        # 创建新用户
        doc = {
            "openid": user.openid,
            "nickname": user.nickname,
            "avatar": user.avatar,
            "created_at": now
        }
        result = await users_collection.insert_one(doc)
        doc["_id"] = str(result.inserted_id)
        return doc


@router.get("/{openid}", summary="获取用户信息")
async def get_user(openid: str):
    """根据 openid 获取用户信息"""
    doc = await users_collection.find_one({"openid": openid})
    if not doc:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user_doc_to_response(doc)


@router.put("/{openid}", summary="更新用户信息")
async def update_user(openid: str, user: UserCreate):
    """更新用户昵称和头像"""
    result = await users_collection.update_one(
        {"openid": openid},
        {"$set": {
            "nickname": user.nickname,
            "avatar": user.avatar,
            "updated_at": datetime.now()
        }}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"message": "更新成功"}
