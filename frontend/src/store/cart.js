/**
 * 购物车状态管理
 *
 * 使用响应式状态管理购物车数据
 * 包含添加、删除、清空等功能
 */

import { reactive } from 'vue'

// 购物车状态
const state = reactive({
  items: []  // 购物车项列表
})

/**
 * 添加菜品到购物车
 * @param {Object} recipe - 菜谱对象
 */
export const addToCart = (recipe) => {
  // 检查是否已在购物车中
  const existing = state.items.find(item => item.id === recipe._id)
  if (existing) {
    existing.quantity += 1
  } else {
    state.items.push({
      id: recipe._id,
      name: recipe.name,
      image: recipe.image,
      price_hearts: recipe.price_hearts,
      quantity: 1
    })
  }
}

/**
 * 从购物车移除菜品
 * @param {string} id - 菜品ID
 */
export const removeFromCart = (id) => {
  const index = state.items.findIndex(item => item.id === id)
  if (index > -1) {
    state.items.splice(index, 1)
  }
}

/**
 * 更新菜品数量
 * @param {string} id - 菜品ID
 * @param {number} quantity - 新数量
 */
export const updateQuantity = (id, quantity) => {
  const item = state.items.find(item => item.id === id)
  if (item) {
    if (quantity <= 0) {
      removeFromCart(id)
    } else {
      item.quantity = quantity
    }
  }
}

/**
 * 清空购物车
 */
export const clearCart = () => {
  state.items = []
}

/**
 * 计算总爱心数
 * @returns {number} 总爱心数
 */
export const getTotalHearts = () => {
  return state.items.reduce((sum, item) => sum + item.price_hearts * item.quantity, 0)
}

/**
 * 获取购物车项数量
 * @returns {number} 购物车项数量
 */
export const getCartCount = () => {
  return state.items.reduce((sum, item) => sum + item.quantity, 0)
}

/**
 * 获取购物车状态
 */
export const useCart = () => {
  return {
    state,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    getTotalHearts,
    getCartCount
  }
}

export default {
  state,
  addToCart,
  removeFromCart,
  updateQuantity,
  clearCart,
  getTotalHearts,
  getCartCount,
  useCart
}
