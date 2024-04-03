<script>
import QuestionItem from "./QuestionItem.vue";

let data = {
  questions:[],
  displayList: false 
}

export default {
  data() {
    return data;
  },
  mounted() {
    this.fetchQuestions();
  },
  props: {
    quiz: Object
  },
  methods: {
    fetchQuestions() {      
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/'+this.quiz.id+'/questions')
        .then(response => response.json())
        .then(json => {
          this.questions = json;
        });
    },
    deleteItem() {
      this.$emit('remove', { id: this.quiz.id });
    },
    editItem() {
      this.$emit('edit', { id: this.quiz.id });
    },
    startEditing() {
      this.$emit('start-editing', { id: this.quiz.id });
    },
    afficher() {
      this.displayList = !this.displayList; 
    },
    removeQuestion(item) {
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
  },
  emits: ['remove', 'edit', 'start-editing'],
  components: { QuestionItem }
};
</script>

<template>
  <div>
    <p @click="afficher">{{ quiz.name }}</p>
    <button @click="startEditing">Modifier</button>
    <button @click="deleteItem">Supprimer</button>
    <ul v-if="displayList">
      <li v-for="item of questions" :key="item.id" >
        <QuestionItem 
        :question="item"
        @remove="removeQuestion"
        ></QuestionItem>
      </li>
    </ul>
  </div>
</template>
