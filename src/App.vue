<script>

import TodoItem from './components/TodoItem.vue';

let data ={
  todos : [{text : 'Faire les courses',checked : true,id:1},{text : 'Taches',checked : false,id:2}],
  title : 'Mes taches',
  newItem : {text :''}
};

export default {

  data(){
    return data;
  },
  methods:{
    addTodo: function(){
      this.todos.push({text : this.tache ,checked : false});
    },
    removeItem: function(id){
      for (var todo in this.todos){
        if (this.todos[todo].id == id.id){
          console.log(todo);
          this.todos.splice(todo,1);
        }
      }
      this.todos.splice();
    }  
  },

  components : { TodoItem }
  
  }


</script>

<template>

  <div id="app6" class="container">
            <h2>{{ title }}</h2>
            <ol>
              <TodoItem 
                v-for="item of todos":todo="item"
                @remove="removeItem">
                
              </TodoItem>
            </ol>
            <div class="container">
                <h2> Ajouter un Todo</h2>
                <input v-model ="tache" type="text"/>
                <span class="input-group-btn">
                    <button v-on:click ="addTodo"
                        class="btn btn-default"
                        type="button">
                        Ajouter un todo
                    </button>
                </span>
            </div>
        </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
