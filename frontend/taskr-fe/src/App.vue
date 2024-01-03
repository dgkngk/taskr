<script setup>
import { RouterLink, RouterView } from 'vue-router'
import TaskList from './components/TaskList.vue';
</script>

<template>
  <header>
    <div class="mt-9 mb-3 text-right">
      <h3 class="mt-9 mb-3 text-center justify-content-space-between">
        Taskr
      </h3>
      <button @click="createTask" class="btn btn-primary">
        Create Task
      </button>
    </div>
  </header>
  <RouterView />
</template>

