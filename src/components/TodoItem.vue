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
    },
    emits : ['remove']
}
</script>

<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <div>
        <p>{{ quiz.name }}</p>
        <input type="button"
            class="btnbtn-danger"
            value="Supprimer"
            @click="suppr">
    </div>

            


</template>