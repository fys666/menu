<!--
  购物车/已点菜品页

  设计风格：温馨的点餐清单
-->
<template>
  <view class="cart-page">
    <!-- 顶部标题 -->
    <view class="page-header">
      <text class="header-icon">🛒</text>
      <text class="header-title">已点菜品</text>
      <text class="header-count" v-if="cartItems.length">{{ cartItems.length }}道</text>
    </view>

    <!-- 购物车列表 -->
    <view v-if="cartItems.length > 0" class="cart-list">
      <view
        v-for="(item, index) in cartItems"
        :key="item.id"
        class="cart-item"
        :style="{ animationDelay: index * 0.08 + 's' }"
      >
        <view class="item-image-wrap">
          <image :src="item.image || defaultImage" class="item-image" mode="aspectFill" />
        </view>
        <view class="item-content">
          <text class="item-name">{{ item.name }}</text>
          <view class="item-price">
            <text class="price-heart">❤️</text>
            <text class="price-value">{{ item.price_hearts }}</text>
          </view>
          <view class="quantity-control">
            <view class="qty-btn qty-minus" @tap="decreaseQuantity(item)">
              <text>−</text>
            </view>
            <text class="qty-value">{{ item.quantity }}</text>
            <view class="qty-btn qty-plus" @tap="increaseQuantity(item)">
              <text>+</text>
            </view>
          </view>
        </view>
        <view class="item-delete" @tap="removeItem(item.id)">
          <text class="delete-icon">✕</text>
        </view>
      </view>
    </view>

    <!-- 空状态 -->
    <view v-else class="empty-state">
      <view class="empty-illustration">
        <text class="empty-emoji">🍽️</text>
      </view>
      <text class="empty-title">还没有选择菜品</text>
      <text class="empty-desc">去菜单看看有什么好吃的吧</text>
      <view class="empty-btn" @tap="goToHome">
        <text>去点菜</text>
      </view>
    </view>

    <!-- 底部结算栏 -->
    <view v-if="cartItems.length > 0" class="bottom-bar">
      <view class="total-section">
        <text class="total-label">合计</text>
        <view class="total-price">
          <text class="total-heart">❤️</text>
          <text class="total-value">{{ totalHearts }}</text>
        </view>
      </view>
      <view class="btn-submit" @tap="goToSubmit">
        <text class="submit-text">提交订单</text>
        <text class="submit-arrow">→</text>
      </view>
    </view>
  </view>
</template>

<script>
import { getCart, updateQuantity, removeFromCart, getTotalHearts } from '../../store/cart.js'

export default {
  data() {
    return {
      cartItems: [],
      totalHearts: 0,
      defaultImage: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400'
    }
  },
  onShow() {
    this.refreshCart()
  },
  methods: {
    refreshCart() {
      this.cartItems = getCart()
      this.totalHearts = getTotalHearts()
    },
    increaseQuantity(item) {
      updateQuantity(item.id, item.quantity + 1)
      this.refreshCart()
    },
    decreaseQuantity(item) {
      if (item.quantity > 1) {
        updateQuantity(item.id, item.quantity - 1)
        this.refreshCart()
      }
    },
    removeItem(id) {
      uni.showModal({
        title: '提示',
        content: '确定要删除这道菜吗？',
        confirmColor: '#E8734A',
        success: (res) => {
          if (res.confirm) {
            removeFromCart(id)
            this.refreshCart()
          }
        }
      })
    },
    goToHome() {
      uni.switchTab({ url: '/pages/index/index' })
    },
    goToSubmit() {
      uni.navigateTo({ url: '/pages/order-submit/index' })
    }
  }
}
</script>

<style scoped>
.cart-page {
  min-height: 100vh;
  padding-bottom: 180rpx;
  background: var(--color-bg);
}

/* ==================== 页面标题 ==================== */
.page-header {
  display: flex;
  align-items: center;
  gap: 12rpx;
  padding: 30rpx 30rpx 20rpx;
}

.header-icon {
  font-size: 40rpx;
}

.header-title {
  font-size: 38rpx;
  font-weight: 700;
  color: var(--color-text);
}

