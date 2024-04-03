<script>
export default {
  props: {
    quiz: Object
  },
  methods: {
    deleteItem() {
      this.$emit('remove', { id: this.quiz.id });
    },
    editItem() {
      this.$emit('edit', { id: this.quiz.id });
    },
    startEditing() {
      this.$emit('start-editing', { id: this.quiz.id });
    },
    consult(){
        this.$emit('consult', { id: this.quiz.id });
    }
  },
  emits: ['remove', 'start-editing', 'consult']
};
</script>


<template>
  <div>
    <p>{{ quiz.name }}</p>
    <button @click="startEditing">Modifier</button>
    <button @click="deleteItem">Supprimer</button>
    <button @click="consult">Consulter</button>
  </div>
</template>
