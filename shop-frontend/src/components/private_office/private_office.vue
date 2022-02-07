<template>
  <div class="row">
    <div class="col-12">
      <div v-if="info">
        <h2>username: {{ info.username }}</h2>
        <h2>first_name: {{ info.first_name }}</h2>
        <h2>last_name: {{ info.last_name }}</h2>
        <h2>email: {{ info.email }}</h2>
        <h2>profile_pic: {{ info.profile_pic }}</h2>
        <h2>id: {{ info.id }}</h2>
      </div>
      <div v-else>
        Войдите пожалуйста
        <router-link class="ms-4" to="/auth">Авторизация</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "private office",
  data() {
    return {
      info: []
    }
  },
  mounted() {
    this.go_office()

  },
  methods: {
    go_office() {
      const token = localStorage.getItem('authToken');
      axios.get('http://127.0.0.1:8000/auth/users/me/', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token}`
        }
      }).then(data => {
        console.log(data)
        this.info = data.data
      }).catch(reject => {
        console.log(reject.response.data)
      })
    },
  }
}
</script>

<style scoped>

</style>