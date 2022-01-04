<template>
  <div>
    <h1>catigories</h1>
    <ul class="list">
      <li class="list-item" v-for="category in categoryList.data" :key="category.id">
        <router-link v-bind:to="category.name">{{ category.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AppCategories",
  data() {
    return {
      categoryList: [],
    }
  },
  mounted() {
    this.loadCategoryList();
  },

  methods: {
    async loadCategoryList() {
      this.categoryList = await axios.get('http://127.0.0.1:8000/api/v1/category/?format=json')
    },
  }

}
</script>

<style scoped>

</style>