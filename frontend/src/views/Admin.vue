<!--
  订单管理页视图

  管理员操作：
  - 查看所有订单
  - 更新订单状态
  - 状态流转操作
-->

<template>
  <div class="admin-page">
    <!-- 顶部导航 -->
    <van-nav-bar title="订单管理" left-arrow @click-left="goBack" />

    <!-- 订单列表 -->
    <div v-if="loading" class="loading">
      <van-loading type="ball" />
    </div>
    <div v-else-if="orders.length > 0" class="order-list">
      <div
        v-for="order in orders"
        :key="order._id"
        class="order-card"
      >
        <!-- 订单头部 -->
        <div class="order-header">
          <span class="order-no">{{ order.order_no }}</span>
          <van-tag :type="getStatusType(order.status)">
            {{ getStatusName(order.status) }}
          </van-tag>
        </div>

        <!-- 订单内容 -->
        <div class="order-content">
          <div class="customer">
            <span class="label">点菜人：</span>
            <span>{{ order.customer_name }}</span>
          </div>
          <div class="items">
            <span v-for="(item, index) in order.items.slice(0, 3)" :key="index" class="item-tag">
              {{ item.name }}
            </span>
          </div>
          <div class="total">
            <span class="heart">❤️</span>
            <span class="value">{{ order.total_hearts }}</span>
          </div>
        </div>

        <!-- 操作按钮 -->
        <div class="actions">
          <van-button
            v-if="order.status === 'pending'"
            type="primary"
            size="small"
            @click="handleStatusChange(order._id, 'confirmed')"
          >
            确认订单
          </van-button>
          <van-button
            v-if="order.status === 'confirmed'"
            type="warning"
            size="small"
            @click="handleStatusChange(order._id, 'cooking')"
          >
            开始制作
          </van-button>
          <van-button
            v-if="order.status === 'cooking'"
            type="success"
            size="small"
            @click="handleStatusChange(order._id, 'ready')"
          >
            已出锅
          </van-button>
          <van-button
            v-if="order.status === 'ready'"
            type="default"
            size="small"
            @click="handleStatusChange(order._id, 'completed')"
          >
            完成
          </van-button>
          <van-button
            type="danger"
            size="small"
            plain
            @click="handleDelete(order._id)"
          >
            删除
          </van-button>
        </div>
      </div>
    </div>
    <van-empty v-else description="暂无订单" />
  </div>
</template>

<script setup>
/**
 * 订单管理页组件逻辑
 *
 * 功能：
 * 1. 加载所有订单
 * 2. 更新订单状态
 * 3. 删除订单
 */
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getOrders, updateOrderStatus, deleteOrder } from '../api'
import { showToast, showSuccessToast, showConfirmDialog } from 'vant'

const router = useRouter()

// 订单数据
const orders = ref([])

// 加载状态
const loading = ref(false)

/**
 * 加载订单列表
 */
const loadOrders = async () => {
  loading.value = true
  try {
    const data = await getOrders({ page_size: 50 })
    orders.value = data.items
  } catch (error) {
    console.error('加载订单失败:', error)
  } finally {
    loading.value = false
  }
}

/**
 * 更新订单状态
 * @param {string} id - 订单ID
 * @param {string} status - 新状态
 */
const handleStatusChange = async (id, status) => {
  try {
    await updateOrderStatus(id, { status, note: `状态变更为${getStatusName(status)}` })
    showSuccessToast('操作成功')
    loadOrders() // 刷新列表
  } catch (error) {
    console.error('更新状态失败:', error)
    showToast('操作失败')
  }
}

/**
 * 删除订单
 * @param {string} id - 订单ID
 */
const handleDelete = async (id) => {
  try {
    await showConfirmDialog({
      title: '提示',
      message: '确定要删除这个订单吗？'
    })
    await deleteOrder(id)
    showSuccessToast('删除成功')
    loadOrders() // 刷新列表
  } catch {
    // 用户取消
  }
}

/**
 * 返回上一页
 */
const goBack = () => {
  router.back()
}

/**
 * 获取状态类型（用于标签颜色）
 * @param {string} status - 状态值
 */
const getStatusType = (status) => {
  const types = {
    pending: 'warning',
    confirmed: 'primary',
    cooking: 'primary',
    ready: 'success',
    completed: 'default'
  }
  return types[status] || 'default'
}

/**
 * 获取状态中文名称
 * @param {string} status - 状态值
 */
const getStatusName = (status) => {
  const names = {
    pending: '待确认',
    confirmed: '已确认',
    cooking: '制作中',
    ready: '已出锅',
    completed: '已完成'
  }
  return names[status] || status
}

// 页面加载时获取数据
onMounted(() => {
  loadOrders()
})
</script>

<style scoped>
.admin-page {
  min-height: 100vh;
  background: #f5f5f5;
}

.order-list {
  padding: 10px;
}

.order-card {
  background: white;
  border-radius: 12px;
  padding: 15px;
  margin-bottom: 10px;
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.order-no {
  font-size: 13px;
  color: #999;
}

.order-content {
  margin-bottom: 12px;
}

.customer {
  font-size: 14px;
  color: #333;
  margin-bottom: 8px;
}

.customer .label {
  color: #999;
}

.items {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}

.item-tag {
  background: #f5f5f5;
  padding: 4px 10px;
  border-radius: 15px;
  font-size: 12px;
  color: #666;
}

.total {
  display: flex;
  align-items: center;
  gap: 4px;
}

.total .heart {
  font-size: 14px;
}

.total .value {
  font-size: 18px;
  font-weight: bold;
  color: #ff4757;
}

.actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  padding-top: 12px;
  border-top: 1px solid #f5f5f5;
}

.loading {
  display: flex;
  justify-content: center;
  padding: 40px;
}
</style>
