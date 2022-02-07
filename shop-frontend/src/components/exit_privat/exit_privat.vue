<template>
  <button type="submit" class="btn btn-2 hover--up ms-3">
    <span>Выход</span>
  </button>

</template>

<script>
import axios from "axios";

export default {
  name: "exit_privat",
  methods: {
    exit() {
      const token = localStorage.getItem('authToken');
      console.log(token)
      axios('http://127.0.0.1:8000/auth/token/logout/', {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
        }
      }).then(data => {
        console.log(data)
      })
      localStorage.removeItem('authToken')
      this.$router.push({ path: '/' })
    },
  }
}
</script>

<style scoped>

</style>