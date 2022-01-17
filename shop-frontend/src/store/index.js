import {createStore} from 'vuex'
import category from "./category/category";
import products from "./products/products";
import comments from "./comments/comments";

export default createStore({
  modules: {
    category,
    products,
    comments,
  },
  state() {
    return {
      appTitle: 'Vuex Work'
    }
  },
})