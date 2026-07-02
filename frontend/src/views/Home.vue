<!--
  首页视图

  展示功能：
  - 顶部搜索栏
  - 分类导航
  - 推荐菜品列表
-->

<template>
  <div class="home">
    <!-- 顶部标题栏 -->
    <div class="header">
      <h1>🍽️ 家庭菜单</h1>
      <p>今天想吃什么？</p>
    </div>

    <!-- 搜索栏 -->
    <van-search
      v-model="searchText"
      placeholder="搜索菜品"
      shape="round"
      @search="handleSearch"
    />

    <!-- 分类导航 -->
    <div class="categories">
      <div
        v-for="cat in categories"
        :key="cat.name"
        class="category-item"
        @click="goToCategory(cat.name)"
      >
        <span class="icon">{{ cat.icon }}</span>
        <span class="name">{{ cat.name }}</span>
      </div>
    </div>

    <!-- 推荐菜品标题 -->
    <div class="section-title">
      <span>🥘 推荐菜品</span>
    </div>

    <!-- 菜品列表 -->
    <div class="recipe-list">
      <RecipeCard
        v-for="recipe in recipes"
        :key="recipe._id"
        :recipe="recipe"
        @click="goToDetail(recipe._id)"
      />
    </div>

    <!-- 加载更多 -->
    <van-loading v-if="loading" type="ball" />
    <van-empty v-if="!loading && recipes.length === 0" description="暂无菜品" />
  </div>
</template>

<script setup>
/**
 * 首页组件逻辑
 *
 * 功能：
 * 1. 加载分类数据
 * 2. 加载推荐菜品
 * 3. 搜索功能
 * 4. 跳转到分类页和详情页
 */
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getRecipes, getCategories } from '../api'
import RecipeCard from '../components/RecipeCard.vue'

const router = useRouter()

// 搜索文本
const searchText = ref('')

// 分类数据
const categories = ref([])

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
  } catch (error) {
    console.error('加载分类失败:', error)
  }
}

/**
 * 加载菜品数据
 * @param {string} search - 搜索关键词
 */
const loadRecipes = async (search = '') => {
  loading.value = true
  try {
    const data = await getRecipes({ search, page_size: 20 })
    recipes.value = data.items
  } catch (error) {
    console.error('加载菜品失败:', error)
  } finally {
    loading.value = false
  }
}

/**
 * 搜索处理
 */
const handleSearch = () => {
  loadRecipes(searchText.value)
}

/**
 * 跳转到分类页
 * @param {string} category - 分类名称
 */
const goToCategory = (category) => {
  router.push({ path: '/category', query: { category } })
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
  loadRecipes()
})
</script>

<style scoped>
.home {
  padding-bottom: 20px;
}

.header {
  background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
  color: white;
  padding: 20px;
  text-align: center;
}

.header h1 {
  font-size: 24px;
  margin-bottom: 5px;
}

.header p {
  font-size: 14px;
  opacity: 0.9;
}

.categories {
  display: flex;
  overflow-x: auto;
  padding: 15px;
  gap: 15px;
  background: white;
}

.category-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 60px;
  cursor: pointer;
}

.category-item .icon {
  font-size: 28px;
  margin-bottom: 5px;
}

.category-item .name {
  font-size: 12px;
  color: #666;
}

.section-title {
  padding: 15px;
  font-size: 16px;
  font-weight: bold;
  color: #333;
}

.recipe-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  padding: 0 10px;
}
</style>
