import axios from "axios";

export default {
  state() {
    return {
      productsList: [],
    }
  },
  mutations: {
    SET_PRODUCT(state, productsList) {
      state.productsList = productsList
    }
  },
  actions: {
    GET_PRODUCT_LIST({commit}) {
      return axios('http://localhost/api/v1/products/?format=json', {
        method: 'GET'
      }).then((productsList) => {
        commit('SET_PRODUCT', productsList.data);
        return productsList
      }).catch((error) => {
        return error
      })
    },
  },
  getters: {
    PRODUCTS(state) {
      return state.productsList
    }
  },
}