<template>
  <div class="col-12 col-sm-6 col-md-4 col-lg-3" v-for="product in products" v-bind:key="product.id">
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
        <router-link v-bind:to="'/Product/' + product.title" class="btn btn-primary">Go somewhere</router-link>
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