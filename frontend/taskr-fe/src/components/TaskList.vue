<script setup>
import TaskModal from './TaskModal.vue';
</script>

<template>
    <div class="mr-5 ml-5 text-right">
        <h6 class="mt-3 mb-3">{{ this.status }} Tasks</h6>
        <div class="mt-3 mb-3" v-for="task in tasks" :key="task.title">
          <b>{{ task.title }} </b>
          <button class="btn btn-primary ml-3" @click="openModal">View</button>
          <TaskModal :task="task" v-show="isModalVisible" @close="closeModal" />
        </div>
      </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tasks: [],
      };
    },
    beforeMount() {
      this.tasks = this.task_list.filter((task) => {return task.status === this.status});
    },
    created() {
      this.tasks = this.task_list.filter((task) => {return task.status === this.status});
    },
    methods: {
      openModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
    },
    props: {
      status: {
        type: String,
        required: true,
      },
      task_list: {
        type: Array,
        required: true,
      }
    }

  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  