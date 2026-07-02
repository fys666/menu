<!--
  菜品详情页 - 沉浸式展示

  设计理念：大图沉浸 + 卡片式内容
-->
<template>
  <view class="recipe-detail" v-if="recipe">
    <!-- 顶部大图 -->
    <view class="hero-section">
      <image
        :src="recipe.image || defaultImage"
        class="hero-image"
        mode="aspectFill"
      />
      <view class="hero-overlay"></view>
      <view class="hero-content">
        <view class="hero-badge">
          <text class="badge-text">{{ recipe.category }}</text>
        </view>
        <text class="hero-name">{{ recipe.name }}</text>
        <text class="hero-desc">{{ recipe.description }}</text>
      </view>
    </view>

    <!-- 信息卡片 -->
    <view class="info-card">
      <!-- 价格 -->
      <view class="price-section">
        <text class="price-heart">❤️</text>
        <text class="price-value">{{ recipe.price_hearts }}</text>
        <text class="price-label">爱心值</text>
      </view>

      <!-- 属性标签 -->
      <view class="attr-row">
        <view class="attr-item">
          <text class="attr-icon">⏱️</text>
          <text class="attr-text">{{ recipe.cook_time }}</text>
        </view>
        <view class="attr-divider"></view>
        <view class="attr-item">
          <text class="attr-icon">📊</text>
          <text class="attr-text">{{ recipe.difficulty }}</text>
        </view>
        <view class="attr-divider"></view>
        <view class="attr-item">
          <text class="attr-icon">🏷️</text>
          <text class="attr-text">{{ recipe.subcategory }}</text>
        </view>
      </view>

      <!-- 标签 -->
      <view class="tags-row" v-if="recipe.tags && recipe.tags.length">
        <view v-for="tag in recipe.tags" :key="tag" class="tag-chip">
          <text>{{ tag }}</text>
        </view>
      </view>
    </view>

    <!-- 食材清单 -->
    <view class="content-card">
      <view class="card-header">
        <text class="card-icon">🥬</text>
        <text class="card-title">食材清单</text>
        <text class="card-count">{{ recipe.ingredients.length }}种</text>
      </view>
      <view class="ingredients-grid">
        <view v-for="(item, index) in recipe.ingredients" :key="index" class="ingredient-pill">
          <text>{{ item }}</text>
        </view>
      </view>
    </view>

    <!-- 制作步骤 -->
    <view class="content-card">
      <view class="card-header">
        <text class="card-icon">👩‍🍳</text>
        <text class="card-title">制作步骤</text>
        <text class="card-count">{{ recipe.steps.length }}步</text>
      </view>
      <view class="steps-list">
        <view v-for="step in recipe.steps" :key="step.order" class="step-item">
          <view class="step-number">
            <text>{{ step.order }}</text>
          </view>
          <view class="step-content">
            <text class="step-text">{{ step.desc }}</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 底部操作栏 -->
    <view class="bottom-bar">
      <view class="btn-add" @tap="handleAddToCart">
        <text class="btn-icon">❤️</text>
        <text class="btn-text">加入已点菜品</text>
      </view>
    </view>
  </view>

  <view v-else class="loading-state">
    <text class="loading-text">加载中...</text>
  </view>
</template>

<script>
import { getRecipe } from '../../api/index.js'
import { addToCart } from '../../store/cart.js'

export default {
  data() {
    return {
      recipe: null,
      defaultImage: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400'
    }
  },
  onLoad(options) {
    if (options.id) {
      this.loadRecipe(options.id)
    }
  },
  methods: {
    async loadRecipe(id) {
      try {
        this.recipe = await getRecipe(id)
      } catch (e) {
        console.error('加载失败:', e)
        uni.showToast({ title: '加载失败', icon: 'none' })
      }
    },
    handleAddToCart() {
      addToCart(this.recipe)
      uni.showToast({ title: '已加入已点菜品', icon: 'success' })
    }
  }
}
</script>

<style scoped>
.recipe-detail {
  padding-bottom: 160rpx;
  background: var(--color-bg);
}

/* ==================== Hero 区域 ==================== */
.hero-section {
  position: relative;
  height: 520rpx;
}

.hero-image {
  width: 100%;
  height: 100%;
}

.hero-overlay {
  position: absolute;
  bottom: 0;
  left: 0; right: 0;
  height: 300rpx;
  background: linear-gradient(to top, rgba(44, 24, 16, 0.85), transparent);
}

