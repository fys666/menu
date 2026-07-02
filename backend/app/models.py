"""
数据模型模块

定义菜谱、订单、分类等数据结构的 Pydantic 模型。
用于 API 请求/响应的数据验证和序列化。
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# ==================== 菜谱相关模型 ====================

class RecipeStep(BaseModel):
    """菜谱步骤"""
    order: int = Field(..., description="步骤序号")
    desc: str = Field(..., description="步骤描述")


class RecipeBase(BaseModel):
    """菜谱基础信息"""
    name: str = Field(..., description="菜名", max_length=50)
    category: str = Field(..., description="分类")
    subcategory: str = Field(..., description="子分类")
    image: str = Field("", description="图片URL")
    description: str = Field("", description="菜品简介")
    ingredients: list[str] = Field(default_factory=list, description="食材列表")
    steps: list[RecipeStep] = Field(default_factory=list, description="制作步骤")
    price_hearts: int = Field(1, description="爱心价格", ge=1, le=10)
    difficulty: str = Field("简单", description="难度：简单/中等/困难")
    cook_time: str = Field("30分钟", description="烹饪时间")
    tags: list[str] = Field(default_factory=list, description="标签")


class RecipeCreate(RecipeBase):
    """创建菜谱请求模型"""
    pass


class RecipeResponse(RecipeBase):
    """菜谱响应模型"""
    id: str = Field(..., alias="_id", description="菜谱ID")

    class Config:
        populate_by_name = True


# ==================== 分类相关模型 ====================

class CategoryBase(BaseModel):
    """分类基础信息"""
    name: str = Field(..., description="分类名称")
    icon: str = Field("🍽️", description="分类图标")
    order: int = Field(0, description="排序序号")


class CategoryCreate(CategoryBase):
    """创建分类请求模型"""
    pass


class CategoryResponse(CategoryBase):
    """分类响应模型"""
    id: str = Field(..., alias="_id", description="分类ID")

    class Config:
        populate_by_name = True


# ==================== 订单相关模型 ====================

class OrderItem(BaseModel):
    """订单项"""
    recipe_id: str = Field(..., description="菜谱ID")
    name: str = Field(..., description="菜名")
    quantity: int = Field(1, description="数量", ge=1)
    price_hearts: int = Field(..., description="单价（爱心）")


class OrderStatusHistory(BaseModel):
    """订单状态历史记录"""
    status: str = Field(..., description="状态")
    time: datetime = Field(default_factory=datetime.now, description="时间")
    note: str = Field("", description="备注")


class OrderBase(BaseModel):
    """订单基础信息"""
    customer_name: str = Field(..., description="点菜人", max_length=20)
    items: list[OrderItem] = Field(default_factory=list, description="订单项列表")
    remark: str = Field("", description="备注", max_length=200)


class OrderCreate(BaseModel):
    """创建订单请求模型"""
    customer_name: str = Field(..., description="点菜人", max_length=20)
    items: list[dict] = Field(..., description="订单项列表")
    remark: str = Field("", description="备注")


class OrderResponse(BaseModel):
    """订单响应模型"""
    id: str = Field(..., alias="_id", description="订单ID")
    order_no: str = Field(..., description="订单号")
    customer_name: str = Field(..., description="点菜人")
    items: list[OrderItem] = Field(default_factory=list, description="订单项列表")
    total_hearts: int = Field(0, description="总爱心数")
    status: str = Field("pending", description="当前状态")
    status_history: list[OrderStatusHistory] = Field(default_factory=list, description="状态历史")
    remark: str = Field("", description="备注")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

    class Config:
        populate_by_name = True


class StatusUpdate(BaseModel):
    """更新订单状态请求模型"""
    status: str = Field(..., description="新状态")
    note: str = Field("", description="备注")


# ==================== 用户相关模型 ====================

class UserCreate(BaseModel):
    """创建/更新用户请求模型"""
    openid: str = Field(..., description="微信 openid")
    nickname: str = Field("微信用户", description="用户昵称")
    avatar: str = Field("", description="用户头像 URL")


class UserResponse(BaseModel):
    """用户响应模型"""
    id: str = Field(..., alias="_id", description="用户ID")
    openid: str = Field(..., description="微信 openid")
    nickname: str = Field("微信用户", description="用户昵称")
    avatar: str = Field("", description="用户头像 URL")
    created_at: datetime = Field(default_factory=datetime.now, description="注册时间")

    class Config:
        populate_by_name = True
