import { createRouter, createWebHistory } from 'vue-router';

import Categories from "../components/category/Categories";
import CategoryBody from "../components/category/CategoryBody";

const routes = [
  { path: '/Categories', component: Categories },
  { path: '/:nameCategory', component: CategoryBody, props: true },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
