<script>

let newNom = 'ddddddddddd';
let edition = 'non';

export default{
    data(){
        return{
            edition: edition,
            newNom: newNom
        }
    },
    props : {
        todo : Object
    },
    methods : {
        suppr : function() {
            this.$emit('remove',{id:this.todo.id});
        },
        edit : function() {
            console.log(newNom);
            this.$emit('edit',{id:this.todo.id, newNom});
        }
    },
    emits : ['remove', 'edit']

}
</script>

<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <div class="checkbox" v-bind:class ="{ 'alert alert-success': todo.checked }">
        <label>
            <input type="checkbox" v-model ="todo.checked">
            {{ todo.text }}
        </label>
    </div>
    <input type="button"
        class="btnbtn-danger"
        value="Supprimer"
        @click="suppr">
    <input type="button"
        class="btnbtn-success"
        value="Editer"
        @click="edition = 'ok'">
    <input v-if ="edition === 'ok'" v-model=newNom type="text"/>
    <input v-if ="edition === 'ok'" type="button" class="btnbtn-success" value="Confirmer" @click="edit"/>
    <span v-else></span>
</template>