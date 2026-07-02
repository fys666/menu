# 🍽️ 家庭菜单小程序

家人点菜系统 - 结构化菜谱、爱心定价、订单管理、制作状态流转

## 📸 功能特性

- **62 道精选菜谱**：涵盖荤菜、素菜、汤羹、主食、凉菜、甜点、饮品 7 大分类
- **结构化菜谱**：每道菜包含食材清单、制作步骤、难度等级、烹饪时间
- **爱心定价**：用 ❤️ 表示价格，无需真实支付，仅供展示
- **订单管理**：完整的下单、确认、制作、出锅、完成流程
- **状态流转**：可视化追踪订单状态变化
- **双端支持**：微信小程序 + H5 网页版
- **微信登录**：自动获取微信用户信息，无需手动输入

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| **前端（小程序）** | uni-app + Vue3 + 微信小程序 |
| **前端（H5）** | Vue3 + Vant + Vite |
| **后端** | FastAPI + Python 3.13 |
| **数据库** | MongoDB 8.x (Docker) |

## 📁 项目结构

```
menu/
├── docker-compose.yml          # MongoDB Docker 配置
├── .gitignore                  # Git 忽略配置
├── backend/                    # FastAPI 后端
│   ├── main.py                # 应用入口
│   ├── requirements.txt       # Python 依赖
│   └── app/
│       ├── database.py        # 数据库连接
│       ├── models.py          # Pydantic 数据模型
│       ├── routes/
│       │   ├── recipes.py     # 菜谱 API
│       │   ├── orders.py      # 订单 API
│       │   └── users.py       # 用户 API（微信登录）
│       └── seed_data.py       # 种子数据（62 道菜）
├── frontend/                   # Vue3 H5 版本
│   └── src/
│       ├── views/             # 页面组件
│       ├── components/        # 公共组件
│       ├── api/               # API 请求
│       └── store/             # 状态管理
└── miniprogram/                # uni-app 微信小程序版本
    ├── src/
    │   ├── pages.json         # 页面路由配置
    │   ├── manifest.json      # 小程序配置
    │   ├── pages/             # 页面目录
    │   ├── api/               # API 请求
    │   └── store/             # 状态管理
    └── dist/build/mp-weixin/  # 编译输出
```

## 🚀 快速开始

### 环境要求

- Docker & Docker Compose
- Python 3.13 (mamba/conda)
- Node.js v24

### 1. 克隆项目

```bash
git clone https://github.com/fys666/menu.git
cd menu
```

### 2. 启动 MongoDB

```bash
sudo docker compose up -d
```

**数据库信息：**
- 地址：`mongodb://fufu:fufufamily@localhost:27017`
- 数据库：`family_menu`

### 3. 启动后端

```bash
cd backend

# 激活环境（首次使用需创建）
mamba create -n menu-backend python=3.13 -y
mamba activate menu-backend
pip install -r requirements.txt

# 启动服务
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

启动后访问：
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/api/health

### 4. 启动前端（二选一）

#### 方式一：H5 网页版

```bash
cd frontend
npm install
npm run dev
```

访问 http://localhost:3000

#### 方式二：微信小程序版

```bash
cd miniprogram
npm install
npm run dev:mp-weixin
```

使用微信开发者工具导入 `miniprogram/dist/dev/mp-weixin` 目录

## 📱 页面功能

| 页面 | 路径 | 功能 |
|------|------|------|
| 首页 | `/` | 分类导航、推荐菜品、搜索 |
| 分类 | `/category` | 按分类浏览菜品 |
| 菜品详情 | `/recipe/:id` | 食材、步骤、加入已点 |
| 已点菜品 | `/cart` | 调整数量、提交订单 |
| 提交订单 | `/order/submit` | 自动填充微信用户信息、确认下单 |
| 订单记录 | `/orders` | 查看所有订单、状态筛选 |
| 订单详情 | `/order/:id` | 订单信息、状态时间线 |
| 订单管理 | `/admin` | 确认订单、更新制作状态 |

## 🔄 订单状态流转

```
待确认 (pending) → 已确认 (confirmed) → 制作中 (cooking) → 已出锅 (ready) → 已完成 (completed)
```

## 📡 API 接口

### 菜谱接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/recipes` | 获取菜谱列表（支持分类筛选、搜索） |
| GET | `/api/recipes/:id` | 获取菜谱详情 |
| GET | `/api/recipes/categories/all` | 获取所有分类 |

