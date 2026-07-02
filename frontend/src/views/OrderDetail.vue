<!--
  订单详情页视图

  展示订单完整信息：
  - 订单状态
  - 点菜人信息
  - 已选菜品列表
  - 总爱心数
  - 状态流转时间线
  - 备注信息
-->

<template>
  <div class="order-detail" v-if="order">
    <!-- 顶部导航 -->
    <van-nav-bar title="订单详情" left-arrow @click-left="goBack" />

    <!-- 订单状态 -->
    <div class="status-section">
      <div class="status-icon">{{ getStatusIcon(order.status) }}</div>
      <div class="status-text">{{ getStatusName(order.status) }}</div>
      <div class="order-no">订单号：{{ order.order_no }}</div>
    </div>

    <!-- 点菜人信息 -->
    <div class="section">
      <div class="info-row">
        <span class="label">👤 点菜人</span>
        <span class="value">{{ order.customer_name }}</span>
      </div>
      <div class="info-row">
        <span class="label">⏰ 下单时间</span>
        <span class="value">{{ formatTime(order.created_at) }}</span>
      </div>
    </div>

    <!-- 已选菜品 -->
    <div class="section">
      <h3>🍽️ 已选菜品</h3>
      <div v-for="item in order.items" :key="item.recipe_id" class="order-item">
        <span class="name">{{ item.name }}</span>
        <span class="quantity">x{{ item.quantity }}</span>
        <span class="price">❤️ {{ item.price_hearts * item.quantity }}</span>
      </div>
      <div class="total-row">
        <span>合计：</span>
        <span class="heart">❤️</span>
        <span class="value">{{ order.total_hearts }}</span>
      </div>
    </div>

    <!-- 备注 -->
    <div v-if="order.remark" class="section">
      <h3>📝 备注</h3>
      <p class="remark">{{ order.remark }}</p>
    </div>

    <!-- 状态流转时间线 -->
    <div class="section">
      <h3>📋 状态记录</h3>
      <van-steps direction="vertical" :active="order.status_history.length - 1">
        <van-step v-for="(record, index) in order.status_history" :key="index">
          <h4>{{ getStatusName(record.status) }}</h4>
          <p>{{ formatTime(record.time) }}</p>
          <p v-if="record.note" class="note">{{ record.note }}</p>
        </van-step>
      </van-steps>
    </div>

    <!-- 管理按钮（仅待确认状态显示） -->
    <div v-if="order.status === 'pending'" class="action-bar">
      <van-button type="primary" block round @click="handleConfirm">
        ✅ 确认订单
      </van-button>
    </div>
  </div>

  <!-- 加载状态 -->
  <div v-else class="loading">
    <van-loading type="ball" />
  </div>
</template>

<script setup>
/**
 * 订单详情页组件逻辑
 *
 * 功能：
 * 1. 加载订单详情
 * 2. 展示订单信息
 * 3. 展示状态流转时间线
 * 4. 快捷确认订单
 */
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getOrder, updateOrderStatus } from '../api'
import { showToast, showSuccessToast } from 'vant'

const route = useRoute()
const router = useRouter()

// 订单数据
const order = ref(null)

/**
 * 加载订单详情
 */
const loadOrder = async () => {
  try {
    const data = await getOrder(route.params.id)
    order.value = data
  } catch (error) {
    console.error('加载订单详情失败:', error)
    showToast('加载失败')
  }
}

/**
 * 返回上一页
 */
const goBack = () => {
  router.back()
}

/**
 * 确认订单
 */
const handleConfirm = async () => {
  try {
    await updateOrderStatus(order.value._id, {
      status: 'confirmed',
      note: '已确认订单'
    })
    showSuccessToast('已确认')
    loadOrder() // 刷新数据
  } catch (error) {
    console.error('确认订单失败:', error)
    showToast('操作失败')
  }
}

/**
 * 获取状态图标
 * @param {string} status - 状态值
 */
const getStatusIcon = (status) => {
  const icons = {
    pending: '⏳',
    confirmed: '✅',
    cooking: '🍳',
    ready: '🍽️',
    completed: '🎉'
  }
  return icons[status] || '❓'
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

// 页面加载时获取数据
onMounted(() => {
  loadOrder()
})
</script>

<style scoped>
.order-detail {
  min-height: 100vh;
  background: #f5f5f5;
  padding-bottom: 80px;
}

.status-section {
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  color: white;
  padding: 30px 20px;
  text-align: center;
}

.status-icon {
  font-size: 48px;
  margin-bottom: 10px;
}

.status-text {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 8px;
}

.order-no {
  font-size: 13px;
  opacity: 0.9;
}

.section {
  background: white;
  margin: 10px;
  padding: 15px;
  border-radius: 12px;
}

.section h3 {
  font-size: 15px;
  color: #333;
  margin-bottom: 12px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #f5f5f5;
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
  padding: 10px 0;
  border-bottom: 1px solid #f5f5f5;
}

.order-item:last-child {
  border-bottom: none;
}

.order-item .name {
  flex: 1;
  font-size: 14px;
  color: #333;
}

.order-item .quantity {
  color: #999;
  margin: 0 15px;
}

.order-item .price {
  color: #ff4757;
  font-weight: bold;
}

.total-row {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px solid #f5f5f5;
  margin-top: 8px;
  font-size: 16px;
}

.total-row .heart {
  font-size: 18px;
}

.total-row .value {
  font-size: 22px;
  font-weight: bold;
  color: #ff4757;
}

.remark {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
}

.note {
  font-size: 12px;
  color: #999;
}

.action-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 15px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
