import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index';
import BootstrapVue3 from 'bootstrap-vue-3'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import './style/style.scss';

const app = createApp(App)
app.use(BootstrapVue3)
app.use(router)
app.use(store)
app.mount('#app')
