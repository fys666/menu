/**
 * API 请求模块
 *
 * 封装 axios 实例，提供统一的请求配置和错误处理
 */

import axios from 'axios'

// 创建 axios 实例
const api = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 响应拦截器
api.interceptors.response.use(
  response => response.data,
  error => {
    console.error('API 请求错误:', error)
    return Promise.reject(error)
  }
)

// ==================== 菜谱 API ====================

/**
 * 获取菜谱列表
 * @param {Object} params - 查询参数
 * @param {string} params.category - 分类筛选
 * @param {string} params.search - 搜索关键词
 * @param {number} params.page - 页码
 * @param {number} params.page_size - 每页数量
 */
export const getRecipes = (params = {}) => {
  return api.get('/api/recipes', { params })
}

/**
 * 获取菜谱详情
 * @param {string} id - 菜谱ID
 */
export const getRecipe = (id) => {
  return api.get(`/api/recipes/${id}`)
}

/**
 * 获取所有分类
 */
export const getCategories = () => {
  return api.get('/api/recipes/categories/all')
}

// ==================== 订单 API ====================

/**
 * 创建订单
 * @param {Object} data - 订单数据
 * @param {string} data.customer_name - 点菜人
 * @param {Array} data.items - 订单项列表
 * @param {string} data.remark - 备注
 */
export const createOrder = (data) => {
  return api.post('/api/orders', data)
}

/**
 * 获取订单列表
 * @param {Object} params - 查询参数
 * @param {string} params.status - 状态筛选
 * @param {number} params.page - 页码
 */
export const getOrders = (params = {}) => {
  return api.get('/api/orders', { params })
}

/**
 * 获取订单详情
 * @param {string} id - 订单ID
 */
export const getOrder = (id) => {
  return api.get(`/api/orders/${id}`)
}

/**
 * 更新订单状态
 * @param {string} id - 订单ID
 * @param {Object} data - 状态数据
 * @param {string} data.status - 新状态
 * @param {string} data.note - 备注
 */
export const updateOrderStatus = (id, data) => {
  return api.patch(`/api/orders/${id}/status`, data)
}

/**
 * 删除订单
 * @param {string} id - 订单ID
 */
export const deleteOrder = (id) => {
  return api.delete(`/api/orders/${id}`)
}

export default api