### 订单接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/orders` | 创建订单 |
| GET | `/api/orders` | 获取订单列表 |
| GET | `/api/orders/:id` | 获取订单详情 |
| PATCH | `/api/orders/:id/status` | 更新订单状态 |
| DELETE | `/api/orders/:id` | 删除订单 |

### 用户接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/users/login` | 微信登录（获取/创建用户） |
| GET | `/api/users/:openid` | 获取用户信息 |
| PUT | `/api/users/:openid` | 更新用户信息 |

## 🍳 菜谱分类

| 分类 | 数量 | 示例菜品 |
|------|------|----------|
| 🍖 荤菜 | 17 道 | 红烧肉、糖醋排骨、宫保鸡丁 |
| 🥬 素菜 | 11 道 | 蒜蓉西兰花、地三鲜、酸辣土豆丝 |
| 🍚 主食 | 8 道 | 蛋炒饭、饺子、小笼包 |
| 🍲 汤羹 | 7 道 | 番茄蛋花汤、冬瓜排骨汤 |
| 🥤 饮品 | 7 道 | 柠檬蜂蜜水、酸梅汤 |
| 🥗 凉菜 | 6 道 | 拍黄瓜、口水鸡 |
| 🍰 甜点 | 6 道 | 芒果班戟、双皮奶 |

## ⚙️ 配置说明

### 小程序 AppID

在 `miniprogram/src/manifest.json` 中配置你的微信小程序 AppID：

```json
{
  "mp-weixin": {
    "appid": "你的AppID"
  }
}
```

### 服务器地址

小程序真机调试时，需要修改 `miniprogram/src/api/index.js` 中的 `BASE_URL` 为内网 IP：

```javascript
const BASE_URL = 'http://192.168.x.x:8000'
```

## 🚢 部署指南

### 方式一：本地开发部署

```bash
# 1. 启动 MongoDB
sudo docker compose up -d

# 2. 启动后端
cd backend
mamba activate menu-backend
uvicorn main:app --host 0.0.0.0 --port 8000

# 3. 启动前端
cd ../miniprogram
npm run dev:mp-weixin
```

### 方式二：服务器部署

#### 1. 安装 Docker

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# 启动 Docker
sudo systemctl start docker
sudo systemctl enable docker
```

#### 2. 部署 MongoDB

```bash
# 上传项目到服务器
git clone https://github.com/fys666/menu.git
cd menu

# 启动 MongoDB
sudo docker compose up -d
```

#### 3. 部署后端

```bash
cd backend

# 安装 Python 3.13
sudo apt update
sudo apt install -y python3.13 python3.13-venv

# 创建虚拟环境
python3.13 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 使用 systemd 管理服务
sudo tee /etc/systemd/system/menu-backend.service << 'EOF'
[Unit]
Description=Family Menu Backend
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/menu/backend
ExecStart=/path/to/menu/backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
sudo systemctl daemon-reload
sudo systemctl enable menu-backend
sudo systemctl start menu-backend
```

#### 4. 配置 Nginx（可选）

```bash
sudo apt install -y nginx

sudo tee /etc/nginx/sites-available/menu << 'EOF'
server {
    listen 80;
    server_name your-domain.com;

    # 后端 API
    location /api {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # H5 前端
    location / {
        root /path/to/menu/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/menu /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 方式三：Docker 全部部署

创建 `docker-compose.full.yml`：

```yaml
services:
  mongo:
    image: mongo:latest
    container_name: family-menu-mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: fufu
      MONGO_INITDB_ROOT_PASSWORD: fufufamily
    volumes:
      - mongo-data:/data/db
    restart: unless-stopped

  backend:
    build: ./backend
    container_name: family-menu-backend
    ports:
      - "8000:8000"
    environment:
      MONGO_HOST: mongo
      MONGO_PORT: 27017
      MONGO_USER: fufu
      MONGO_PASS: fufufamily
    depends_on:
      - mongo
    restart: unless-stopped

volumes:
  mongo-data:
```

后端 `Dockerfile`：

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

启动：

```bash
sudo docker compose -f docker-compose.full.yml up -d
```

## 📝 注意事项

1. 首次启动后端会自动导入 62 道菜谱种子数据
2. 小程序真机调试需在微信开发者工具中勾选「不校验合法域名」
3. 生产环境需在微信小程序后台添加服务器域名
4. 菜品图片使用 Unsplash 外链，需确保网络可访问
5. 服务器部署时确保防火墙开放 8000 端口

## 📄 License

MIT
