<!--
  提交订单页视图

  填写订单信息：
  - 点菜人姓名
  - 已选菜品列表
  - 总爱心数
  - 备注信息
  - 提交按钮
-->

<template>
  <div class="order-submit">
    <!-- 顶部导航 -->
    <van-nav-bar title="提交订单" left-arrow @click-left="goBack" />

    <!-- 点菜人 -->
    <div class="section">
      <h3>👤 点菜人</h3>
      <van-field
        v-model="customerName"
        placeholder="请输入点菜人姓名"
        :rules="[{ required: true, message: '请输入点菜人姓名' }]"
      />
    </div>

    <!-- 已选菜品 -->
    <div class="section">
      <h3>🍽️ 已选菜品</h3>
      <div v-for="item in cartItems" :key="item.id" class="order-item">
        <span class="name">{{ item.name }} x{{ item.quantity }}</span>
        <span class="price">❤️ {{ item.price_hearts * item.quantity }}</span>
      </div>
    </div>

    <!-- 总计 -->
    <div class="section total">
      <span>合计：</span>
      <span class="heart">❤️</span>
      <span class="value">{{ totalHearts }}</span>
    </div>

    <!-- 备注 -->
    <div class="section">
      <h3>📝 备注</h3>
      <van-field
        v-model="remark"
        type="textarea"
        placeholder="有什么特殊要求吗？（选填）"
        rows="2"
        maxlength="200"
        show-word-limit
      />
    </div>

    <!-- 提交按钮 -->
    <div class="submit-bar">
      <van-button
        type="primary"
        block
        round
        :loading="submitting"
        @click="handleSubmit"
      >
        确认提交订单
      </van-button>
    </div>
  </div>
</template>

<script setup>
/**
 * 提交订单页组件逻辑
 *
 * 功能：
 * 1. 展示已选菜品
 * 2. 填写点菜人信息
 * 3. 提交订单到后端
 * 4. 跳转到订单详情页
 */
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCart } from '../store/cart'
import { createOrder } from '../api'
import { showToast, showSuccessToast } from 'vant'

const router = useRouter()
const { state, clearCart, getTotalHearts } = useCart()

// 点菜人姓名
const customerName = ref('')

// 备注
const remark = ref('')

// 提交状态
const submitting = ref(false)

// 购物车项
const cartItems = computed(() => state.items)

// 总爱心数
const totalHearts = computed(() => getTotalHearts())

/**
 * 返回上一页
 */
const goBack = () => {
  router.back()
}

/**
 * 提交订单
 */
const handleSubmit = async () => {
  // 验证
  if (!customerName.value.trim()) {
    showToast('请输入点菜人姓名')
    return
  }

  if (cartItems.value.length === 0) {
    showToast('请选择菜品')
    return
  }

  submitting.value = true

  try {
    // 构建订单数据
    const orderData = {
      customer_name: customerName.value.trim(),
      items: cartItems.value.map(item => ({
        recipe_id: item.id,
        name: item.name,
        quantity: item.quantity,
        price_hearts: item.price_hearts
      })),
      remark: remark.value.trim()
    }

    // 提交订单
    const result = await createOrder(orderData)

    // 清空购物车
    clearCart()

    // 提示成功
    showSuccessToast('下单成功')

    // 跳转到订单详情页
    router.replace(`/order/${result._id}`)
  } catch (error) {
    console.error('提交订单失败:', error)
    showToast('提交失败，请重试')
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.order-submit {
  min-height: 100vh;
  padding-bottom: 80px;
  background: #f5f5f5;
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
  margin-bottom: 10px;
}

.order-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #f5f5f5;
}

.order-item:last-child {
  border-bottom: none;
}

.order-item .name {
  font-size: 14px;
  color: #333;
}

.order-item .price {
  color: #ff4757;
  font-weight: bold;
}

.total {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 8px;
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

.submit-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 15px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}
</style>
