<!--
  订单详情页

  展示订单完整信息和状态流转
-->
<template>
  <view class="order-detail" v-if="order">
    <!-- 订单状态 -->
    <view class="status-section">
      <text class="status-icon">{{ getStatusIcon(order.status) }}</text>
      <text class="status-text">{{ getStatusName(order.status) }}</text>
      <text class="order-no">订单号：{{ order.order_no }}</text>
    </view>

    <!-- 点菜人信息 -->
    <view class="section">
      <view class="info-row">
        <text class="label">👤 点菜人</text>
        <text class="value">{{ order.customer_name }}</text>
      </view>
      <view class="info-row">
        <text class="label">⏰ 下单时间</text>
        <text class="value">{{ formatTime(order.created_at) }}</text>
      </view>
    </view>

    <!-- 已选菜品 -->
    <view class="section">
      <text class="section-title">🍽️ 已选菜品</text>
      <view v-for="item in order.items" :key="item.recipe_id" class="order-item">
        <text class="name">{{ item.name }}</text>
        <text class="quantity">x{{ item.quantity }}</text>
        <text class="price">❤️ {{ item.price_hearts * item.quantity }}</text>
      </view>
      <view class="total-row">
        <text>合计：</text>
        <text class="heart">❤️</text>
        <text class="value">{{ order.total_hearts }}</text>
      </view>
    </view>

    <!-- 备注 -->
    <view v-if="order.remark" class="section">
      <text class="section-title">📝 备注</text>
      <text class="remark">{{ order.remark }}</text>
    </view>

    <!-- 状态流转记录 -->
    <view class="section">
      <text class="section-title">📋 状态记录</text>
      <view class="timeline">
        <view v-for="(record, index) in order.status_history" :key="index" class="timeline-item">
          <view class="timeline-dot"></view>
          <view class="timeline-content">
            <text class="timeline-title">{{ getStatusName(record.status) }}</text>
            <text class="timeline-time">{{ formatTime(record.time) }}</text>
            <text v-if="record.note" class="timeline-note">{{ record.note }}</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 操作按钮 -->
    <view v-if="order.status === 'pending'" class="action-bar">
      <view class="btn-confirm" @tap="handleConfirm">
        <text>✅ 确认订单</text>
      </view>
    </view>
  </view>

  <!-- 加载状态 -->
  <view v-else class="loading">
    <text>加载中...</text>
  </view>
</template>

<script>
import { getOrder, updateOrderStatus } from '../../api/index.js'

export default {
  data() {
    return {
      order: null
    }
  },
  onLoad(options) {
    if (options.id) {
      this.loadOrder(options.id)
    }
  },
  methods: {
    async loadOrder(id) {
      try {
        this.order = await getOrder(id)
      } catch (e) {
        console.error('加载订单详情失败:', e)
        uni.showToast({ title: '加载失败', icon: 'none' })
      }
    },
    async handleConfirm() {
      try {
        await updateOrderStatus(this.order._id, {
          status: 'confirmed',
          note: '已确认订单'
        })
        uni.showToast({ title: '已确认', icon: 'success' })
        this.loadOrder(this.order._id)
      } catch (e) {
        console.error('确认订单失败:', e)
        uni.showToast({ title: '操作失败', icon: 'none' })
      }
    },
    getStatusIcon(status) {
      const icons = {
        pending: '⏳',
        confirmed: '✅',
        cooking: '🍳',
        ready: '🍽️',
        completed: '🎉'
      }
      return icons[status] || '❓'
    },
    getStatusName(status) {
      const names = {
        pending: '待确认',
        confirmed: '已确认',
        cooking: '制作中',
        ready: '已出锅',
        completed: '已完成'
      }
      return names[status] || status
    },
    formatTime(timeStr) {
      const date = new Date(timeStr)
      const month = date.getMonth() + 1
      const day = date.getDate()
      const hours = date.getHours().toString().padStart(2, '0')
      const minutes = date.getMinutes().toString().padStart(2, '0')
      return `${month}月${day}日 ${hours}:${minutes}`
    }
  }
}
</script>

<style scoped>
.order-detail {
  min-height: 100vh;
  background: #f5f5f5;
  padding-bottom: 160rpx;
}

.status-section {
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  color: white;
  padding: 60rpx 40rpx;
  text-align: center;
}

.status-icon {
  font-size: 96rpx;
  display: block;
  margin-bottom: 16rpx;
}

.status-text {
  font-size: 40rpx;
  font-weight: bold;
  display: block;
  margin-bottom: 12rpx;
}

.order-no {
  font-size: 26rpx;
  opacity: 0.9;
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

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 16rpx 0;
  border-bottom: 2rpx solid #f5f5f5;
}

.info-row:last-child {
  border-bottom: none;
}

.info-row .label {
  color: #999;
}

.info-row .value {
  color: #333;
}

.order-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16rpx 0;
  border-bottom: 2rpx solid #f5f5f5;
}

.order-item:last-child {
  border-bottom: none;
}

.order-item .name {
  flex: 1;
  font-size: 28rpx;
  color: #333;
}

.order-item .quantity {
  color: #999;
  margin: 0 24rpx;
}

.order-item .price {
  color: #ff4757;
  font-weight: bold;
}

.total-row {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding-top: 20rpx;
  border-top: 2rpx solid #f5f5f5;
  margin-top: 12rpx;
  font-size: 32rpx;
}

.total-row .heart {
  font-size: 36rpx;
  margin-left: 12rpx;
}

.total-row .value {
  font-size: 44rpx;
  font-weight: bold;
  color: #ff4757;
  margin-left: 12rpx;
}

.remark {
  font-size: 28rpx;
  color: #666;
  line-height: 1.6;
}

.timeline {
  position: relative;
  padding-left: 40rpx;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 12rpx;
  top: 0;
  bottom: 0;
  width: 4rpx;
  background: #ff6b6b;
}

.timeline-item {
  position: relative;
  margin-bottom: 30rpx;
}

.timeline-dot {
  position: absolute;
  left: -36rpx;
  top: 8rpx;
  width: 20rpx;
  height: 20rpx;
  background: #ff6b6b;
  border-radius: 50%;
}

.timeline-title {
  font-size: 28rpx;
  color: #333;
  font-weight: 600;
  display: block;
}

.timeline-time {
  font-size: 24rpx;
  color: #999;
  display: block;
  margin-top: 6rpx;
}

.timeline-note {
  font-size: 24rpx;
  color: #666;
  display: block;
  margin-top: 6rpx;
}

.action-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20rpx 30rpx;
  background: white;
  box-shadow: 0 -4rpx 20rpx rgba(0, 0, 0, 0.1);
}

.btn-confirm {
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  color: white;
  text-align: center;
  padding: 24rpx;
  border-radius: 48rpx;
  font-size: 32rpx;
  font-weight: 600;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #999;
}
</style>
