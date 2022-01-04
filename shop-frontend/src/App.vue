<template>
  <div id="app">
    <nav class="header">
      <div class="container">
        <div class="header-content">
          <div>
            типо шапка
          </div>
          <router-link to="/Categories">Categories</router-link>
        </div>
      </div>
    </nav>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods: {

  },
  components: {
  },
}
</script>

<style>
  .header {
    background-color: black;
    color: white;
    padding: 10px;
  }
  .header-content {
    display: flex;
    justify-content: space-between;
  }
  .header a {
    color: white;
  }
</style>
