import { createRouter, createWebHistory } from 'vue-router'
import TaskListView from '../views/TaskListView.vue';
import TaskForm from '../components/TaskForm.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/tasks/create', component: TaskForm },
    { path: '/', component: TaskListView },
  ]
})

export default router
