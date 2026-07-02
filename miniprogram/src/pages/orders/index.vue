<!--
  订单列表页

  设计风格：温馨的订单卡片
-->
<template>
  <view class="orders-page">
    <!-- 顶部标题 -->
    <view class="page-header">
      <text class="header-icon">📋</text>
      <text class="header-title">订单记录</text>
    </view>

    <!-- 状态筛选 -->
    <view class="filter-section">
      <scroll-view scroll-x :show-scrollbar="false">
        <view class="filter-list">
          <view
            v-for="tab in tabs"
            :key="tab.value"
            class="filter-chip"
            :class="{ active: currentStatus === tab.value }"
            @tap="switchTab(tab.value)"
          >
            <text>{{ tab.label }}</text>
          </view>
        </view>
      </scroll-view>
    </view>

    <!-- 订单列表 -->
    <view v-if="loading" class="loading-state">
      <text>加载中...</text>
    </view>

    <view v-else-if="orders.length > 0" class="order-list">
      <view
        v-for="(order, index) in orders"
        :key="order._id"
        class="order-card"
        :style="{ animationDelay: index * 0.1 + 's' }"
        @tap="goToDetail(order._id)"
      >
        <!-- 订单头部 -->
        <view class="card-header">
          <view class="order-info">
            <text class="order-no">{{ order.order_no }}</text>
            <text class="order-time">{{ formatTime(order.created_at) }}</text>
          </view>
          <view class="status-badge" :class="'status-' + order.status">
            <text>{{ getStatusName(order.status) }}</text>
          </view>
        </view>

        <!-- 订单内容 -->
        <view class="card-body">
          <view class="customer-row">
            <text class="customer-avatar">👤</text>
            <text class="customer-name">{{ order.customer_name }}</text>
          </view>

          <view class="items-preview">
            <view v-for="(item, idx) in order.items.slice(0, 4)" :key="idx" class="item-chip">
              <text>{{ item.name }}</text>
            </view>
            <view v-if="order.items.length > 4" class="item-more">
              <text>+{{ order.items.length - 4 }}</text>
            </view>
          </view>
        </view>

        <!-- 订单底部 -->
        <view class="card-footer">
          <view class="footer-total">
            <text class="total-heart">❤️</text>
            <text class="total-value">{{ order.total_hearts }}</text>
          </view>
          <view class="footer-arrow">
            <text>查看详情 →</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 空状态 -->
    <view v-else class="empty-state">
      <view class="empty-illustration">
        <text class="empty-emoji">📭</text>
      </view>
      <text class="empty-title">暂无订单记录</text>
      <text class="empty-desc">快去点几道菜吧</text>
    </view>
  </view>
</template>

<script>
import { getOrders } from '../../api/index.js'

export default {
  data() {
    return {
      tabs: [
        { label: '全部', value: '' },
        { label: '待确认', value: 'pending' },
        { label: '制作中', value: 'cooking' },
        { label: '已完成', value: 'completed' }
      ],
      currentStatus: '',
      orders: [],
      loading: false
    }
  },
  onShow() {
    this.loadOrders()
  },
  methods: {
    async loadOrders() {
      this.loading = true
      try {
        const data = await getOrders({ status: this.currentStatus, page_size: 50 })
        this.orders = data.items
      } catch (e) {
        console.error('加载订单失败:', e)
      } finally {
        this.loading = false
      }
    },
    switchTab(status) {
      this.currentStatus = status
      this.loadOrders()
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
    },
    goToDetail(id) {
      uni.navigateTo({ url: `/pages/order-detail/index?id=${id}` })
    }
  }
}
</script>

<style scoped>
.orders-page {
  min-height: 100vh;
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

/* ==================== 筛选栏 ==================== */
.filter-section {
  padding: 0 24rpx 20rpx;
}

.filter-list {
  display: inline-flex;
  gap: 16rpx;
}

.filter-chip {
  padding: 14rpx 28rpx;
  background: var(--color-card);
  border-radius: 32rpx;
  box-shadow: 0 2rpx 12rpx rgba(0,0,0,0.04);
}

.filter-chip text {
  font-size: 26rpx;
  color: var(--color-text-secondary);
  font-weight: 500;
}

.filter-chip.active {
  background: var(--color-primary);
}

.filter-chip.active text {
  color: white;
}

/* ==================== 订单列表 ==================== */
.order-list {
  padding: 0 24rpx;
}

.order-card {
  background: var(--color-card);
  border-radius: 24rpx;
  padding: 28rpx;
  margin-bottom: 20rpx;
  box-shadow: 0 4rpx 20rpx rgba(0,0,0,0.04);
  animation: fadeInUp 0.4s ease-out forwards;
  opacity: 0;
}

.order-card:active {
  transform: scale(0.99);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20rpx;
}

.order-info {
  display: flex;
  flex-direction: column;
  gap: 6rpx;
}

.order-no {
  font-size: 24rpx;
  color: var(--color-text-secondary);
}

.order-time {
  font-size: 22rpx;
  color: var(--color-text-secondary);
  opacity: 0.7;
}

.status-badge {
  padding: 8rpx 20rpx;
  border-radius: 20rpx;
  font-size: 22rpx;
  font-weight: 600;
}

.status-pending {
  background: rgba(244, 162, 97, 0.15);
  color: var(--color-primary);
}

.status-confirmed, .status-cooking {
  background: rgba(232, 115, 74, 0.1);
  color: var(--color-primary);
}

.status-ready {
  background: rgba(82, 183, 136, 0.15);
  color: var(--color-success);
}

.status-completed {
  background: var(--color-bg);
  color: var(--color-text-secondary);
}

.card-body {
  margin-bottom: 20rpx;
}

.customer-row {
  display: flex;
  align-items: center;
  gap: 10rpx;
  margin-bottom: 16rpx;
}

.customer-avatar {
  font-size: 28rpx;
}

.customer-name {
  font-size: 28rpx;
  font-weight: 600;
  color: var(--color-text);
}

.items-preview {
  display: flex;
  flex-wrap: wrap;
  gap: 12rpx;
}

.item-chip {
  background: var(--color-bg);
  padding: 8rpx 18rpx;
  border-radius: 16rpx;
}

.item-chip text {
  font-size: 24rpx;
  color: var(--color-text-secondary);
}

.item-more {
  background: var(--color-primary);
  padding: 8rpx 18rpx;
  border-radius: 16rpx;
}

.item-more text {
  font-size: 24rpx;
  color: white;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 20rpx;
  border-top: 2rpx solid var(--color-border);
}

.footer-total {
  display: flex;
  align-items: center;
  gap: 6rpx;
}

.total-heart {
  font-size: 28rpx;
}

.total-value {
  font-size: 40rpx;
  font-weight: 700;
  color: var(--color-heart);
}

.footer-arrow {
  font-size: 24rpx;
  color: var(--color-primary);
  font-weight: 500;
}

/* ==================== 空状态 ==================== */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 160rpx 0;
}

.empty-illustration {
  width: 180rpx;
  height: 180rpx;
  background: var(--color-card);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 32rpx;
  box-shadow: 0 8rpx 32rpx rgba(0,0,0,0.06);
}

.empty-emoji {
  font-size: 72rpx;
}

.empty-title {
  font-size: 32rpx;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 10rpx;
}

.empty-desc {
  font-size: 26rpx;
  color: var(--color-text-secondary);
}

.loading-state {
  display: flex;
  justify-content: center;
  padding: 100rpx;
  color: var(--color-text-secondary);
}
</style>
