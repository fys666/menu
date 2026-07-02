"""
家庭菜单小程序 - 后端主程序

FastAPI 应用入口，负责：
- 初始化 FastAPI 应用
- 注册路由
- 启动/关闭事件处理
- 配置 CORS 跨域
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database import init_db, close_db
from app.routes.recipes import router as recipes_router
from app.routes.orders import router as orders_router
from app.routes.users import router as users_router
from app.seed_data import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理

    启动时：初始化数据库连接、创建索引、导入种子数据
    关闭时：关闭数据库连接
    """
    # 启动时执行
    print("🚀 家庭菜单小程序后端启动中...")
    await init_db()
    await seed_database()
    print("✅ 后端启动完成")
    yield
    # 关闭时执行
    await close_db()
    print("👋 后端已关闭")


# 创建 FastAPI 应用
app = FastAPI(
    title="家庭菜单小程序 API",
    description="家人点菜系统 - 结构化菜谱、爱心定价、订单管理",
    version="1.0.0",
    lifespan=lifespan
)

# 配置 CORS 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（生产环境应限制）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(recipes_router)
app.include_router(orders_router)
app.include_router(users_router)


@app.get("/", summary="健康检查")
async def root():
    """API 健康检查端点"""
    return {
        "message": "家庭菜单小程序 API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/api/health", summary="健康检查")
async def health_check():
    """详细的健康检查端点"""
    return {
        "status": "healthy",
        "service": "family-menu-api",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
