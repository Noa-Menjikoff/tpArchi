<script>


export default{
    data(){
        return{
        }
    },
    props : {
        quiz : Object
    },
    methods : {
        suppr : function() {
            this.$emit('remove',{id:this.quiz.id});
        },
        edit : function() {
            this.$emit('edit',{id:this.quiz.id});
        },
    },
    emits : ['remove','edit']
}
</script>

<template>
    <div>
      <p>{{ quiz.name }}</p>
      <button @click="edit">Modifier</button>
      <button @click="suppr">Supprimer</button>
    </div>
  </template>