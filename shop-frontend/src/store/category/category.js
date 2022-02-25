import axios from "axios";

export default ({
  state() {
    return {
      categoriesList: []
    }
  },
  mutations: {
    SET_CATEGORIES(state, categoriesList){
      state.categoriesList = categoriesList
    }
  },
  actions: {
    GET_CATEGORIES_LIST({commit}) {
      return axios('http://localhost/api/v1/category/', {
        method: 'GET'
      }).then((categoriesList) => {
        commit('SET_CATEGORIES', categoriesList.data);
        return categoriesList
      })
    },
  },
  getters: {
    CATEGORIES(state) {
      return state.categoriesList
    },
  },
})
