<!--
  分类页 - 左侧导航 + 右侧列表

  设计风格：温暖的书架式分类
-->
<template>
  <view class="category-page">
    <!-- 左侧分类导航 -->
    <scroll-view scroll-y class="category-nav">
      <view class="nav-header">
        <text class="nav-title">菜谱分类</text>
      </view>
      <view
        v-for="(cat, index) in categories"
        :key="cat.name"
        class="nav-item"
        :class="{ active: currentCategory === cat.name }"
        :style="{ animationDelay: index * 0.05 + 's' }"
        @tap="selectCategory(cat.name)"
      >
        <view class="nav-icon-wrap" :class="{ active: currentCategory === cat.name }">
          <text class="nav-icon">{{ cat.icon }}</text>
        </view>
        <text class="nav-text">{{ cat.name }}</text>
        <view v-if="currentCategory === cat.name" class="nav-indicator"></view>
      </view>
    </scroll-view>

    <!-- 右侧菜品列表 -->
    <scroll-view scroll-y class="recipe-panel">
      <view class="panel-header">
        <text class="panel-title">{{ currentCategory || '全部' }}</text>
        <text class="panel-count">{{ recipes.length }}道</text>
      </view>

      <view v-if="loading" class="loading-state">
        <text>加载中...</text>
      </view>

      <view v-else class="recipe-list">
        <view
          v-for="(recipe, index) in recipes"
          :key="recipe._id"
          class="recipe-item"
          :style="{ animationDelay: index * 0.06 + 's' }"
          @tap="goToDetail(recipe._id)"
        >
          <view class="item-image-wrap">
            <image
              :src="recipe.image || defaultImage"
              class="item-image"
              mode="aspectFill"
            />
          </view>
          <view class="item-content">
            <text class="item-name">{{ recipe.name }}</text>
            <view class="item-tags">
              <text class="item-tag" :class="'tag-' + recipe.difficulty">
                {{ recipe.difficulty }}
              </text>
              <text class="item-time">⏱️ {{ recipe.cook_time }}</text>
            </view>
            <view class="item-price">
              <text class="price-heart">❤️</text>
              <text class="price-num">{{ recipe.price_hearts }}</text>
            </view>
          </view>
          <view class="item-add" @tap.stop="quickAdd(recipe)">
            <text>+</text>
          </view>
        </view>

        <view v-if="recipes.length === 0 && !loading" class="empty-state">
          <text class="empty-icon">🍽️</text>
          <text class="empty-text">该分类暂无菜品</text>
        </view>
      </view>
    </scroll-view>
  </view>
</template>

<script>
import { getRecipes, getCategories } from '../../api/index.js'
import { addToCart } from '../../store/cart.js'

export default {
  data() {
    return {
      categories: [],
      currentCategory: '',
      recipes: [],
      loading: false,
      defaultImage: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400'
    }
  },
  onLoad() {
    this.loadCategories()
  },
  onShow() {
    const selectedCategory = getApp().globalData.selectedCategory
    if (selectedCategory) {
      this.currentCategory = selectedCategory
      getApp().globalData.selectedCategory = null
    }
  },
  methods: {
    async loadCategories() {
      try {
        this.categories = await getCategories()
        if (!this.currentCategory && this.categories.length > 0) {
          this.currentCategory = this.categories[0].name
          this.loadRecipes(this.currentCategory)
        }
      } catch (e) {
        console.error('加载分类失败:', e)
      }
    },
    async loadRecipes(category) {
      this.loading = true
      try {
        const data = await getRecipes({ category, page_size: 50 })
        this.recipes = data.items
      } catch (e) {
        console.error('加载菜品失败:', e)
      } finally {
        this.loading = false
      }
    },
    selectCategory(name) {
      this.currentCategory = name
      this.loadRecipes(name)
    },
    goToDetail(id) {
      uni.navigateTo({ url: `/pages/recipe/index?id=${id}` })
    },
    quickAdd(recipe) {
      addToCart(recipe)
      uni.showToast({ title: '已加入', icon: 'success' })
    }
  }
}
</script>

