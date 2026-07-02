<!--
  订单管理页

  管理员操作：确认订单、更新状态
-->
<template>
  <view class="admin-page">
    <!-- 订单列表 -->
    <view v-if="loading" class="loading">
      <text>加载中...</text>
    </view>
    <view v-else-if="orders.length > 0" class="order-list">
      <view
        v-for="order in orders"
        :key="order._id"
        class="order-card"
      >
        <!-- 订单头部 -->
        <view class="order-header">
          <text class="order-no">{{ order.order_no }}</text>
          <text class="status-tag" :class="'status-' + order.status">
            {{ getStatusName(order.status) }}
          </text>
        </view>

        <!-- 订单内容 -->
        <view class="order-content">
          <view class="customer">
            <text class="label">点菜人：</text>
            <text>{{ order.customer_name }}</text>
          </view>
          <view class="items">
            <text v-for="(item, index) in order.items.slice(0, 3)" :key="index" class="item-tag">
              {{ item.name }}
            </text>
          </view>
          <view class="total">
            <text class="heart">❤️</text>
            <text class="value">{{ order.total_hearts }}</text>
          </view>
        </view>

        <!-- 操作按钮 -->
        <view class="actions">
          <view v-if="order.status === 'pending'" class="btn-action btn-primary" @tap="handleStatusChange(order._id, 'confirmed')">
            <text>确认订单</text>
          </view>
          <view v-if="order.status === 'confirmed'" class="btn-action btn-warning" @tap="handleStatusChange(order._id, 'cooking')">
            <text>开始制作</text>
          </view>
          <view v-if="order.status === 'cooking'" class="btn-action btn-success" @tap="handleStatusChange(order._id, 'ready')">
            <text>已出锅</text>
          </view>
          <view v-if="order.status === 'ready'" class="btn-action btn-default" @tap="handleStatusChange(order._id, 'completed')">
            <text>完成</text>
          </view>
          <view class="btn-action btn-danger" @tap="handleDelete(order._id)">
            <text>删除</text>
          </view>
        </view>
      </view>
    </view>
    <view v-else class="empty">
      <text>暂无订单</text>
    </view>
  </view>
</template>

<script>
import { getOrders, updateOrderStatus, deleteOrder } from '../../api/index.js'

export default {
  data() {
    return {
      orders: [],
      loading: false
    }
  },
  onLoad() {
    this.loadOrders()
  },
  methods: {
    async loadOrders() {
      this.loading = true
      try {
        const data = await getOrders({ page_size: 50 })
        this.orders = data.items
      } catch (e) {
        console.error('加载订单失败:', e)
      } finally {
        this.loading = false
      }
    },
    async handleStatusChange(id, status) {
      try {
        await updateOrderStatus(id, { status, note: `状态变更为${this.getStatusName(status)}` })
        uni.showToast({ title: '操作成功', icon: 'success' })
        this.loadOrders()
      } catch (e) {
        console.error('更新状态失败:', e)
        uni.showToast({ title: '操作失败', icon: 'none' })
      }
    },
    handleDelete(id) {
      uni.showModal({
        title: '提示',
        content: '确定要删除这个订单吗？',
        success: async (res) => {
          if (res.confirm) {
            try {
              await deleteOrder(id)
              uni.showToast({ title: '删除成功', icon: 'success' })
              this.loadOrders()
            } catch (e) {
              console.error('删除失败:', e)
            }
          }
        }
      })
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
    }
  }
}
</script>

<style scoped>
.admin-page {
  min-height: 100vh;
  background: #f5f5f5;
}

.order-list {
  padding: 20rpx;
}

.order-card {
  background: white;
  border-radius: 16rpx;
  padding: 24rpx;
  margin-bottom: 20rpx;
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16rpx;
}

.order-no {
  font-size: 24rpx;
  color: #999;
}

.status-tag {
  font-size: 22rpx;
  padding: 6rpx 16rpx;
  border-radius: 8rpx;
}

.status-pending {
  background: #fff7e6;
  color: #fa8c16;
}

.status-confirmed, .status-cooking {
  background: #e6f7ff;
  color: #1890ff;
}

.status-ready {
  background: #f6ffed;
  color: #52c41a;
}

.status-completed {
  background: #f5f5f5;
  color: #999;
}

.order-content {
  margin-bottom: 20rpx;
}

.customer {
  font-size: 28rpx;
  color: #333;
  margin-bottom: 12rpx;
}

.customer .label {
  color: #999;
}

.items {
  display: flex;
  flex-wrap: wrap;
  gap: 12rpx;
  margin-bottom: 12rpx;
}

.item-tag {
  background: #f5f5f5;
  padding: 6rpx 16rpx;
  border-radius: 24rpx;
  font-size: 24rpx;
  color: #666;
}

.total {
  display: flex;
  align-items: center;
}

.total .heart {
  font-size: 28rpx;
}

.total .value {
  font-size: 36rpx;
  font-weight: bold;
  color: #ff4757;
  margin-left: 6rpx;
}

.actions {
  display: flex;
  gap: 16rpx;
  flex-wrap: wrap;
  padding-top: 20rpx;
  border-top: 2rpx solid #f5f5f5;
}

.btn-action {
  padding: 12rpx 24rpx;
  border-radius: 8rpx;
  font-size: 24rpx;
}

.btn-primary {
  background: #1890ff;
  color: white;
}

.btn-warning {
  background: #fa8c16;
  color: white;
}

.btn-success {
  background: #52c41a;
  color: white;
}

.btn-default {
  background: #f5f5f5;
  color: #666;
}

.btn-danger {
  background: #fff1f0;
  color: #ff4d4f;
}

.loading, .empty {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 100rpx;
  color: #999;
}
</style>
