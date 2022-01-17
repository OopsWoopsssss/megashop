<template>
  <div class="row mt-5" v-if="product">
    <div class="col-12 col-md-5">
      <img class="img" v-bind:src="'http://127.0.0.1:8000' + product.poster" alt="image">
    </div>
    <div class="col-12 col-md-7 d-flex flex-column justify-content-between">
      <div>
        <h3>{{ product.title }}</h3>
        <h3>{{  }}</h3>


        <form class="d-block">
          <div class="rate">
            <input v-on:change="submitForm" type="radio" v-model="checkedNames" checked id="star5" name="rate" value="5"/>
            <label for="star5" title="text">5 stars</label>
            <input v-on:change="submitForm" type="radio" v-model="checkedNames" id="star4" name="rate" value="4"/>
            <label for="star4" title="text">4 stars</label>
            <input v-on:change="submitForm" type="radio" v-model="checkedNames" id="star3" name="rate" value="3"/>
            <label for="star3" title="text">3 stars</label>
            <input v-on:change="submitForm" type="radio" v-model="checkedNames" id="star2" name="rate" value="2"/>
            <label for="star2" title="text">2 stars</label>
            <input v-on:change="submitForm" type="radio" v-model="checkedNames" id="star1" name="rate" value="1"/>
            <label for="star1" title="text">1 star</label>
          </div>
        </form>


        <b-badge v-for="category in product.category" v-bind:key="category" class="text-uppercase me-2"
                 variant="primary">{{ category }}
        </b-badge>
        <div v-html="product.description"></div>
        <p>цена: {{ product.price }}р</p>
      </div>
      <div>
        <button type="button" class="btn btn-primary">В корзину</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from "axios";

export default {
  name: "cardProduct",
  props: ['idProducts'],
  data() {
    return {
      checkedNames: this.star,
    }
  },
  mounted() {
    this.GET_PRODUCT_LIST();
  },
  methods: {
    ...mapActions(['GET_PRODUCT_LIST']),

    async submitForm() {
      let params = {
        "star": parseInt(this.checkedNames),
        "product": this.product.id,
      }
      console.log(params)
      const json = JSON.stringify({...params});
      const res = await axios.post('http://127.0.0.1:8000/api/v1/rating/', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(data => {
        console.log(data)
      })
      console.log(res)
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
    star() {
      this.checkedNames = this.product.middle_star
    }
  }
}
</script>


<style scoped>

.rate {
  float: left;
  height: 46px;
  padding: 0 10px;
}

.rate:not(:checked) > input {
  position: absolute;
  top: -9999px;
}

.rate:not(:checked) > label {
  float: right;
  width: 1em;
  overflow: hidden;
  white-space: nowrap;
  cursor: pointer;
  font-size: 30px;
  color: #ccc;
}

.rate:not(:checked) > label:before {
  content: '★ ';
}

.rate > input:checked ~ label {
  color: #ffc700;
}

.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
  color: #deb217;
}

.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
  color: #c59b08;
}

</style>