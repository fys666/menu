/**
 * API 请求模块
 *
 * 基于 uni.request 封装，适配微信小程序
 */

// 服务器地址配置
// 小程序真机调试时使用内网 IP
const BASE_URL = 'http://localhost:8000'

/**
 * 通用请求方法
 * @param {string} url - 请求路径
 * @param {string} method - 请求方法
 * @param {Object} data - 请求数据
 * @returns {Promise} 请求结果
 */
const request = (url, method = 'GET', data = {}) => {
  return new Promise((resolve, reject) => {
    uni.request({
      url: `${BASE_URL}${url}`,
      method,
      data,
      header: {
        'Content-Type': 'application/json'
      },
      success: (res) => {
        if (res.statusCode === 200) {
          resolve(res.data)
        } else {
          reject(res)
        }
      },
      fail: (err) => {
        console.error('请求失败:', err)
        reject(err)
      }
    })
  })
}

// ==================== 菜谱 API ====================

/**
 * 获取菜谱列表
 * @param {Object} params - 查询参数
 */
export const getRecipes = (params = {}) => {
  const query = Object.entries(params)
    .filter(([_, v]) => v !== undefined && v !== '')
    .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
    .join('&')
  return request(`/api/recipes${query ? '?' + query : ''}`)
}

/**
 * 获取菜谱详情
 * @param {string} id - 菜谱ID
 */
export const getRecipe = (id) => {
  return request(`/api/recipes/${id}`)
}

/**
 * 获取所有分类
 */
export const getCategories = () => {
  return request('/api/recipes/categories/all')
}

// ==================== 订单 API ====================

/**
 * 创建订单
 * @param {Object} data - 订单数据
 */
export const createOrder = (data) => {
  return request('/api/orders', 'POST', data)
}

/**
 * 获取订单列表
 * @param {Object} params - 查询参数
 */
export const getOrders = (params = {}) => {
  const query = Object.entries(params)
    .filter(([_, v]) => v !== undefined && v !== '')
    .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
    .join('&')
  return request(`/api/orders${query ? '?' + query : ''}`)
}

/**
 * 获取订单详情
 * @param {string} id - 订单ID
 */
export const getOrder = (id) => {
  return request(`/api/orders/${id}`)
}

/**
 * 更新订单状态
 * @param {string} id - 订单ID
 * @param {Object} data - 状态数据
 */
export const updateOrderStatus = (id, data) => {
  return request(`/api/orders/${id}/status`, 'PATCH', data)
}

/**
 * 删除订单
 * @param {string} id - 订单ID
 */
export const deleteOrder = (id) => {
  return request(`/api/orders/${id}`, 'DELETE')
}

// ==================== 用户 API ====================

/**
 * 微信登录（获取/创建用户）
 * @param {Object} data - 用户数据
 */
export const wxLogin = (data) => {
  return request('/api/users/login', 'POST', data)
}

/**
 * 获取用户信息
 * @param {string} openid - 用户 openid
 */
export const getUser = (openid) => {
  return request(`/api/users/${openid}`)
}
