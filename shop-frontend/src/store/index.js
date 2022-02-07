import {createStore} from 'vuex'
import category from "./category/category";
import products from "./products/products";
import comments from "./comments/comments";
import auth from "./auth/auth";

export default createStore({
  modules: {
    category,
    products,
    comments,
    auth,
  },
  state() {
    return {
      appTitle: 'Vuex Work'
    }
  },
})