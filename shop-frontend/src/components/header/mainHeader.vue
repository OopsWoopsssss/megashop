<template>
  <div class="main-header">
    <nav class="navbar navbar-expand-lg">
      <div class="container-md">
        <router-link class="navbar-brand" to="/">
          <img src="https://img.icons8.com/color/50/000000/cute-monster.png"/>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <div class="navbar-toggler-wrapper">
            <span class="navbar-toggler-icon"></span>
            <span class="navbar-toggler-icon"></span>
            <span class="navbar-toggler-icon"></span>
          </div>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item nav-item--categories dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Категории
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li v-for="category in CATEGORIES" :key="category.id">
                  <router-link class="dropdown-item" v-bind:to="'/' + category.name">{{ category.name }}</router-link>
                </li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">О нас</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "header",
  data() {
    return {
    }
  },
  mounted() {
    this.GET_CATEGORIES_LIST()
  },
  methods: {
    ...mapActions(['GET_CATEGORIES_LIST']),
  },
  computed: {
    ...mapGetters(['CATEGORIES'])
  },
}
</script>

<style lang="scss" scoped>
  .main-header {
    .navbar {
      background-color: black;
      color: white;
      &-toggler {
        &-wrapper {
          display: flex;
          align-items: center;
          flex-direction: column;
          position: relative;
          transition: .3s;
        }
        &-icon {
          background-color: white;
          position: absolute;
          width: 30px;
          height: 3px;
          &:nth-child(1) {
            top: -9px;
          }
          &:nth-child(2) {
            opacity: 1;
          }
          &:nth-child(3) {
            top: 9px;
          }
        }
      }

      button[aria-expanded="true"] {
        .navbar-toggler{
          &-wrapper {
            transform: rotate(180deg);
          }
          &-icon {
            &:nth-child(1) {
              transform: rotate(45deg);
              top: 0px;
            }
            &:nth-child(2) {
              opacity: 0;
            }
            &:nth-child(3) {
              transform: rotate(-45deg);
              top: 0;
            }
          }
        }
      }

    }
    .dropdown {
      &-menu {
        background-color: black;
      }
      &-item {
        &:hover {
          color: black
        }
      }
    }
  }
  .header-content {
    display: flex;
    justify-content: space-between;
  }
  .main-header a {
    color: white;
  }
  .nav-item {
    &--categories {
      .router-link-active {
        background-color: gray;
      }
    }
  }
</style>