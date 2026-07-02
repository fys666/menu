<!--
  提交订单页

  使用微信用户信息自动填充点菜人
-->
<template>
  <view class="order-submit">
    <!-- 点菜人（自动填充） -->
    <view class="section">
      <text class="section-title">👤 点菜人</text>
      <view class="user-info" v-if="userInfo">
        <image v-if="userInfo.avatar" :src="userInfo.avatar" class="avatar" />
        <view v-else class="avatar-placeholder">
          <text>{{ userInfo.nickname ? userInfo.nickname[0] : '?' }}</text>
        </view>
        <view class="user-detail">
          <text class="nickname">{{ userInfo.nickname || '微信用户' }}</text>
          <text class="hint">已自动获取微信信息</text>
        </view>
      </view>
      <view v-else class="user-info">
        <view class="avatar-placeholder">
          <text>?</text>
        </view>
        <view class="user-detail">
          <input
            class="input"
            placeholder="请输入点菜人姓名"
            v-model="customerName"
          />
        </view>
      </view>
    </view>

    <!-- 已选菜品 -->
    <view class="section">
      <text class="section-title">🍽️ 已选菜品</text>
      <view v-for="item in cartItems" :key="item.id" class="order-item">
        <text class="name">{{ item.name }} x{{ item.quantity }}</text>
        <text class="price">❤️ {{ item.price_hearts * item.quantity }}</text>
      </view>
    </view>

    <!-- 总计 -->
    <view class="section total-section">
      <text>合计：</text>
      <text class="heart">❤️</text>
      <text class="value">{{ totalHearts }}</text>
    </view>

    <!-- 备注 -->
    <view class="section">
      <text class="section-title">📝 备注</text>
      <textarea
        class="textarea"
        placeholder="有什么特殊要求吗？（选填）"
        v-model="remark"
        maxlength="200"
      />
    </view>

    <!-- 提交按钮 -->
    <view class="submit-bar">
      <view class="btn-submit" :class="{ disabled: submitting }" @tap="handleSubmit">
        <text>{{ submitting ? '提交中...' : '确认提交订单' }}</text>
      </view>
    </view>
  </view>
</template>

<script>
import { getCart, clearCart, getTotalHearts } from '../../store/cart.js'
import { createOrder } from '../../api/index.js'

export default {
  data() {
    return {
      customerName: '',
      remark: '',
      cartItems: [],
      totalHearts: 0,
      submitting: false,
      userInfo: null
    }
  },
  onLoad() {
    this.cartItems = getCart()
    this.totalHearts = getTotalHearts()

    // 获取微信用户信息
    const app = getApp()
    this.userInfo = app.globalData.userInfo
  },
  methods: {
    async handleSubmit() {
      if (this.submitting) return

      // 获取点菜人姓名
      const name = this.userInfo
        ? (this.userInfo.nickname || '微信用户')
        : this.customerName.trim()

      if (!name) {
        uni.showToast({ title: '请输入点菜人姓名', icon: 'none' })
        return
      }

      if (this.cartItems.length === 0) {
        uni.showToast({ title: '请选择菜品', icon: 'none' })
        return
      }

      this.submitting = true

      try {
        const orderData = {
          customer_name: name,
          items: this.cartItems.map(item => ({
            recipe_id: item.id,
            name: item.name,
            quantity: item.quantity,
            price_hearts: item.price_hearts
          })),
          remark: this.remark.trim()
        }

        const result = await createOrder(orderData)
        clearCart()

        uni.showToast({ title: '下单成功', icon: 'success' })

        setTimeout(() => {
          uni.redirectTo({ url: `/pages/order-detail/index?id=${result._id}` })
        }, 1500)
      } catch (e) {
        console.error('提交订单失败:', e)
        uni.showToast({ title: '提交失败，请重试', icon: 'none' })
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>

<style scoped>
.order-submit {
  min-height: 100vh;
  padding-bottom: 160rpx;
  background: #f5f5f5;
}

.section {
  background: white;
  margin: 20rpx;
  padding: 30rpx;
  border-radius: 16rpx;
}

.section-title {
  font-size: 30rpx;
  color: #333;
  font-weight: 600;
  margin-bottom: 20rpx;
  display: block;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20rpx;
}

.avatar {
  width: 80rpx;
  height: 80rpx;
  border-radius: 50%;
}

.avatar-placeholder {
  width: 80rpx;
  height: 80rpx;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 32rpx;
  font-weight: bold;
}

.user-detail {
  flex: 1;
}

.nickname {
  font-size: 30rpx;
  color: #333;
  font-weight: 600;
  display: block;
}

.hint {
  font-size: 24rpx;
  color: #999;
  display: block;
  margin-top: 6rpx;
}

.input {
  border: 2rpx solid #eee;
  border-radius: 12rpx;
  padding: 20rpx;
  font-size: 28rpx;
  width: 100%;
  box-sizing: border-box;
}

.textarea {
  border: 2rpx solid #eee;
  border-radius: 12rpx;
  padding: 20rpx;
  font-size: 28rpx;
  width: 100%;
  height: 160rpx;
  box-sizing: border-box;
}

.order-item {
  display: flex;
  justify-content: space-between;
  padding: 16rpx 0;
  border-bottom: 2rpx solid #f5f5f5;
}

.order-item:last-child {
  border-bottom: none;
}

.order-item .name {
  font-size: 28rpx;
  color: #333;
}

.order-item .price {
  color: #ff4757;
  font-weight: bold;
}

.total-section {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  font-size: 32rpx;
}

.total-section .heart {
  font-size: 36rpx;
  margin-left: 12rpx;
}

.total-section .value {
  font-size: 44rpx;
  font-weight: bold;
  color: #ff4757;
  margin-left: 12rpx;
}

.submit-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20rpx 30rpx;
  background: white;
  box-shadow: 0 -4rpx 20rpx rgba(0, 0, 0, 0.1);
}

.btn-submit {
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  color: white;
  text-align: center;
  padding: 24rpx;
  border-radius: 48rpx;
  font-size: 32rpx;
  font-weight: 600;
}

.btn-submit.disabled {
  opacity: 0.6;
}
</style>
