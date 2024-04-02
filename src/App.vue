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
    this.fetchQuizs();
  },
  methods: {
    fetchQuizs() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz')
        .then(response => response.json())
        .then(json => {
          this.quizs = json;
        });
    },
    removeItem(item) {
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/" + item.id, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'DELETE'
      }).then(() => {
        this.quizs = this.quizs.filter(quiz => quiz.id !== item.id);
      }).catch(error => {
        console.error('Erreur lors de la suppression du questionnaire :', error);
      });
    },
    addItem() {
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
      }).then(() => {
        this.newItem = '';
        this.fetchQuizs(); // Rafraîchir la liste après l'ajout
      }).catch(error => {
        console.error('Erreur lors de l\'ajout du questionnaire :', error);
      });
    },
    startEditing(item) {
      // Mettre l'élément en mode édition
      this.quizs.forEach(quiz => {
        if (quiz.id !== item.id) {
          quiz.editing = false;
        } else {
          quiz.editing = true;
        }
      });
    },
    confirmEdit(item) {
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/" + item.id, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'PUT',
        body: JSON.stringify({
          name: item.name
        })
      }).then(() => {
        item.editing = false; // Sortir du mode édition
      }).catch(error => {
        console.error('Erreur lors de la mise à jour du questionnaire :', error);
      });
    },
    editItem(item) {
      console.log(item);
    },
  },
  components: { TodoItem }
};
</script>


<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <li v-for="item of quizs" :key="item.id">
        <TodoItem
          :quiz="item"
          @remove="removeItem"
          @edit="editItem"
          @start-editing="startEditing"
        ></TodoItem>
        <!-- Champ d'édition et bouton de confirmation -->
        <div v-if="item.editing">
          <input v-model="item.name" type="text" />
          <button @click="confirmEdit(item)">Confirmer</button>
        </div>
      </li>
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

