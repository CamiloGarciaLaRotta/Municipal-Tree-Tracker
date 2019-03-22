<template>
	<div id="cities">
    <h1> Cities </h1>
    
    <div id="newcity">
      name:  <input placeholder="City Name" v-model="newCity" type=text>
      <button @click="createCity(newCity)">Create</button>
    </div>

    <div id="listing">
      <h3> listing all cities: </h3>
      <ol>
        <li v-bind:key="m.cid" v-for="m in cities" style="width=100%">
          <div>
            <span> {{m.c_name.replace(new RegExp('-| ', 'g'), '_')}} <strong v-on:click="deleteCity(m.cid)" style="color:red"> X </strong> </span>
          </div>
        </li>
      </ol>
    </div>
    <div class="alert alert-secondary" role="alert" v-if="errorCity" style="color:red">Error: {{errorCity.response.data.message}}  </div>
  </div>
</template>

<script>
// init script for services
import axios from 'axios'
var config = require('../../config')

var frontendUrl = 'http://' + config.dev.host + ':' + config.dev.port
var backendUrl = 'http://' + config.dev.backendHost + ':' + config.dev.backendPort

var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: { 'Access-Control-Allow-Origin': frontendUrl }
})

//  export module
export default {
  name: 'cities',
  data () {
    return {
      cities: [],
      newCity: '',
      errorCity: '',
      response: [],
      trees: [],
      errorTree: ''
    }
  },
  created: function () {
    this.updateView()
  },
  methods: {
    createCity: function (newCity) {
      var params = {
        c_name: newCity,
        c_polygon: '((1.0,0.0),(0.0,0.0),(2.0,3.0))'
      }
      AXIOS.post('/cities', params)
      .then(response => {
        // JSON responses are automatically parsed.
        this.updateView()
      })
      .catch(e => {
        this.errorCity = e
      })
    },
    deleteCity: function (cid) {
      AXIOS.delete('/cities/' + cid)
      .then(response => {
        this.updateView()
      })
      .catch(e => {
        this.errorCity = e
      })
    },
    updateView: function () {
      this.errorTree = ''
      this.errorTransaction = ''
      AXIOS.get('/cities')
      .then(response => {
        this.cities = response.data
      })
      .catch(e => {
        this.errorTree = e
      })
    }
  }
}
</script>

<style scoped>

#newcity, #listing {
  margin-top: 4em;
  margin-left:3em;
  float:left;
  clear:both;
}
#listing li {
  text-align: left;
}

input {
  text-align: center; 
}
select, input {
  border-radius: 1em;
  border-color: none;
}
button{
    background-color: #060E3D;
    color: white;
    padding: 3px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    display:block;
    margin:auto;
    border-radius: 1em;
    display:inline-block;
}

button:hover{
    background-color: #555555;
}
#myModal3 ul {
  list-style-type: none;
  text-align: center;
  margin-left:-3em;
}

/* The Modal (background) */
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 30%;
}

/* The Close Button */
.close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
}
span {
  display: inline;
}
strong{
  cursor: pointer;
}
</style>