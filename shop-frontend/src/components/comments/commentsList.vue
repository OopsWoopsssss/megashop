<template>
  <div>
    <div v-for="comment in commentList" v-bind:key="comment.name">
      <span class="text-secondary">Имя: {{ comment.name }}</span>
      <p class="text-primary">{{ comment.text }}</p>
      <hr>
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