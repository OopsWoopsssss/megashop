import {createStore} from 'vuex'
import category from "./category/category";
import products from "./products/products";

export default createStore({
  modules: {
    category,
    products,
  },
  state() {
    return {
      appTitle: 'Vuex Work'
    }
  },
})