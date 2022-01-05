<template>
  <div>
    <h1>Главная страница</h1>
    <hr>
    <h2>Все товары</h2>
    <div class="row mt-5">
      <cards v-bind:products="listProduct.data"></cards>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cards from "./cards/cards";

export default {
  name: "mainPage",
    data() {
    return {
      listProduct: [],
    }
  },
  mounted() {
    this.loadProductList();

  },
  methods: {
    async loadProductList() {
      this.listProduct = await axios.get('http://127.0.0.1:8000/api/v1/products/?format=json')
    },
  },
  components: {
    cards,
  }
}
</script>

<style scoped>

</style>