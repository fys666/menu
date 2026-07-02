<!--
  订单列表页视图

  展示所有订单记录：
  - 订单状态筛选
  - 订单列表
  - 点击查看订单详情
-->

<template>
  <div class="order-list-page">
    <!-- 顶部标题 -->
    <van-nav-bar title="订单记录" />

    <!-- 状态筛选 -->
    <div class="filter-bar">
      <van-tabs v-model:active="activeStatus" @change="handleStatusChange">
        <van-tab title="全部" name="" />
        <van-tab title="待确认" name="pending" />
        <van-tab title="制作中" name="cooking" />
        <van-tab title="已完成" name="completed" />
      </van-tabs>
    </div>

    <!-- 订单列表 -->
    <div v-if="loading" class="loading">
      <van-loading type="ball" />
    </div>
    <div v-else-if="orders.length > 0" class="order-list">
      <div
        v-for="order in orders"
        :key="order._id"
        class="order-card"
        @click="goToDetail(order._id)"
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
            <span v-if="order.items.length > 3" class="more">等{{ order.items.length }}道菜</span>
          </div>
        </div>

        <!-- 订单底部 -->
        <div class="order-footer">
          <span class="time">{{ formatTime(order.created_at) }}</span>
          <div class="total">
            <span class="heart">❤️</span>
            <span class="value">{{ order.total_hearts }}</span>
          </div>
        </div>
      </div>
    </div>
    <van-empty v-else description="暂无订单记录" />
  </div>
</template>

<script setup>
/**
 * 订单列表页组件逻辑
 *
 * 功能：
 * 1. 加载订单列表
 * 2. 按状态筛选
 * 3. 格式化时间
 * 4. 跳转到订单详情页
 */
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getOrders } from '../api'

const router = useRouter()

// 当前选中的状态
const activeStatus = ref('')

// 订单数据
const orders = ref([])

// 加载状态
const loading = ref(false)

/**
 * 加载订单列表
 * @param {string} status - 状态筛选
 */
const loadOrders = async (status = '') => {
  loading.value = true
  try {
    const data = await getOrders({ status, page_size: 50 })
    orders.value = data.items
  } catch (error) {
    console.error('加载订单失败:', error)
  } finally {
    loading.value = false
  }
}

/**
 * 状态变化处理
 */
const handleStatusChange = (status) => {
  loadOrders(status)
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

/**
 * 格式化时间
 * @param {string} timeStr - 时间字符串
 */
const formatTime = (timeStr) => {
  const date = new Date(timeStr)
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')
  return `${month}月${day}日 ${hours}:${minutes}`
}

/**
 * 跳转到订单详情页
 * @param {string} id - 订单ID
 */
const goToDetail = (id) => {
  router.push(`/order/${id}`)
}

// 页面加载时获取数据
onMounted(() => {
  loadOrders()
})
</script>

<style scoped>
.order-list-page {
  min-height: 100vh;
  background: #f5f5f5;
}

.filter-bar {
  background: white;
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
  margin-bottom: 10px;
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
}

.item-tag {
  background: #f5f5f5;
  padding: 4px 10px;
  border-radius: 15px;
  font-size: 12px;
  color: #666;
}

.more {
  font-size: 12px;
  color: #999;
}

.order-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 10px;
  border-top: 1px solid #f5f5f5;
}

.order-footer .time {
  font-size: 12px;
  color: #999;
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

.loading {
  display: flex;
  justify-content: center;
  padding: 40px;
}
</style>
