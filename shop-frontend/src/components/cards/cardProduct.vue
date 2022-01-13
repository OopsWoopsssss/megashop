<template>
  <div class="row mt-5">
    <div class="col-12 col-md-5">
      <img class="img" v-bind:src="'http://127.0.0.1:8000' + product.poster" alt="image">
    </div>
    <div class="col-12 col-md-7 d-flex flex-column justify-content-between">
      <div>
        <h3>{{ product.title }}</h3>
        <b-badge v-for="category in product.category" v-bind:key="category" class="text-uppercase me-2" variant="primary">{{ category }}</b-badge>
        <div v-html="product.description"></div>
        <p>цена: {{ product.price }}р</p>
      </div>
      <div>
        <button type="button" class="btn btn-primary">В корзину</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "cardProduct",
  props: ['idProducts'],
    data() {
    return {
    }
  },
  mounted() {
    this.GET_PRODUCT_LIST()
  },
  methods: {
    ...mapActions(['GET_PRODUCT_LIST'])
  },
  computed:{
    ...mapGetters(['PRODUCTS']),
    product() {
      if (this.PRODUCTS) {
        return this.PRODUCTS.find(e => e.id == this.idProducts)
      }
      return true
    }
  },
}
</script>

<style scoped>

</style>