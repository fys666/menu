<!--
  菜品卡片组件

  展示单个菜品的缩略信息：
  - 菜品图片
  - 菜名
  - 分类标签
  - 爱心价格
-->

<template>
  <div class="recipe-card" @click="$emit('click')">
    <!-- 菜品图片 -->
    <div class="image-wrapper">
      <img
        :src="recipe.image || defaultImage"
        :alt="recipe.name"
        class="recipe-image"
        @error="handleImageError"
      />
      <div class="difficulty-badge">{{ recipe.difficulty }}</div>
    </div>

    <!-- 菜品信息 -->
    <div class="info">
      <h3 class="name">{{ recipe.name }}</h3>
      <p class="category">{{ recipe.category }} · {{ recipe.cook_time }}</p>
      <div class="price">
        <span class="heart">❤️</span>
        <span class="value">{{ recipe.price_hearts }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
/**
 * 菜品卡片组件
 *
 * Props:
 * - recipe: 菜谱对象
 *
 * Events:
 * - click: 点击卡片时触发
 */
import { ref } from 'vue'

// Props
const props = defineProps({
  recipe: {
    type: Object,
    required: true
  }
})

// Emits
defineEmits(['click'])

// 默认图片（当图片加载失败时使用）
const defaultImage = 'https://via.placeholder.com/400x300?text=美味菜品'

/**
 * 图片加载失败处理
 */
const handleImageError = (e) => {
  e.target.src = defaultImage
}
</script>

<style scoped>
.recipe-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.2s;
}

.recipe-card:active {
  transform: scale(0.98);
}

.image-wrapper {
  position: relative;
  width: 100%;
  padding-top: 75%;
  overflow: hidden;
}

.recipe-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.difficulty-badge {
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
}

.info {
  padding: 10px;
}

.name {
  font-size: 14px;
  font-weight: 600;
  color: #333;
  margin-bottom: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.category {
  font-size: 12px;
  color: #999;
  margin-bottom: 6px;
}

.price {
  display: flex;
  align-items: center;
  gap: 2px;
}

.heart {
  font-size: 14px;
}

.value {
  font-size: 16px;
  font-weight: bold;
  color: #ff4757;
}
</style>