.hero-content {
  position: absolute;
  bottom: 40rpx;
  left: 30rpx;
  right: 30rpx;
}

.hero-badge {
  display: inline-block;
  background: var(--color-primary);
  padding: 8rpx 20rpx;
  border-radius: 20rpx;
  margin-bottom: 16rpx;
}

.badge-text {
  font-size: 22rpx;
  color: white;
  font-weight: 600;
}

.hero-name {
  font-size: 48rpx;
  font-weight: 700;
  color: white;
  display: block;
  margin-bottom: 10rpx;
  text-shadow: 0 4rpx 16rpx rgba(0,0,0,0.3);
}

.hero-desc {
  font-size: 26rpx;
  color: rgba(255,255,255,0.85);
}

/* ==================== 信息卡片 ==================== */
.info-card {
  background: var(--color-card);
  margin: 20rpx 24rpx;
  padding: 32rpx;
  border-radius: 24rpx;
  box-shadow: 0 8rpx 32rpx rgba(0,0,0,0.06);
}

.price-section {
  display: flex;
  align-items: baseline;
  gap: 8rpx;
  margin-bottom: 24rpx;
  padding-bottom: 24rpx;
  border-bottom: 2rpx solid var(--color-border);
}

.price-heart {
  font-size: 40rpx;
}

.price-value {
  font-size: 56rpx;
  font-weight: 700;
  color: var(--color-heart);
}

.price-label {
  font-size: 24rpx;
  color: var(--color-text-secondary);
  margin-left: 8rpx;
}

.attr-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 24rpx;
}

.attr-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8rpx;
}

.attr-icon {
  font-size: 36rpx;
}

.attr-text {
  font-size: 24rpx;
  color: var(--color-text-secondary);
}

.attr-divider {
  width: 2rpx;
  height: 48rpx;
  background: var(--color-border);
}

.tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12rpx;
}

.tag-chip {
  background: var(--color-bg);
  padding: 10rpx 20rpx;
  border-radius: 24rpx;
}

.tag-chip text {
  font-size: 24rpx;
  color: var(--color-primary);
}

/* ==================== 内容卡片 ==================== */
.content-card {
  background: var(--color-card);
  margin: 20rpx 24rpx;
  padding: 32rpx;
  border-radius: 24rpx;
  box-shadow: 0 8rpx 32rpx rgba(0,0,0,0.06);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12rpx;
  margin-bottom: 24rpx;
}

.card-icon {
  font-size: 36rpx;
}

.card-title {
  font-size: 32rpx;
  font-weight: 700;
  color: var(--color-text);
  flex: 1;
}

.card-count {
  font-size: 22rpx;
  color: var(--color-text-secondary);
  background: var(--color-bg);
  padding: 6rpx 14rpx;
  border-radius: 16rpx;
}

/* 食材网格 */
.ingredients-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16rpx;
}

.ingredient-pill {
  background: var(--color-bg);
  padding: 14rpx 24rpx;
  border-radius: 32rpx;
  border: 2rpx solid var(--color-border);
}

.ingredient-pill text {
  font-size: 26rpx;
  color: var(--color-text);
}

/* 步骤列表 */
.steps-list {
  display: flex;
  flex-direction: column;
  gap: 24rpx;
}

.step-item {
  display: flex;
  gap: 20rpx;
}

.step-number {
  width: 52rpx;
  height: 52rpx;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.step-number text {
  color: white;
  font-size: 26rpx;
  font-weight: 700;
}

.step-content {
  flex: 1;
  padding-top: 10rpx;
}

.step-text {
  font-size: 28rpx;
  color: var(--color-text);
  line-height: 1.7;
}

/* ==================== 底部栏 ==================== */
.bottom-bar {
  position: fixed;
  bottom: 0;
  left: 0; right: 0;
  padding: 24rpx 32rpx;
  padding-bottom: calc(24rpx + env(safe-area-inset-bottom));
  background: var(--color-card);
  box-shadow: 0 -8rpx 32rpx rgba(0,0,0,0.08);
}

.btn-add {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12rpx;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  padding: 28rpx;
  border-radius: 56rpx;
  box-shadow: 0 8rpx 32rpx rgba(232, 115, 74, 0.35);
}

.btn-add:active {
  transform: scale(0.98);
}

.btn-icon {
  font-size: 36rpx;
}

.btn-text {
  font-size: 32rpx;
  font-weight: 600;
  color: white;
}

.loading-state {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: var(--color-text-secondary);
}
</style>
