<template>
  <div>
    <div class="row">
      <div class="col-3" v-for="product in products" v-bind:key="product.id">
        <p>{{ product.id }}</p>
        <p>{{ product.description }}</p>
        <p>{{ product.price }}</p>
        <p>{{ product.category }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CategoryBody",
  props: ['nameCategory'],
  data() {
    return {
      listProduct: [],
    }
  },

  mounted() {
    this.loadProductList();

  },

  beforeUpdate() {
    console.log('mounted')
    console.log(this.listProduct.data)
  },

  methods: {
    async loadProductList() {
      this.listProduct = await axios.get('http://127.0.0.1:8000/api/v1/products/?format=json')
      console.log(this.listProduct.data)
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


}
</script>

<style scoped>

</style>