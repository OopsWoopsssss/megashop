<template>
  <div class="container-md">
    <div class="row">
      <div class="dol-12">
        <form class="mt-5" v-on:submit.prevent="auth">
          <span class="text-danger"> {{ this.getErrors.non_field_errors }}</span>
          <div class="mb-3">
            <label for="nameauthId" class="form-label">Имя пользователя</label>
            <input v-model="authName" v-on:focus="this.clearErrors" type="name" class="form-control" id="nameauthId" aria-describedby="nameauth">
            <span class="text-danger"> {{ this.getErrors.username }}</span>
          </div>
          <div class="mb-3">
            <label for="new-password" class="form-label">Пароль</label>
            <input v-model="authPassword" v-on:focus="this.clearErrors" type="new-password" class="form-control" id="new-password">
            <span class="text-danger"> {{ this.getErrors.password }}</span>
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
import { mapActions, mapGetters, mapMutations } from 'vuex'

export default {
  name: "auth",
  data() {
    return {
      authName: '',
      authPassword: '',
    }
  },
  methods: {
    ...mapActions(['AUTH_USER']),
    ...mapMutations(['clearErrors']),
    auth() {
      this.AUTH_USER({
        "username": this.authName,
        "password": this.authPassword,
      })
    },
  },
  computed: {
    ...mapGetters(['GET_ERRORS']),
    getErrors(){
      let errors = {}
      if (this.GET_ERRORS?.data) {
        console.log(this.GET_ERRORS.data)
        for (let el in this.GET_ERRORS.data) {
          let errorText = ''
          for (let item in this.GET_ERRORS.data[el]) {
            errorText += '' + this.GET_ERRORS.data[el][item]
          }
          errors[el] = errorText
        }
      }
      return errors
    },
  }
}
</script>
"27fc80139acc0f69993fd9524c1b5d7fd617cb40"
<style scoped>

</style>