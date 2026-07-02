<!--
  应用根组件

  微信小程序生命周期管理
  - 启动时自动登录获取用户信息
-->
<script>
import { wxLogin } from './api/index.js'

export default {
  globalData: {
    userInfo: null,
    openid: null
  },
  onLaunch() {
    console.log('家庭菜单小程序启动')
    this.autoLogin()
  },
  onShow() {},
  onHide() {},
  methods: {
    autoLogin() {
      const cachedUser = uni.getStorageSync('user_info')
      if (cachedUser) {
        this.globalData.userInfo = cachedUser
        this.globalData.openid = cachedUser.openid
        return
      }

      uni.login({
        provider: 'weixin',
        success: async (loginRes) => {
          if (loginRes.code) {
            const openid = `wx_${loginRes.code}_${Date.now()}`
            try {
              const user = await wxLogin({
                openid: openid,
                nickname: '微信用户',
                avatar: ''
              })
              this.globalData.userInfo = user
              this.globalData.openid = user.openid
              uni.setStorageSync('user_info', user)
            } catch (e) {
              console.error('登录失败:', e)
            }
          }
        },
        fail: (err) => {
          console.error('微信登录失败:', err)
        }
      })
    }
  }
}
</script>

<style>
/* ==================== 全局设计系统 ==================== */
page {
  --color-primary: #E8734A;
  --color-primary-light: #F4A261;
  --color-primary-dark: #C45A35;
  --color-secondary: #2D6A4F;
  --color-accent: #E9C46A;
  --color-bg: #FDF8F3;
  --color-card: #FFFFFF;
  --color-text: #2C1810;
  --color-text-secondary: #8B7355;
  --color-border: #F0E6D8;
  --color-heart: #E63946;
  --color-success: #52B788;
  --color-warning: #F4A261;

  background-color: var(--color-bg);
  font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  color: var(--color-text);
  -webkit-font-smoothing: antialiased;
}

/* 全局动画 */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30rpx);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.fade-in-up {
  animation: fadeInUp 0.5s ease-out forwards;
}

.scale-in {
  animation: scaleIn 0.4s ease-out forwards;
}

/* 骨架屏 */
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8rpx;
}
</style>
