<!-- TaskListView.vue -->
<template>
    <div>
      <h2>Task List</h2>
      <router-link to="/tasks/create">Create Task</router-link>
      <ul class="list-group">
        <router-link
          v-for="task in tasks"
          :key="task.id"
          :to="'/tasks/' + task.id"
          class="list-group-item"
        >
          {{ task.title }}
        </router-link>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tasks: [
          { id: 1, title: "Task 1", description: "Description 1", status: "open" },
          { id: 2, title: "Task 2", description: "Description 2", status: "testing" },
          { id: 3, title: "Task 3", description: "Description 3", status: "done" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  