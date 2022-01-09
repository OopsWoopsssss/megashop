<template>
  <div class="col-12 col-sm-6 col-md-4 col-lg-3" v-for="product in products" v-bind:key="product.id">
    <div class="card">
      <img class="card-img-top" v-bind:src="'http://127.0.0.1:8000' + product.poster" alt="Card image cap">
      <div class="card-body">
        <h4 class="card-title">
          {{ product.title }}
        </h4>
        <router-link v-for="category in product.category" v-bind:key="category" v-bind:to="category">
          <b-badge class="me-2 d-inline-block" variant="secondary">{{ category }}</b-badge>
        </router-link>
        <p class="mt-3">{{ product.price }} р.</p>
        <div class="d-flex justify-content-between">
          <router-link v-bind:to="'/Product/' + product.id" class="btn btn-primary">Подробнее</router-link>
          <button type="button" class="btn btn-primary">В корзину</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cards",
  props:['products']
}
</script>

<style scoped>

</style>