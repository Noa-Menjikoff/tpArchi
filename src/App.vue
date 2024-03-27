<script>

import TodoItem from "./components/TodoItem.vue";

let data = {
  todos: [{ id: 1, text : 'Faire le courses', checked : true}],
  quizs: [],
  title: 'Mes quiz',
  newItem: "",
  chgmtItem: ""
};

export default{
  data() {
    return data;
  },
  mounted(){
      fetch('http://localhost:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(json => {
          this.quizs = json
      })
  },
  methods: {
    removeItem: function(item){
      console.log(item.id);
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/"+item.id,{
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method:'DELETE'
      }).then(res =>{
        this.quizs.splice(this.quizs.indexOf(item),1);
      }).catch(res =>{ console.log(res)});
    },
  },
  components:{ TodoItem }
}
</script>

<template>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
        <div  class="container">
            <h2>{{ title }}</h2>
            <ol>
                <TodoItem
                v-for="item of quizs"
                :quiz="item"
                @remove = "removeItem"
                ></TodoItem>
            </ol>
            <div class="container">
                <h2> Ajouter un quiz</h2>
                <input v-model =newItem type="text"/>
                <span class="input-group-btn">
                    <button v-on:click ="addItem"
                        class="btn btn-default"
                        type="button">
                        Ajouter un todo
                    </button>
                    
                </span>
            </div>
        </div>
</template>