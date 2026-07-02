<!--
  应用根组件

  提供全局布局结构：
  - 顶部导航栏
  - 主内容区域（路由视图）
  - 底部 TabBar 导航
-->

<template>
  <div class="app">
    <!-- 主内容区域 -->
    <router-view />

    <!-- 底部 TabBar -->
    <van-tabbar v-if="showTabbar" v-model="activeTab" route>
      <van-tabbar-item icon="home-o" to="/">首页</van-tabbar-item>
      <van-tabbar-item icon="apps-o" to="/category">分类</van-tabbar-item>
      <van-tabbar-item icon="cart-o" :badge="cartCount || ''" to="/cart">已点</van-tabbar-item>
      <van-tabbar-item icon="orders-o" to="/orders">订单</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script setup>
/**
 * 根组件逻辑
 *
 * 控制 TabBar 显示和购物车角标
 */
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useCart } from './store/cart'

const route = useRoute()
const { getCartCount } = useCart()

// 当前激活的 Tab
const activeTab = ref(0)

// 是否显示 TabBar
const showTabbar = computed(() => route.meta.showTabbar !== false)

// 购物车数量
const cartCount = computed(() => getCartCount())
</script>

<style>
/* 全局样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f7f8fa;
}

.app {
  min-height: 100vh;
  padding-bottom: 50px;
}

/* 自定义样式变量 */
:root {
  --primary-color: #ff6b6b;
  --heart-color: #ff4757;
}
</style>
