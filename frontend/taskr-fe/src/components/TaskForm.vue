<template>
    <div class="modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h3>Create Task</h3>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addTask">
                <label for="title">Title:</label>
                <input v-model="newTask.title" required />
                <label for="description">Description:</label>
                <textarea v-model="newTask.description" required></textarea>
                <label for="status">Status:</label>
                <select v-model="newTask.status" required>
                <option value="open">Open</option>
                <option value="testing">Testing</option>
                <option value="done">Done</option>
                </select>
                <button type="submit">Add Task</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newTask: {
          title: "",
          description: "",
          status: "open",
        },
      };
    },
    methods: {
      addTask() {
        this.$emit("addTask", { ...this.newTask });
        this.newTask = {
          title: "",
          description: "",
          status: "open",
        };
      },
    },
  };
  </script>

  