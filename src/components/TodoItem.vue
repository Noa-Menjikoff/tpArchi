<script>


export default{
    data(){
        return{
        }
    },
    props : {
        quiz : Object
    },
}
</script>

<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <p>{{ quiz.name }}</p>
            


</template>