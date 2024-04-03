<script>
export default {

  props: {
    question: Object
  },
  methods: {
    deleteQuestion() {
      this.$emit('remove', { id: this.question.id });
    },
    editQuestion() {
      this.$emit('edit', { id: this.question.id });
    },
    startEditingQuestion() {
      this.$emit('start-editing', { id: this.question.id });
    },
  },
  emits: ['remove', 'edit', 'start-editing'],
};
</script>

<template>
  <div>
    <p>{{ question.title }}</p>
    <button @click="startEditingQuestion">Modifier</button>
    <button @click="deleteQuestion">Supprimer</button>
  </div>
</template>
