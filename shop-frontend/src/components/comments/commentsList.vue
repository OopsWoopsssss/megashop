<template>
  <div class="mt-5">
    <div v-if="commentList.length">
      <div v-for="comment in commentList" v-bind:key="comment.name">
        <span class="text-secondary">Имя: {{ comment.name }}</span>
        <p class="text-primary">{{ comment.text }}</p>
        <hr>
      </div>
    </div>
    <div v-else class="text-uppercase text-center">
      <img src="https://img.icons8.com/ios/50/000000/cute-monster.png"/>
          коментариев еще нет
      <img src="https://img.icons8.com/ios/50/000000/cute-monster.png"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "commentsList",
  props: ['commentList'],

  computed: {
    commentsw() {
      return this.commentList
    },
  },
}
</script>

<style scoped>

</style>