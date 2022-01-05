<template>
  <div id="app">
    <app-header></app-header>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import appHeader from "./components/header/header";
export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods: {

  },
  components: {
    appHeader,
  },
}
</script>

<style>

</style>
