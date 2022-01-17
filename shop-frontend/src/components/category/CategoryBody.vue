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
import cards from "../cards/cards";
import { mapActions , mapGetters } from "vuex";

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
    this.GET_PRODUCT_LIST();

  },
  methods: {
    ...mapActions(['GET_PRODUCT_LIST'])
  },
  computed:{
    ...mapGetters(['PRODUCTS']),
    products() {
      if (this.PRODUCTS) {
        return this.PRODUCTS.filter(e => {
          for(let key in e.category) {
            if (this.nameCategory == e.category[key]) {
              return true
            }
          }
        })
      }
      return true
    },
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