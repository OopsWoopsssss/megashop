<template>
  <div class="row mt-5" v-if="product">
    <div class="col-12 col-md-5">
      <img class="img" v-bind:src="'http://127.0.0.1:8000' + product.poster" alt="image">
    </div>
    <div class="col-12 col-md-7 d-flex flex-column justify-content-between">
      <div>
        <h3>{{ product.title }}</h3>
        <form>
          <hr>
          <div class="raiting">
            <input class="raiting__control visually-hidden" type="radio" v-on:change="submitForm" v-model="checkedNames"
                   name="raiting" value="1" id="raiting-1">
            <label class="raiting__label" for="raiting-1">
              <svg class="raiting__icon" width="38" height="38" viewBox="0 0 38 38">
                <path fill="currentColor"
                      d="M26.22 32.01c-.2 0-.41-.05-.6-.15l-6.64-3.65-6.64 3.65c-.44.25-.98.2-1.38-.1-.4-.31-.6-.83-.51-1.35l1.3-7.7-5.37-5.48a1.42 1.42 0 01-.32-1.37c.15-.5.56-.86 1.05-.93l7.43-1.14 3.27-7.02A1.3 1.3 0 0118.98 6c.5 0 .96.3 1.17.77l3.31 7.01 7.43 1.14c.49.07.9.43 1.05.93.14.48.02 1-.32 1.37l-5.37 5.47 1.3 7.7c.1.53-.1 1.07-.52 1.38-.23.17-.52.26-.8.24z"></path>
              </svg>
              <span class="visually-hidden">1</span>
            </label>

            <input class="raiting__control visually-hidden" type="radio" v-on:change="submitForm" v-model="checkedNames"
                   name="raiting" value="2" id="raiting-2">
            <label class="raiting__label" for="raiting-2">
              <svg class="raiting__icon" width="38" height="38" viewBox="0 0 38 38">
                <path fill="currentColor"
                      d="M26.22 32.01c-.2 0-.41-.05-.6-.15l-6.64-3.65-6.64 3.65c-.44.25-.98.2-1.38-.1-.4-.31-.6-.83-.51-1.35l1.3-7.7-5.37-5.48a1.42 1.42 0 01-.32-1.37c.15-.5.56-.86 1.05-.93l7.43-1.14 3.27-7.02A1.3 1.3 0 0118.98 6c.5 0 .96.3 1.17.77l3.31 7.01 7.43 1.14c.49.07.9.43 1.05.93.14.48.02 1-.32 1.37l-5.37 5.47 1.3 7.7c.1.53-.1 1.07-.52 1.38-.23.17-.52.26-.8.24z"></path>
              </svg>
              <span class="visually-hidden">2</span>
            </label>

            <input class="raiting__control visually-hidden" type="radio" v-on:change="submitForm" v-model="checkedNames"
                   name="raiting" value="3" id="raiting-3">
            <label class="raiting__label" for="raiting-3">
              <svg class="raiting__icon" width="38" height="38" viewBox="0 0 38 38">
                <path fill="currentColor"
                      d="M26.22 32.01c-.2 0-.41-.05-.6-.15l-6.64-3.65-6.64 3.65c-.44.25-.98.2-1.38-.1-.4-.31-.6-.83-.51-1.35l1.3-7.7-5.37-5.48a1.42 1.42 0 01-.32-1.37c.15-.5.56-.86 1.05-.93l7.43-1.14 3.27-7.02A1.3 1.3 0 0118.98 6c.5 0 .96.3 1.17.77l3.31 7.01 7.43 1.14c.49.07.9.43 1.05.93.14.48.02 1-.32 1.37l-5.37 5.47 1.3 7.7c.1.53-.1 1.07-.52 1.38-.23.17-.52.26-.8.24z"></path>
              </svg>
              <span class="visually-hidden">3</span>
            </label>

            <input class="raiting__control visually-hidden" type="radio" v-on:change="submitForm" v-model="checkedNames"
                   name="raiting" value="4" id="raiting-4">
            <label class="raiting__label" for="raiting-4">
              <svg class="raiting__icon" width="38" height="38" viewBox="0 0 38 38">
                <path fill="currentColor"
                      d="M26.22 32.01c-.2 0-.41-.05-.6-.15l-6.64-3.65-6.64 3.65c-.44.25-.98.2-1.38-.1-.4-.31-.6-.83-.51-1.35l1.3-7.7-5.37-5.48a1.42 1.42 0 01-.32-1.37c.15-.5.56-.86 1.05-.93l7.43-1.14 3.27-7.02A1.3 1.3 0 0118.98 6c.5 0 .96.3 1.17.77l3.31 7.01 7.43 1.14c.49.07.9.43 1.05.93.14.48.02 1-.32 1.37l-5.37 5.47 1.3 7.7c.1.53-.1 1.07-.52 1.38-.23.17-.52.26-.8.24z"></path>
              </svg>
              <span class="visually-hidden">4</span>
            </label>

            <input class="raiting__control visually-hidden" type="radio" v-on:change="submitForm" v-model="checkedNames"
                   name="raiting" value="5" id="raiting-5">
            <label class="raiting__label" for="raiting-5">
              <svg class="raiting__icon" width="38" height="38" viewBox="0 0 38 38">
                <path fill="currentColor"
                      d="M26.22 32.01c-.2 0-.41-.05-.6-.15l-6.64-3.65-6.64 3.65c-.44.25-.98.2-1.38-.1-.4-.31-.6-.83-.51-1.35l1.3-7.7-5.37-5.48a1.42 1.42 0 01-.32-1.37c.15-.5.56-.86 1.05-.93l7.43-1.14 3.27-7.02A1.3 1.3 0 0118.98 6c.5 0 .96.3 1.17.77l3.31 7.01 7.43 1.14c.49.07.9.43 1.05.93.14.48.02 1-.32 1.37l-5.37 5.47 1.3 7.7c.1.53-.1 1.07-.52 1.38-.23.17-.52.26-.8.24z"></path>
              </svg>
              <span class="visually-hidden">5</span>
            </label>

            <div class="raiting__focus"></div>
          </div>
          <hr>
        </form>
        <b-badge v-for="category in product.category" v-bind:key="category" class="text-uppercase me-2"
                 variant="primary">{{ category }}
        </b-badge>
        <div v-html="product.description"></div>
        <p>цена: {{ product.price }}р</p>
      </div>
      <div>
        <button type="submit" class="btn btn-1 hover--down">
          <span>В корзину</span>
        </button>
      </div>
    </div>
    <commentsList v-bind:commentList="product.reviews"></commentsList>
    <commentsForm v-on:submitForm="GET_PRODUCT_LIST()" v-bind:id="product.id"></commentsForm>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from "axios";

