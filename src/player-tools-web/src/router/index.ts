import AppVue from '../App.vue'
import HomeViewVue from '../views/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: AppVue
    },
    {
      path: '/home',
      name: 'home',
      component: HomeViewVue
    }
  ]
})

export default router
