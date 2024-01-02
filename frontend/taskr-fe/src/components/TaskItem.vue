<!-- TaskItem.vue -->
<template>
  <li class="list-group-item">
    <div>
      <strong>{{ task.title }}</strong>
      <span class="badge badge-primary">{{ task.status }}</span>
    </div>
    <div>
      <button @click="showDescription">Show Description</button>
      <button @click="editTask">Edit</button>
      <button @click="deleteTask">Delete</button>
    </div>
    <div v-if="showDescription">
      <p>{{ task.description }}</p>
    </div>
    <div v-if="showEditForm">
      <input v-model="editedTitle" placeholder="Enter new title" />
      <textarea v-model="editedDescription" placeholder="Enter new description"></textarea>
      <button @click="saveEdit">Save</button>
    </div>
  </li>
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
  methods: {
    showDescription() {
      this.showDescription = !this.showDescription;
    },
    editTask() {
      this.showEditForm = true;
    },
    saveEdit() {
      this.$emit("updateTask", {
        ...this.task,
        title: this.editedTitle,
        description: this.editedDescription,
      });
      this.showEditForm = false;
    },
    deleteTask() {
      this.$emit("deleteTask", this.task.id);
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
