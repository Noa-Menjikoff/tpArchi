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
    }
  },
  emits: ['remove', 'edit', 'start-editing']
};
</script>

<template>
  <div>
    <p>{{ quiz.name }}</p>
    <button @click="startEditing">Modifier</button>
    <button @click="deleteItem">Supprimer</button>
  </div>
</template>
