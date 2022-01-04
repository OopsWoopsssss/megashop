import Vue from 'vue'
import VueRouter from 'vue-router'
import Categories from "../components/category/Categories";
import CategoryBody from "../components/category/CategoryBody";

Vue.use(VueRouter)

const routes = [
  { path: '/Categories', component: Categories },
  { path: '/:nameCategory', component: CategoryBody, props: true },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
