<template>
  <div class="row mt-5">
    <div class="col-12 col-md-5">
      <img class="img" v-bind:src="product.poster" alt="image">
    </div>
    <div class="col-12 col-md-7 d-flex flex-column justify-content-between">
      <div>
        <h3>{{ product.title }}</h3>
        <b-badge class="text-uppercase" variant="primary">{{ product.category }}</b-badge>
        <p>{{ product.description }}</p>
        <p>цена: {{ product.price }}р</p>
      </div>
      <div>
        <button type="button" class="btn btn-primary">В корзину</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "cardProducts",
  props: ['idProducts'],
    data() {
    return {
      Products: [],
    }
  },
  mounted() {
    this.loadProductList();

  },
  methods: {
    async loadProductList() {
      this.Products = await axios.get('http://127.0.0.1:8000/api/v1/products/?format=json')
    },
  },
  computed:{
    product() {
      if (this.Products.data) {
        return this.Products.data.find(e => e.id == this.idProducts)
      }
      return true
    }
  },
}
</script>

<style scoped>

</style>