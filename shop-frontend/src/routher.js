import VueRouter from 'vue-router'

import Categories from "./conponents/category/Categories";
import CategoryBody from "./conponents/category/CategoryBody";

const routes = [
    { path: '/Categories', component: Categories },
    { path: '/:nameCategory', component: CategoryBody, props: true },
]

const router = new VueRouter({
  mode: 'history',
  routes,
})
export default router