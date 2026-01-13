import api from "./api";

const taskService = {
  // Get all tasks
  getTasks: async (status = null) => {
    const url = status ? `/tasks?status=${status}` : "/tasks";
    const response = await api.get(url);
    return response.data;
  },

  // Get single task by ID
  getTaskById: async (taskId) => {
    const response = await api.get(`/tasks/${taskId}`);
    return response.data;
  },

  // Create new task
  createTask: async (taskData) => {
    const response = await api.post("/tasks", taskData);
    return response.data;
  },

  // Update task
  updateTask: async (taskId, taskData) => {
    const response = await api.put(`/tasks/${taskId}`, taskData);
    return response.data;
  },

  // Delete task
  deleteTask: async (taskId) => {
    const response = await api.delete(`/tasks/${taskId}`);
    return response.data;
  },

  // Get tasks grouped by status (for Kanban board)
  getTasksGroupedByStatus: async () => {
    const tasks = await taskService.getTasks();

    return {
      pending: tasks.filter((task) => task.status === "pending"),
      "in-progress": tasks.filter((task) => task.status === "in-progress"),
      completed: tasks.filter((task) => task.status === "completed"),
    };
  },
};

export default taskService;
