<script setup>
import TaskList from '../components/TaskList.vue';
</script>

<template>
  <div class="nav bg-dark display-flex justify-content-center">
    <TaskList :task_list="tasksList" :status="'Open'" />
    <TaskList :task_list="tasksList" :status="'Testing'" />
    <TaskList :task_list="tasksList" :status="'Done'" />
  </div>
    
</template>
  
  <script>
export default {
  data() {
    return {
      tasksList: [],
      timer: ''
    }
  },
  created() {
    this.getTasks();
  },
  beforeMount() {
    this.getTasks();
  },
  methods: {
    createTask() {
      this.$router.push('/tasks/create');
    },
    async getTasks() {
      const response = await fetch('http://localhost:5000/', {mode: 'cors'});
      const data = await response.json();
      this.tasksList = data;
    },
  },
};
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  