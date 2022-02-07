import { createRouter, createWebHistory } from 'vue-router';

import CategoryBody from "../components/category/CategoryBody";
import mainPage from "../components/mainPage";
import cardProduct from "../components/cards/cardProduct";
import signup from "../components/auth_signup/signup/signup";
import auth from "../components/auth_signup/auth/auth";
import privteOffice from "../components/private_office/private_office";

const routes = [

    { path: '/Product/:idProducts', component: cardProduct, props: true, },

    { path: '/', component: mainPage },

    { path: '/:nameCategory', component: CategoryBody, props: true },

    { path: '/signup', component: signup },

    { path: '/auth', component: auth },

    { path: '/privteOffice', component: privteOffice },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
