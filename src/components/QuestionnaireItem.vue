<script>
import QuestionItem from "./QuestionItem.vue";

let data = {
  questions:[],
  displayList: false ,
  newQuestion:'',
  type:'',
  answer:'',
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
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/"+this.quiz.id+"/questions/"+item.id, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'DELETE'
      }).then(() => {
        this.questions = this.questions.filter(question => question.id !== item.id);
      }).catch(error => {
        console.error('Erreur lors de la suppression du questionnaire :', error);
      });
    },
    addQuestion() {
      if (this.newQuestion.trim() === '') {
        return;
      }
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/"+this.quiz.id+"/questions", {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
          title: this.newQuestion,
          type: this.type,
          answer: this.answer
        })
      }).then(() => {
        this.newQuestion = '';
        this.type = '';
        this.answer = '';
        this.fetchQuestions(); // Rafraîchir la liste après l'ajout
      }).catch(error => {
        console.error('Erreur lors de l\'ajout du questionnaire :', error);
      });
    },
    startEditingQuestion(item) {
      this.questions.forEach(question => {
        if (question.id !== item.id) {
          question.editing = false;
        } else {
          question.editing = true;
        }
      });
    },
    confirmEdit(item) {
    console.log(this.quiz.id)
    console.log(item.id)
      fetch("http://localhost:5000/quiz/api/v1.0/quiz/"+this.quiz.id+"/questions/" + item.id, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        method: 'PUT',
        body: JSON.stringify({
          title: item.title,
          answer: item.answer,
          proposition1:'',
          proposition2:''
        })
      }).then(() => {
        item.editing = false; // Sortir du mode édition
      }).catch(error => {
        console.error('Erreur lors de la mise à jour du questionnaire :', error);
      });
    },
    editQuestion(item) {
      console.log(item);
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
        @edit="editQuestion"
        @start-editing="startEditingQuestion"
        ></QuestionItem>
        <div v-if="item.editing">
          <input v-model="item.title " type="text" />
          <button @click="confirmEdit(item)">Confirmer</button>
        </div>
      </li>


      <h2>Ajouter une question</h2>
      <input v-model="newQuestion" type="text" placeholder="question"/>
      <input v-model="type" type="text" placeholder="type"/>
      <input v-model="answer" type="text" placeholder="answer"/>
      <span class="input-group-btn">
        <button @click="addQuestion" class="btn btn-default" type="button">
          Ajouter une question
        </button>
      </span>
    </ul>
    
  </div>
</template>
