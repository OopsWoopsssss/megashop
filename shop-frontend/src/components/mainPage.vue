<template>
  <div>
    <h1>Главная страница</h1>
    <hr>
    <h2>Все товары</h2>
    <div class="row mt-5">
      <cards v-bind:products="PRODUCTS"></cards>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import cards from "./cards/cards";

export default {
  name: "mainPage",
    data() {
    return {
    }
  },
  mounted() {
    this.GET_PRODUCT_LIST()
  },
  methods: {
    ...mapActions(['GET_PRODUCT_LIST']),
  },
  computed: {
    ...mapGetters(['PRODUCTS']),
  },
  components: {
    cards,
  }
}
</script>

<style scoped>

</style>