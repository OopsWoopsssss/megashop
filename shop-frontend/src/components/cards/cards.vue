<template>
  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="product in products" v-bind:key="product.id">
    <div class="card">
      <div class="card-img-top"
           v-bind:style="`background-image: url(${'http://127.0.0.1:8000' + product.poster})`">
      </div>
      <div class="card-body">
        <h4 class="card-title">
          {{ product.title }}
        </h4>
        <router-link v-for="category in product.category" v-bind:key="category" v-bind:to="category">
          <b-badge class="me-2 d-inline-block" variant="secondary">{{ category }}</b-badge>
        </router-link>
        <p class="mt-3">{{ product.price }} р.</p>
        <div class="">
          <router-link v-bind:to="'/Product/' + product.id" class="btn btn-2 hover--down d-block w-100 mb-2">
            <span>Подробнее</span>
          </router-link>
          <button type="button" class="btn btn-1 hover--down d-block w-100">
            <span>В корзину</span>
          </button>
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
  .card-img-top {
    padding-bottom: 60%;
    background-size: cover;
    background-position: center;
  }
</style>