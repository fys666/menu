<!--
  分类页视图

  按分类浏览所有菜品：
  - 左侧分类导航
  - 右侧菜品列表
-->

<template>
  <div class="category-page">
    <!-- 分类导航 -->
    <div class="category-nav">
      <div
        v-for="cat in categories"
        :key="cat.name"
        class="nav-item"
        :class="{ active: currentCategory === cat.name }"
        @click="selectCategory(cat.name)"
      >
        <span class="icon">{{ cat.icon }}</span>
        <span class="name">{{ cat.name }}</span>
      </div>
    </div>

    <!-- 菜品列表 -->
    <div class="recipe-list">
      <div v-if="loading" class="loading">
        <van-loading type="ball" />
      </div>
      <template v-else>
        <RecipeCard
          v-for="recipe in recipes"
          :key="recipe._id"
          :recipe="recipe"
          @click="goToDetail(recipe._id)"
        />
        <van-empty v-if="recipes.length === 0" description="该分类暂无菜品" />
      </template>
    </div>
  </div>
</template>

<script setup>
/**
 * 分类页组件逻辑
 *
 * 功能：
 * 1. 加载所有分类
 * 2. 根据选中分类筛选菜品
 * 3. 支持从首页带入分类参数
 */
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getRecipes, getCategories } from '../api'
import RecipeCard from '../components/RecipeCard.vue'

const route = useRoute()
const router = useRouter()

// 分类数据
const categories = ref([])

// 当前选中的分类
const currentCategory = ref('')

// 菜品数据
const recipes = ref([])

// 加载状态
const loading = ref(false)

/**
 * 加载分类数据
 */
const loadCategories = async () => {
  try {
    const data = await getCategories()
    categories.value = data

    // 如果URL中有分类参数，选中对应分类
    if (route.query.category) {
      currentCategory.value = route.query.category
    } else if (data.length > 0) {
      currentCategory.value = data[0].name
    }
  } catch (error) {
    console.error('加载分类失败:', error)
  }
}

/**
 * 加载菜品数据
 * @param {string} category - 分类名称
 */
const loadRecipes = async (category = '') => {
  loading.value = true
  try {
    const data = await getRecipes({ category, page_size: 50 })
    recipes.value = data.items
  } catch (error) {
    console.error('加载菜品失败:', error)
  } finally {
    loading.value = false
  }
}

/**
 * 选择分类
 * @param {string} category - 分类名称
 */
const selectCategory = (category) => {
  currentCategory.value = category
  loadRecipes(category)
}

/**
 * 跳转到菜品详情页
 * @param {string} id - 菜品ID
 */
const goToDetail = (id) => {
  router.push(`/recipe/${id}`)
}

// 页面加载时获取数据
onMounted(() => {
  loadCategories()
})

// 监听分类变化
watch(currentCategory, (newCategory) => {
  if (newCategory) {
    loadRecipes(newCategory)
  }
})
</script>

<style scoped>
.category-page {
  display: flex;
  height: calc(100vh - 50px);
}

.category-nav {
  width: 80px;
  background: #f5f5f5;
  overflow-y: auto;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px 10px;
  cursor: pointer;
  border-left: 3px solid transparent;
}

.nav-item.active {
  background: white;
  border-left-color: #ff6b6b;
}

.nav-item .icon {
  font-size: 24px;
  margin-bottom: 5px;
}

.nav-item .name {
  font-size: 12px;
  color: #666;
}

.nav-item.active .name {
  color: #ff6b6b;
  font-weight: 600;
}

.recipe-list {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  align-content: start;
}

.loading {
  grid-column: span 2;
  display: flex;
  justify-content: center;
  padding: 40px;
}
</style>
