<template>
  <div>
    <div class="row mt-5">
      <cards v-if="products.length" v-bind:products="products"></cards>
      <div v-else class="col-12 text-center">
        <h2>
          <img src="https://img.icons8.com/ios/50/000000/cute-monster.png"/>
          Товаров еще не завезли
          <img src="https://img.icons8.com/ios/50/000000/cute-monster.png"/>
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import cards from "../cards/cards";

export default {
  name: "CategoryBody",
  props: ['nameCategory'],
  emits: ['products'],
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
  computed:{
    products() {
      if (this.listProduct.data) {
        return this.listProduct.data.filter(e => e.category == this.nameCategory)
      }
      return true
    }
  },

  components: {
    cards,
  }
}
</script>

<style lang="scss" scoped>
  //.badge {
  //  &-secondary {
  //    color: #fff;
  //    background-color: #007bff;
  //  }
  //}
</style>