import { createRouter, createWebHistory } from 'vue-router';

import CategoryBody from "../components/category/CategoryBody";
import mainPage from "../components/mainPage";
import cardProduct from "../components/cards/cardProduct";

const routes = [

    { path: '/Product/:idProducts', component: cardProduct, props: true, },

    { path: '/', component: mainPage },

    { path: '/:nameCategory', component: CategoryBody, props: true },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