import commentsForm from "../comments/commentsForm";
import commentsList from "../comments/commentsList";

export default {
  name: "cardProduct",
  props: ['idProducts'],
  data() {
    return {
      checkedNames: 0,
    }
  },
  mounted() {
    this.GET_PRODUCT_LIST();
  },
  methods: {
    ...mapActions(['GET_PRODUCT_LIST']),

    submitForm() {
      let params = {
        "star": parseInt(this.checkedNames),
        "product": this.product.id,
      }
      console.log(params)
      const json = JSON.stringify({...params});
      axios.post('http://127.0.0.1:8000/api/v1/rating/', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }
  },
  computed: {
    ...mapGetters(['PRODUCTS']),
    product() {
      if (this.PRODUCTS) {
        return this.PRODUCTS.find(e => e.id == this.idProducts)
      }
      return true
    },

  },
  watch: {
    product(){
      this.checkedNames = this.product.middle_star
    },
  },
  components: {
    commentsForm,
    commentsList,
  }
}
</script>


<style scoped>

.visually-hidden {
  position: absolute;
  margin: -1px;
  clip-path: inset(50%);
  clip: rect(0 0 0 0);
  overflow: hidden;
  width: 1px;
  height: 1px;
  border: 0;
  padding: 0;
  white-space: nowrap;
}

.raiting {
  position: relative;
  display: inline-flex;
  align-items: center;
  color: hsl(219deg, 35%, 92%);
}

.raiting__icon {
  display: block;
  overflow: visible;
}

.raiting__focus {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  pointer-events: none;
}

.raiting__label {
  flex: 0 0 auto;
  color: hsl(40deg, 100%, 50%);
  cursor: pointer;
  transition: transform .24s cubic-bezier(.47, .34, .34, 1.77),
  color 125ms;
}

.raiting__label:hover {
  transform: scale(1.2);
}

.raiting__control {
}

.raiting__control:indeterminate + .raiting__label {
  color: hsl(219deg, 35%, 92%);
}

.raiting__control:focus + .raiting__label {
  transform: scale(1.2);
}

.raiting__control:focus ~ .raiting__focus {
  outline: 2px solid #4254ff;
}

.raiting__control:focus-visible + .raiting__label {
  outline: 2px solid #4254ff;
}

.raiting__control:focus:not(:focus-visible) ~ .raiting__focus,
.raiting__control:focus-visible ~ .raiting__focus {
  outline: none;
}

.raiting__control:checked + .raiting__label {
  color: hsl(40deg, 100%, 50%);
  transform: scale(1.2);
}

.raiting__control:checked + .raiting__label ~ .raiting__label {
  color: hsl(219deg, 35%, 92%);
}

.raiting:hover .raiting__label.raiting__label,
.raiting:hover .raiting__label:hover {
  color: hsl(40deg, 100%, 50%);
}

.raiting:hover .raiting__label:hover ~ .raiting__label {
  color: hsl(219deg, 35%, 92%);
}


</style>