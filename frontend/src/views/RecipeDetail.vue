<!--
  菜品详情页视图

  展示菜品完整信息：
  - 大图展示
  - 菜品名称和简介
  - 爱心价格
  - 食材列表
  - 制作步骤
  - 加入购物车按钮
-->

<template>
  <div class="recipe-detail" v-if="recipe">
    <!-- 顶部图片 -->
    <div class="image-section">
      <img
        :src="recipe.image || defaultImage"
        :alt="recipe.name"
        class="recipe-image"
        @error="handleImageError"
      />
      <van-nav-bar
        left-arrow
        @click-left="goBack"
        class="nav-bar"
      />
    </div>

    <!-- 菜品信息 -->
    <div class="info-section">
      <div class="header">
        <h1>{{ recipe.name }}</h1>
        <div class="price">
          <span class="heart">❤️</span>
          <span class="value">{{ recipe.price_hearts }}</span>
        </div>
      </div>

      <div class="meta">
        <van-tag type="primary">{{ recipe.category }}</van-tag>
        <van-tag type="success">{{ recipe.difficulty }}</van-tag>
        <van-tag>⏱️ {{ recipe.cook_time }}</van-tag>
      </div>

      <p class="description">{{ recipe.description }}</p>

      <!-- 标签 -->
      <div class="tags" v-if="recipe.tags && recipe.tags.length">
        <van-tag v-for="tag in recipe.tags" :key="tag" plain type="danger">{{ tag }}</van-tag>
      </div>
    </div>

    <!-- 食材列表 -->
    <div class="section">
      <h2>🥬 所需食材</h2>
      <div class="ingredients">
        <div v-for="(item, index) in recipe.ingredients" :key="index" class="ingredient-item">
          {{ item }}
        </div>
      </div>
    </div>

    <!-- 制作步骤 -->
    <div class="section">
      <h2>👩‍🍳 制作步骤</h2>
      <div class="steps">
        <div v-for="step in recipe.steps" :key="step.order" class="step-item">
          <div class="step-number">{{ step.order }}</div>
          <div class="step-desc">{{ step.desc }}</div>
        </div>
      </div>
    </div>

    <!-- 底部操作栏 -->
    <div class="bottom-bar">
      <van-button
        type="primary"
        block
        round
        @click="handleAddToCart"
      >
        ❤️ 加入已点菜品
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
 * 菜品详情页组件逻辑
 *
 * 功能：
 * 1. 根据ID加载菜品详情
 * 2. 展示食材和步骤
 * 3. 加入购物车
 */
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getRecipe } from '../api'
import { addToCart } from '../store/cart'
import { showToast } from 'vant'

const route = useRoute()
const router = useRouter()

// 菜品数据
const recipe = ref(null)

// 默认图片
const defaultImage = 'https://via.placeholder.com/400x300?text=美味菜品'

/**
 * 加载菜品详情
 */
const loadRecipe = async () => {
  try {
    const data = await getRecipe(route.params.id)
    recipe.value = data
  } catch (error) {
    console.error('加载菜品详情失败:', error)
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
 * 图片加载失败处理
 */
const handleImageError = (e) => {
  e.target.src = defaultImage
}

/**
 * 加入购物车
 */
const handleAddToCart = () => {
  addToCart(recipe.value)
  showToast('已加入已点菜品')
}

// 页面加载时获取数据
onMounted(() => {
  loadRecipe()
})
</script>

<style scoped>
.recipe-detail {
  padding-bottom: 70px;
}

.image-section {
  position: relative;
  width: 100%;
  height: 300px;
}

.recipe-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nav-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background: transparent;
}

.info-section {
  padding: 15px;
  background: white;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 10px;
}

.header h1 {
  font-size: 20px;
  color: #333;
  flex: 1;
}

.price {
  display: flex;
  align-items: center;
  gap: 4px;
}

.price .heart {
  font-size: 18px;
}

.price .value {
  font-size: 24px;
  font-weight: bold;
  color: #ff4757;
}

.meta {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}

.description {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.section {
  margin-top: 10px;
  padding: 15px;
  background: white;
}

.section h2 {
  font-size: 16px;
  color: #333;
  margin-bottom: 15px;
}

.ingredients {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ingredient-item {
  background: #f5f5f5;
  padding: 8px 12px;
  border-radius: 20px;
  font-size: 13px;
  color: #666;
}

.steps {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.step-item {
  display: flex;
  gap: 12px;
}

.step-number {
  width: 24px;
  height: 24px;
  background: #ff6b6b;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: bold;
  flex-shrink: 0;
}

.step-desc {
  font-size: 14px;
  color: #333;
  line-height: 1.6;
  padding-top: 2px;
}

.bottom-bar {
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
