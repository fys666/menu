<!--
  首页 - 温馨厨房风格

  设计理念：温暖的家宴氛围，琥珀色调，圆润卡片
-->
<template>
  <view class="home">
    <!-- 顶部 Hero 区域 -->
    <view class="hero">
      <view class="hero-bg"></view>
      <view class="hero-content">
        <view class="greeting">
          <text class="wave">👨‍🍳</text>
          <text class="title">今晚想吃什么？</text>
        </view>
        <text class="subtitle">为家人准备一顿温馨的晚餐</text>
      </view>
      <!-- 装饰元素 -->
      <view class="decoration deco-1"></view>
      <view class="decoration deco-2"></view>
    </view>

    <!-- 搜索栏 -->
    <view class="search-container">
      <view class="search-bar">
        <text class="search-icon">🔍</text>
        <input
          class="search-input"
          placeholder="搜索你想吃的..."
          placeholder-class="search-placeholder"
          v-model="searchText"
          @confirm="handleSearch"
        />
      </view>
    </view>

    <!-- 分类导航 - 胶囊风格 -->
    <view class="category-section">
      <scroll-view scroll-x class="category-scroll" :show-scrollbar="false">
        <view class="category-list">
          <view
            v-for="(cat, index) in categories"
            :key="cat.name"
            class="category-pill"
            :class="{ active: currentCategory === cat.name }"
            :style="{ animationDelay: index * 0.05 + 's' }"
            @tap="selectCategory(cat.name)"
          >
            <text class="pill-icon">{{ cat.icon }}</text>
            <text class="pill-text">{{ cat.name }}</text>
          </view>
        </view>
      </scroll-view>
    </view>

    <!-- 推荐菜品 -->
    <view class="section">
      <view class="section-header">
        <view class="section-title-group">
          <text class="section-emoji">✨</text>
          <text class="section-title">今日推荐</text>
        </view>
        <text class="section-count">{{ recipes.length }}道菜</text>
      </view>

      <!-- 菜品网格 -->
      <view class="recipe-grid">
        <view
          v-for="(recipe, index) in recipes"
          :key="recipe._id"
          class="recipe-card"
          :style="{ animationDelay: index * 0.08 + 's' }"
          @tap="goToDetail(recipe._id)"
        >
          <!-- 图片容器 -->
          <view class="card-image-wrap">
            <image
              :src="recipe.image || defaultImage"
              class="card-image"
              mode="aspectFill"
            />
            <!-- 难度标签 -->
            <view class="difficulty-badge" :class="'diff-' + recipe.difficulty">
              <text>{{ recipe.difficulty }}</text>
            </view>
          </view>

          <!-- 卡片内容 -->
          <view class="card-content">
            <text class="card-name">{{ recipe.name }}</text>
            <view class="card-meta">
              <text class="meta-item">⏱️ {{ recipe.cook_time }}</text>
              <text class="meta-dot">·</text>
              <text class="meta-item">{{ recipe.category }}</text>
            </view>
            <view class="card-footer">
              <view class="price-tag">
                <text class="price-heart">❤️</text>
                <text class="price-value">{{ recipe.price_hearts }}</text>
              </view>
              <view class="add-btn" @tap.stop="quickAdd(recipe)">
                <text class="add-icon">+</text>
              </view>
            </view>
          </view>
        </view>
      </view>

      <!-- 空状态 -->
      <view v-if="!loading && recipes.length === 0" class="empty-state">
        <text class="empty-icon">🍳</text>
        <text class="empty-text">暂无菜品</text>
      </view>

      <!-- 加载状态 -->
      <view v-if="loading" class="loading-state">
        <text class="loading-text">正在准备菜单...</text>
      </view>
    </view>
  </view>
</template>

<script>
import { getRecipes, getCategories } from '../../api/index.js'
import { addToCart } from '../../store/cart.js'

export default {
  data() {
    return {
      searchText: '',
      currentCategory: '',
      categories: [],
      recipes: [],
      loading: false,
      defaultImage: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400'
    }
  },
  onLoad() {
    this.loadCategories()
    this.loadRecipes()
  },
  methods: {
    async loadCategories() {
      try {
        this.categories = await getCategories()
      } catch (e) {
        console.error('加载分类失败:', e)
      }
    },
    async loadRecipes(category = '') {
      this.loading = true
      try {
        const params = { page_size: 20 }
        if (category) params.category = category
        if (this.searchText) params.search = this.searchText
        const data = await getRecipes(params)
        this.recipes = data.items
      } catch (e) {
        console.error('加载菜品失败:', e)
      } finally {
        this.loading = false
      }
    },
    selectCategory(name) {
      this.currentCategory = this.currentCategory === name ? '' : name
      this.loadRecipes(this.currentCategory)
    },
    handleSearch() {
      this.loadRecipes(this.currentCategory)
    },
    goToDetail(id) {
      uni.navigateTo({ url: `/pages/recipe/index?id=${id}` })
    },
    quickAdd(recipe) {
      addToCart(recipe)
      uni.showToast({
        title: '已加入',
        icon: 'success',
        duration: 1000
      })
    }
  }
}
</script>

