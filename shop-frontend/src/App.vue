<template>
  <div id="app">
    <div class="container">
      <span>
        {{ test }}
      </span>
      <br>
      <button v-on:click="loadProduct">
        ++
      </button>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
export default {
  // state: {
  //       backendUrl: "http://127.0.0.1:8000/api/v1"
  //   },
  name: 'App',
  data() {
    return {
      test: 1,
      backendUrl: "http://127.0.0.1:8000/api/v1/product",
      listProduct: [],
    }
  },
  methods: {
    incor() {
      this.test++
    },
    getServerUrl() {
      return this.backendUrl
    },
    async loadProduct() {
      let apaaaa = await axios.get('http://127.0.0.1:8000/api/v1/product/')
      console.log(apaaaa.data)
      // this.listProduct = await fetch('http://127.0.0.1:8000/api/v1/product/')
      //     .then(response => response.json())
      //     .then(data => console.log(data[0].name))
    },
  },

  components: {}
}
</script>

<style>
.container {
  max-width: 350px;
  margin: 0 auto;
}

.w-100 {
  width: 100%;
}
</style>
