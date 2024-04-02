<script>
import TodoItem from "./components/TodoItem.vue";

let data = {
  quizs: [],
  title: 'Mes quiz',
  newItem: "",
  chgmtItem: ""
};

export default {
  data() {
    return data;
  },
  mounted() {
    fetch('http://localhost:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(json => {
        this.quizs = json;
      });
  },
  methods: {
    removeItem: function(item) {
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/" + item.id, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'DELETE'
      }).then(res => {
        this.quizs = this.quizs.filter(quiz => quiz.id !== item.id);
      }).catch(res => {
        console.log(res);
      });
    },

    addItem: function() {
      if (this.newItem.trim() === '') {
        return;
      }
      fetch("http://localhost:5000/quiz/api/v1.0/quiz", {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
          name: this.newItem 
        })
      }).then(response => response.json())
        .then(json => {
          console.log(json);
          this.newItem = '';
          window.location.reload();
        }).catch(error => {
          console.error('Erreur lors de l\'ajout du questionnaire :', error);
        });
    },

  },
  components: { TodoItem }
};
</script>

<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <TodoItem
        v-for="item of quizs"
        :quiz="item"
        @remove="removeItem"
        :key="item.id"
      ></TodoItem>
    </ol>
    <div class="container">
      <h2>Ajouter un quiz</h2>
      <input v-model="newItem" type="text" />
      <span class="input-group-btn">
        <button @click="addItem" class="btn btn-default" type="button">
          Ajouter un quiz
        </button>
      </span>
    </div>
  </div>
</template>
