<!-- TaskItem.vue -->
<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          {{ this.task.title }}
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="close"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot name="body">
          {{ this.task.description }}
        </slot>
       </section>

      <footer class="modal-footer">
        <button
          type="button"
          class="btn-green"
          @click="close"
        >
          Close Modal
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    task: Object,
  },
  data() {
    return {
      showDescription: false,
      showEditForm: false,
      editedTitle: this.task.title,
      editedDescription: this.task.description,
    };
  },
   
};
</script>

<style scoped>
/* Add your styles here */
</style>
