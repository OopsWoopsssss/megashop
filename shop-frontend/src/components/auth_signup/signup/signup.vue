<template>
  <div class="container-md">
    <div class="row">
      <div class="dol-12">
        <form class="mt-5" v-on:submit.prevent="signup">
          <div class="mb-3">
            <label for="nameSignupId" class="form-label">Имя пользователя</label>
            <input v-model="signupName" type="name" class="form-control" id="nameSignupId" aria-describedby="nameSignup">
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Пароль</label>
            <input v-model="signupPassword" type="password" class="form-control" id="exampleInputPassword1">
            <span class="text-danger">{{ errorpassword }}</span>
          </div>
          <button type="submit" class="btn btn-1 hover--down">
            <span>Submit</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "signup",
  data() {
    return {
      signupName: '',
      signupPassword: '',
      errorpassword: ''
    }
  },
  methods: {
    signup() {
      const data = {
          "username": this.signupName,
          "password": this.signupPassword,
        }
      const json = JSON.stringify({...data});
      axios.post('http://localhost/auth/users/', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(data => {
        console.log(data)
      }).catch(reject => {
        console.log(reject.response.data.password[0])
        this.errorpassword = reject.response.data.password[0]
      })
    },
  }
}
</script>

<style scoped>

</style>