<style scoped>
.category-page {
  display: flex;
  height: 100vh;
  background: var(--color-bg);
}

/* ==================== 左侧导航 ==================== */
.category-nav {
  width: 180rpx;
  background: var(--color-card);
  box-shadow: 4rpx 0 24rpx rgba(0,0,0,0.04);
  position: relative;
  z-index: 2;
}

.nav-header {
  padding: 30rpx 20rpx 20rpx;
}

.nav-title {
  font-size: 24rpx;
  color: var(--color-text-secondary);
  font-weight: 600;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 24rpx 16rpx;
  position: relative;
  animation: fadeInUp 0.3s ease-out forwards;
  opacity: 0;
}

.nav-icon-wrap {
  width: 80rpx;
  height: 80rpx;
  border-radius: 24rpx;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg);
  transition: all 0.3s ease;
  margin-bottom: 10rpx;
}

.nav-icon-wrap.active {
  background: var(--color-primary);
  box-shadow: 0 6rpx 20rpx rgba(232, 115, 74, 0.3);
  transform: scale(1.1);
}

.nav-icon {
  font-size: 40rpx;
}

.nav-text {
  font-size: 24rpx;
  color: var(--color-text-secondary);
  font-weight: 500;
}

.nav-item.active .nav-text {
  color: var(--color-primary);
  font-weight: 600;
}

.nav-indicator {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 6rpx;
  height: 40rpx;
  background: var(--color-primary);
  border-radius: 3rpx 0 0 3rpx;
}

/* ==================== 右侧列表 ==================== */
.recipe-panel {
  flex: 1;
  padding: 24rpx;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20rpx;
}

.panel-title {
  font-size: 36rpx;
  font-weight: 700;
  color: var(--color-text);
}

.panel-count {
  font-size: 24rpx;
  color: var(--color-text-secondary);
  background: var(--color-border);
  padding: 8rpx 16rpx;
  border-radius: 20rpx;
}

/* ==================== 菜品列表 ==================== */
.recipe-list {
  display: flex;
  flex-direction: column;
  gap: 20rpx;
}

.recipe-item {
  display: flex;
  align-items: center;
  gap: 20rpx;
  background: var(--color-card);
  border-radius: 20rpx;
  padding: 20rpx;
  box-shadow: 0 4rpx 16rpx rgba(0,0,0,0.04);
  animation: fadeInUp 0.4s ease-out forwards;
  opacity: 0;
}

.recipe-item:active {
  transform: scale(0.98);
}

.item-image-wrap {
  width: 160rpx;
  height: 160rpx;
  border-radius: 16rpx;
  overflow: hidden;
  flex-shrink: 0;
}

.item-image {
  width: 100%;
  height: 100%;
}

.item-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10rpx;
}

.item-name {
  font-size: 30rpx;
  font-weight: 600;
  color: var(--color-text);
}

.item-tags {
  display: flex;
  align-items: center;
  gap: 12rpx;
}

.item-tag {
  font-size: 20rpx;
  padding: 4rpx 12rpx;
  border-radius: 8rpx;
  font-weight: 500;
}

.tag-简单 {
  background: rgba(82, 183, 136, 0.15);
  color: var(--color-success);
}

.tag-中等 {
  background: rgba(244, 162, 97, 0.15);
  color: var(--color-primary);
}

.tag-困难 {
  background: rgba(230, 57, 70, 0.15);
  color: var(--color-heart);
}

.item-time {
  font-size: 22rpx;
  color: var(--color-text-secondary);
}

.item-price {
  display: flex;
  align-items: center;
  gap: 6rpx;
}

.price-heart {
  font-size: 24rpx;
}

.price-num {
  font-size: 32rpx;
  font-weight: 700;
  color: var(--color-heart);
}

.item-add {
  width: 60rpx;
  height: 60rpx;
  background: var(--color-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 4rpx 16rpx rgba(232, 115, 74, 0.3);
}

.item-add text {
  color: white;
  font-size: 40rpx;
  font-weight: 300;
  line-height: 1;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100rpx 0;
}

.empty-icon {
  font-size: 80rpx;
  margin-bottom: 16rpx;
}

.empty-text {
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
