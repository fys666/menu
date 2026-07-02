/**
 * 家庭菜单小程序 - 前端入口
 *
 * 初始化 Vue 应用，配置路由和 Vant UI 组件库
 */

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Vant UI 组件库
import Vant from 'vant'
import 'vant/lib/index.css'

// 创建 Vue 应用
const app = createApp(App)

// 使用插件
app.use(router)
app.use(Vant)

// 挂载应用
app.mount('#app')
