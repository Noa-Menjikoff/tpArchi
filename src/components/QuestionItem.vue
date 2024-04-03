<script>
export default {

  props: {
    question: Object
  },
  methods: {
    deleteQuestion() {
      this.$emit('remove', { id: this.question.id });
    },
  },
  emits: ['remove', 'edit', 'start-editing'],
};
</script>

<template>
  <div>
    <p>{{ question.title }}</p>
    <button @click="deleteQuestion">Supprimer</button>
  </div>
</template>
