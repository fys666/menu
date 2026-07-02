<!--
  购物车/已点菜品页视图

  展示已选择的菜品：
  - 菜品列表（可调整数量）
  - 总爱心数
  - 提交订单按钮
-->

<template>
  <div class="cart-page">
    <!-- 顶部标题 -->
    <van-nav-bar title="已点菜品" />

    <!-- 购物车列表 -->
    <div v-if="cartItems.length > 0" class="cart-list">
      <div v-for="item in cartItems" :key="item.id" class="cart-item">
        <!-- 菜品信息 -->
        <div class="item-info">
          <img :src="item.image || defaultImage" :alt="item.name" class="item-image" />
          <div class="item-detail">
            <h3>{{ item.name }}</h3>
            <div class="price">
              <span class="heart">❤️</span>
              <span>{{ item.price_hearts }}</span>
            </div>
          </div>
        </div>

        <!-- 数量控制 -->
        <div class="quantity-control">
          <van-stepper
            :model-value="item.quantity"
            @change="(val) => updateQuantity(item.id, val)"
            min="1"
            max="10"
          />
          <van-button
            type="danger"
            size="small"
            plain
            @click="removeItem(item.id)"
          >
            删除
          </van-button>
        </div>
      </div>
    </div>

    <!-- 空状态 -->
    <van-empty v-else description="还没有选择菜品哦">
      <van-button round type="primary" class="empty-button" @click="goToHome">
        去点菜
      </van-button>
    </van-empty>

    <!-- 底部结算栏 -->
    <div v-if="cartItems.length > 0" class="bottom-bar">
      <div class="total">
        <span>合计：</span>
        <span class="heart">❤️</span>
        <span class="value">{{ totalHearts }}</span>
      </div>
      <van-button type="primary" round @click="goToSubmit">
        提交订单
      </van-button>
    </div>
  </div>
</template>

<script setup>
/**
 * 购物车页面组件逻辑
 *
 * 功能：
 * 1. 展示已选菜品列表
 * 2. 调整菜品数量
 * 3. 删除菜品
 * 4. 计算总爱心数
 * 5. 跳转到提交订单页
 */
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCart } from '../store/cart'
import { showConfirmDialog } from 'vant'

const router = useRouter()
const { state, updateQuantity, removeFromCart, getTotalHearts } = useCart()

// 默认图片
const defaultImage = 'https://via.placeholder.com/80x80?text=菜品'

// 购物车项
const cartItems = computed(() => state.items)

// 总爱心数
const totalHearts = computed(() => getTotalHearts())

/**
 * 更新数量
 * @param {string} id - 菜品ID
 * @param {number} quantity - 新数量
 */
const updateQty = (id, quantity) => {
  updateQuantity(id, quantity)
}

/**
 * 删除菜品
 * @param {string} id - 菜品ID
 */
const removeItem = async (id) => {
  try {
    await showConfirmDialog({
      title: '提示',
      message: '确定要删除这道菜吗？'
    })
    removeFromCart(id)
  } catch {
    // 用户取消
  }
}

/**
 * 跳转到首页
 */
const goToHome = () => {
  router.push('/')
}

/**
 * 跳转到提交订单页
 */
const goToSubmit = () => {
  router.push('/order/submit')
}
</script>

<style scoped>
.cart-page {
  min-height: 100vh;
  padding-bottom: 70px;
}

.cart-list {
  padding: 10px;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  border-radius: 12px;
  padding: 12px;
  margin-bottom: 10px;
}

.item-info {
  display: flex;
  gap: 12px;
  flex: 1;
}

.item-image {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
}

.item-detail h3 {
  font-size: 15px;
  color: #333;
  margin-bottom: 8px;
}

.item-detail .price {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #ff4757;
  font-weight: bold;
}

.quantity-control {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.bottom-bar {
  position: fixed;
  bottom: 50px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.total {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 16px;
}

.total .heart {
  font-size: 18px;
}

.total .value {
  font-size: 24px;
  font-weight: bold;
  color: #ff4757;
}

.empty-button {
  width: 120px;
}
</style>