<style scoped>
/* ==================== Hero 区域 ==================== */
.hero {
  position: relative;
  height: 380rpx;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(145deg, #E8734A 0%, #F4A261 50%, #E9C46A 100%);
}

.hero-bg::after {
  content: '';
  position: absolute;
  bottom: -2rpx;
  left: 0; right: 0;
  height: 60rpx;
  background: var(--color-bg);
  border-radius: 40rpx 40rpx 0 0;
}

.hero-content {
  position: relative;
  z-index: 2;
  padding: 100rpx 40rpx 60rpx;
}

.greeting {
  display: flex;
  align-items: center;
  gap: 16rpx;
  margin-bottom: 12rpx;
}

.wave {
  font-size: 56rpx;
}

.title {
  font-size: 48rpx;
  font-weight: 700;
  color: white;
  text-shadow: 0 4rpx 12rpx rgba(0,0,0,0.15);
}

.subtitle {
  font-size: 28rpx;
  color: rgba(255,255,255,0.9);
  padding-left: 72rpx;
}

/* 装饰圆点 */
.decoration {
  position: absolute;
  border-radius: 50%;
  opacity: 0.3;
}

.deco-1 {
  width: 200rpx; height: 200rpx;
  background: white;
  top: 40rpx; right: -40rpx;
}

.deco-2 {
  width: 120rpx; height: 120rpx;
  background: var(--color-accent);
  bottom: 80rpx; right: 60rpx;
}

/* ==================== 搜索栏 ==================== */
.search-container {
  padding: 0 30rpx;
  margin-top: -20rpx;
  position: relative;
  z-index: 10;
}

.search-bar {
  display: flex;
  align-items: center;
  background: var(--color-card);
  border-radius: 48rpx;
  padding: 20rpx 28rpx;
  box-shadow: 0 8rpx 32rpx rgba(232, 115, 74, 0.12);
}

.search-icon {
  font-size: 32rpx;
  margin-right: 16rpx;
}

.search-input {
  flex: 1;
  font-size: 28rpx;
  color: var(--color-text);
}

.search-placeholder {
  color: var(--color-text-secondary);
}

/* ==================== 分类导航 ==================== */
.category-section {
  margin-top: 30rpx;
}

.category-scroll {
  white-space: nowrap;
}

.category-list {
  display: inline-flex;
  gap: 16rpx;
  padding: 10rpx 30rpx;
}

.category-pill {
  display: inline-flex;
  align-items: center;
  gap: 8rpx;
  padding: 16rpx 28rpx;
  background: var(--color-card);
  border-radius: 40rpx;
  box-shadow: 0 4rpx 16rpx rgba(0,0,0,0.04);
  animation: fadeInUp 0.4s ease-out forwards;
  opacity: 0;
}

.category-pill.active {
  background: var(--color-primary);
  box-shadow: 0 6rpx 24rpx rgba(232, 115, 74, 0.35);
}

.pill-icon {
  font-size: 32rpx;
}

.pill-text {
  font-size: 26rpx;
  color: var(--color-text);
  font-weight: 500;
}

.category-pill.active .pill-text {
  color: white;
}

/* ==================== 菜品区域 ==================== */
.section {
  padding: 30rpx;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24rpx;
}

.section-title-group {
  display: flex;
  align-items: center;
  gap: 10rpx;
}

.section-emoji {
  font-size: 36rpx;
}

.section-title {
  font-size: 34rpx;
  font-weight: 700;
  color: var(--color-text);
}

.section-count {
  font-size: 24rpx;
  color: var(--color-text-secondary);
  background: var(--color-border);
  padding: 8rpx 16rpx;
  border-radius: 20rpx;
}

/* ==================== 菜品卡片 ==================== */
.recipe-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20rpx;
}

.recipe-card {
  background: var(--color-card);
  border-radius: 24rpx;
  overflow: hidden;
  box-shadow: 0 8rpx 32rpx rgba(44, 24, 16, 0.06);
  animation: fadeInUp 0.5s ease-out forwards;
  opacity: 0;
  transition: transform 0.2s ease;
}

.recipe-card:active {
  transform: scale(0.97);
}

.card-image-wrap {
  position: relative;
  width: 100%;
  height: 240rpx;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 100%;
}

.difficulty-badge {
  position: absolute;
  top: 16rpx;
  right: 16rpx;
  padding: 6rpx 16rpx;
  border-radius: 20rpx;
  font-size: 20rpx;
  font-weight: 600;
  backdrop-filter: blur(10px);
}

.diff-简单 {
  background: rgba(82, 183, 136, 0.9);
  color: white;
}

.diff-中等 {
  background: rgba(244, 162, 97, 0.9);
  color: white;
}

.diff-困难 {
  background: rgba(230, 57, 70, 0.9);
  color: white;
}

.card-content {
  padding: 20rpx;
}

.card-name {
  font-size: 28rpx;
  font-weight: 600;
  color: var(--color-text);
  display: block;
  margin-bottom: 8rpx;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.card-meta {
  display: flex;
  align-items: center;
  gap: 8rpx;
  margin-bottom: 16rpx;
}

.meta-item {
  font-size: 22rpx;
  color: var(--color-text-secondary);
}

.meta-dot {
  color: var(--color-border);
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price-tag {
  display: flex;
  align-items: center;
  gap: 6rpx;
}

.price-heart {
  font-size: 26rpx;
}

.price-value {
  font-size: 32rpx;
  font-weight: 700;
  color: var(--color-heart);
}

.add-btn {
  width: 52rpx;
  height: 52rpx;
  background: var(--color-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4rpx 16rpx rgba(232, 115, 74, 0.3);
}

.add-icon {
  color: white;
  font-size: 36rpx;
  font-weight: 300;
  line-height: 1;
}

/* ==================== 状态 ==================== */
.empty-state, .loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 120rpx 0;
}

.empty-icon {
  font-size: 96rpx;
  margin-bottom: 20rpx;
}

.empty-text, .loading-text {
  font-size: 28rpx;
  color: var(--color-text-secondary);
}
</style>
