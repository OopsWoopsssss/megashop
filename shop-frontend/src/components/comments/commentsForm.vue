<template>
  <div class="my-5">
    <form class="row" v-on:submit.prevent="submitForm">
      <div class="col-6">
        <div class="form-floating mb-3">
          <input v-model="commentName" required type="name" class="form-control" id="floatingInput" placeholder="Имя">
          <label for="floatingInput">Имя</label>
        </div>
      </div>
      <div class="col-6">
        <div class="form-floating">
          <input v-model="commentEmail" required type="email" class="form-control" id="floatingPassword" placeholder="email">
          <label for="floatingPassword">email</label>
        </div>
      </div>
      <div class="col-12 mt-2">
        <div class="form-floating">
          <textarea v-model="commentText" required class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
          <label for="floatingTextarea">Comments</label>
        </div>
      </div>
      <div class="col-12">
        <button class="w-100 mt-2 btn btn-primary">Отправить</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props:['id'],

  data(){
    return {
      commentName: '',
      commentEmail: '',
      commentText: '',
    }
  },

  methods: {
    ...mapActions(['SET_COMMENTS_LIST']),

    submitForm(){
      this.SET_COMMENTS_LIST({
        "name": this.commentName,
        "email": this.commentEmail,
        "product": this.id,
        "text": this.commentText,
      })
      this.commentName = ''
      this.commentEmail = ''
      this.commentText = ''

      this.$emit('submitForm')
    }
  }
}
</script>

<style lang="scss" scoped>

</style>