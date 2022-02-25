import axios from "axios";
import router from "../../router";

export default ({
  state() {
    return {
      authToken: '',
      errors: ''
    }
  },
  mutations: {
    errors(state, payload) {
      state.errors = payload
    },
    clearErrors(state) {
      state.errors = {}
    }
  },
  actions: {
    AUTH_USER(context, payload) {
      const data = {
        "username": payload.username,
        "password": payload.password,
      }
      const json = JSON.stringify({...data});
      axios.post('http://localhost/auth/token/login', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        router.push({ path: '/privteOffice' })
        localStorage.setItem('authToken', response.data.auth_token);
      }).catch(reject => {
        context.commit('errors', reject.response)
      })
    },
  },
  getters: {
    GET_ERRORS(state) {
      return state.errors
    },
  },
})
