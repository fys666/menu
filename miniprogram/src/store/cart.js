/**
 * 购物车状态管理
 *
 * 使用 uni storage 持久化购物车数据
 */

const STORAGE_KEY = 'family_menu_cart'

/**
 * 获取购物车数据
 */
export const getCart = () => {
  const data = uni.getStorageSync(STORAGE_KEY)
  return data ? JSON.parse(data) : []
}

/**
 * 保存购物车数据
 * @param {Array} items - 购物车项
 */
const saveCart = (items) => {
  uni.setStorageSync(STORAGE_KEY, JSON.stringify(items))
}

/**
 * 添加菜品到购物车
 * @param {Object} recipe - 菜谱对象
 */
export const addToCart = (recipe) => {
  const items = getCart()
  const existing = items.find(item => item.id === recipe._id)

  if (existing) {
    existing.quantity += 1
  } else {
    items.push({
      id: recipe._id,
      name: recipe.name,
      image: recipe.image,
      price_hearts: recipe.price_hearts,
      quantity: 1
    })
  }

  saveCart(items)
  return items
}

/**
 * 从购物车移除菜品
 * @param {string} id - 菜品ID
 */
export const removeFromCart = (id) => {
  let items = getCart()
  items = items.filter(item => item.id !== id)
  saveCart(items)
  return items
}

/**
 * 更新菜品数量
 * @param {string} id - 菜品ID
 * @param {number} quantity - 新数量
 */
export const updateQuantity = (id, quantity) => {
  const items = getCart()
  const index = items.findIndex(item => item.id === id)

  if (index > -1) {
    if (quantity <= 0) {
      items.splice(index, 1)
    } else {
      items[index].quantity = quantity
    }
  }

  saveCart(items)
  return items
}

/**
 * 清空购物车
 */
export const clearCart = () => {
  saveCart([])
  return []
}

/**
 * 计算总爱心数
 * @returns {number} 总爱心数
 */
export const getTotalHearts = () => {
  const items = getCart()
  return items.reduce((sum, item) => sum + item.price_hearts * item.quantity, 0)
}

/**
 * 获取购物车项数量
 * @returns {number} 购物车项数量
 */
export const getCartCount = () => {
  const items = getCart()
  return items.reduce((sum, item) => sum + item.quantity, 0)
}