.header-count {
  font-size: 24rpx;
  color: var(--color-primary);
  background: rgba(232, 115, 74, 0.1);
  padding: 6rpx 14rpx;
  border-radius: 16rpx;
  font-weight: 600;
}

/* ==================== 购物车列表 ==================== */
.cart-list {
  padding: 0 24rpx;
}

.cart-item {
  display: flex;
  align-items: center;
  gap: 20rpx;
  background: var(--color-card);
  border-radius: 24rpx;
  padding: 24rpx;
  margin-bottom: 20rpx;
  box-shadow: 0 4rpx 20rpx rgba(0,0,0,0.04);
  animation: fadeInUp 0.4s ease-out forwards;
  opacity: 0;
}

.item-image-wrap {
  width: 140rpx;
  height: 140rpx;
  border-radius: 16rpx;
  overflow: hidden;
  flex-shrink: 0;
}

.item-image {
  width: 100%;
  height: 100%;
}

.item-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12rpx;
}

.item-name {
  font-size: 30rpx;
  font-weight: 600;
  color: var(--color-text);
}

.item-price {
  display: flex;
  align-items: center;
  gap: 6rpx;
}

.price-heart {
  font-size: 24rpx;
}

.price-value {
  font-size: 32rpx;
  font-weight: 700;
  color: var(--color-heart);
}

/* 数量控制 */
.quantity-control {
  display: flex;
  align-items: center;
  gap: 20rpx;
}

.qty-btn {
  width: 48rpx;
  height: 48rpx;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.qty-minus {
  background: var(--color-bg);
}

.qty-minus text {
  font-size: 32rpx;
  color: var(--color-text-secondary);
}

.qty-plus {
  background: var(--color-primary);
  box-shadow: 0 4rpx 12rpx rgba(232, 115, 74, 0.3);
}

.qty-plus text {
  font-size: 32rpx;
  color: white;
}

.qty-value {
  font-size: 32rpx;
  font-weight: 600;
  color: var(--color-text);
  min-width: 48rpx;
  text-align: center;
}

/* 删除按钮 */
.item-delete {
  width: 56rpx;
  height: 56rpx;
  border-radius: 50%;
  background: rgba(230, 57, 70, 0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.delete-icon {
  font-size: 24rpx;
  color: var(--color-heart);
}

/* ==================== 空状态 ==================== */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 160rpx 0;
}

.empty-illustration {
  width: 200rpx;
  height: 200rpx;
  background: var(--color-card);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 40rpx;
  box-shadow: 0 8rpx 32rpx rgba(0,0,0,0.06);
}

.empty-emoji {
  font-size: 80rpx;
}

.empty-title {
  font-size: 32rpx;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 12rpx;
}

.empty-desc {
  font-size: 26rpx;
  color: var(--color-text-secondary);
  margin-bottom: 40rpx;
}

.empty-btn {
  background: var(--color-primary);
  padding: 20rpx 60rpx;
  border-radius: 40rpx;
}

.empty-btn text {
  color: white;
  font-size: 28rpx;
  font-weight: 600;
}

/* ==================== 底部结算栏 ==================== */
.bottom-bar {
  position: fixed;
  bottom: 100rpx;
  left: 0; right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24rpx 30rpx;
  background: var(--color-card);
  box-shadow: 0 -8rpx 32rpx rgba(0,0,0,0.08);
}

.total-section {
  display: flex;
  flex-direction: column;
  gap: 4rpx;
}

.total-label {
  font-size: 22rpx;
  color: var(--color-text-secondary);
}

.total-price {
  display: flex;
  align-items: baseline;
  gap: 6rpx;
}

.total-heart {
  font-size: 32rpx;
}

.total-value {
  font-size: 48rpx;
  font-weight: 700;
  color: var(--color-heart);
}

.btn-submit {
  display: flex;
  align-items: center;
  gap: 12rpx;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  padding: 24rpx 48rpx;
  border-radius: 48rpx;
  box-shadow: 0 8rpx 24rpx rgba(232, 115, 74, 0.3);
}

.btn-submit:active {
  transform: scale(0.98);
}

.submit-text {
  font-size: 30rpx;
  font-weight: 600;
  color: white;
}

.submit-arrow {
  font-size: 28rpx;
  color: white;
}
</style>
