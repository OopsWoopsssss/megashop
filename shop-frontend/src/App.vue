<template>
  <div id="app">
    <mainAppHeader></mainAppHeader>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import mainAppHeader from "./components/header/mainHeader";
export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods: {

  },
  components: {
    mainAppHeader,
  },
}
</script>

<style>

</style>
