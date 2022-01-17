import axios from "axios";

export default ({
  state() {
    return {
    }
  },
  actions: {
    SET_COMMENTS_LIST(context, payload) {
      const data = {
          "name": payload.name,
          "email": payload.email,
          "product": payload.product,
          "text": payload.text,
        }
      const json = JSON.stringify({...data});
      axios.post('http://127.0.0.1:8000/api/v1/review/', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(data => {
        console.log(data)
      })
    },
  },
})
