<script>

import TodoItem from "./components/TodoItem.vue";

let data = {
  todos: [{ id: 1, text : 'Faire le courses', checked : true}],
  title: 'Mes taches',
  newItem: "",
  chgmtItem: ""
};

export default{
  data() {
    return data;
  },
  methods: {
    addItem: function(){
      
      let text = this.newItem.trim();
      if(text){
        this.todos.push({id: this.todos.length+1,text: text, checked: false});
        this.newItem = "";
      }
    },
    removeItem: function(item){
      for(let i = 0; i < this.todos.length; i++){
        if(this.todos[i].id == item.id){
          this.todos.splice(i, 1);
          break;
        }
      }
    },
    editItem: function(item, nouveauNom){
      console.log(nouveauNom);
      for(let i = 0; i < this.todos.length; i++){
        if(this.todos[i].id == item.id){
          this.todos[i].text = nouveauNom;
          this.todos[i].checked = false;
          break;
        }
      }
    }
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
                v-for="item of todos"
                :todo="item"
                @remove = "removeItem"
                @edit = "editItem"
                ></TodoItem>
            </ol>
            <div class="container">
                <h2> Ajouter un Todo</h2>
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