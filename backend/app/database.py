"""
数据库连接模块

负责与 MongoDB 数据库建立连接，提供数据库和集合的访问。
使用 motor 异步驱动实现非阻塞的数据库操作。
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB 连接配置
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_USER = os.getenv("MONGO_USER", "fufu")
MONGO_PASS = os.getenv("MONGO_PASS", "fufufamily")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "family_menu")

# 构建 MongoDB 连接 URL
MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"

# 创建异步 MongoDB 客户端
client = AsyncIOMotorClient(MONGO_URL)

# 获取数据库实例
database = client[MONGO_DB_NAME]

# 集合（表）定义
recipes_collection = database["recipes"]       # 菜谱集合
orders_collection = database["orders"]         # 订单集合
categories_collection = database["categories"] # 分类集合
users_collection = database["users"]           # 用户集合


async def init_db():
    """
    初始化数据库

    创建必要的索引以提高查询性能：
    - 菜谱集合：按分类和名称建立索引
    - 订单集合：按状态和创建时间建立索引
    """
    # 菜谱索引
    await recipes_collection.create_index("category")
    await recipes_collection.create_index("name")

    # 订单索引
    await orders_collection.create_index("status")
    await orders_collection.create_index("created_at")

    # 用户索引
    await users_collection.create_index("openid", unique=True)

    print("数据库索引创建完成")


async def close_db():
    """关闭数据库连接"""
    client.close()
    print("数据库连接已关闭")
