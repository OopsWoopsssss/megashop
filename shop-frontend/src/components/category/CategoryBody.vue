<template>
  <div>
    <div class="row mt-5">
      <div class="col-3" v-for="product in products" v-bind:key="product.id">
        <div class="card">
          <img class="card-img-top" v-bind:src="product.poster" alt="Card image cap">
          <div class="card-body">
            <h4 class="card-title">
              {{ product.title }}
            </h4>
            <router-link v-bind:to="product.category">
              <b-badge variant="secondary">{{ product.category }}</b-badge>
            </router-link>

            <p class="card-text">
              {{ product.description }}
            </p>
            <p>{{ product.price }}</p>
            <a href="#!" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
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

<style lang="scss" scoped>
  //.badge {
  //  &-secondary {
  //    color: #fff;
  //    background-color: #007bff;
  //  }
  //}
</style>