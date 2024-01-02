<!-- TaskDetail.vue -->
<template>
    <div>
      <h2>{{ task.title }}</h2>
      <p>Status: {{ task.status }}</p>
      <p>{{ task.description }}</p>
      <router-link :to="'/tasks/' + task.id + '/edit'">Edit Task</router-link>
      <button @click="deleteTask">Delete Task</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        task: {},
      };
    },
    created() {
      // Fetch the task based on the route parameter
      const taskId = this.$route.params.id;
      this.task = this.tasks.find((task) => task.id === parseInt(taskId));
    },
    methods: {
      deleteTask() {
        // Implement task deletion logic
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  