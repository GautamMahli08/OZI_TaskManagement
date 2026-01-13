import React, { useState } from 'react';
import Navbar from '../components/layout/Navbar';
import KanbanBoard from '../components/kanban/KanbanBoard';
import CreateTaskModal from '../components/modals/CreateTaskModal';
import EditTaskModal from '../components/modals/EditTaskModal';
import { Plus, AlertCircle, Mail } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import authService from '../services/authService';
import taskService from '../services/taskService';
import { getErrorMessage } from '../utils/helpers';

const DashboardPage = () => {
  const { user } = useAuth();
  const [createModalOpen, setCreateModalOpen] = useState(false);
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);
  const [refreshTrigger, setRefreshTrigger] = useState(0);
  const [resendLoading, setResendLoading] = useState(false);
  const [showVerificationBanner, setShowVerificationBanner] = useState(true);

  const handleTaskCreated = () => {
    setRefreshTrigger(prev => prev + 1);
  };

  const handleTaskUpdated = () => {
    setRefreshTrigger(prev => prev + 1);
  };

  const handleEditTask = (task) => {
    setSelectedTask(task);
    setEditModalOpen(true);
  };

  const handleDeleteTask = async (task) => {
    if (window.confirm(`Are you sure you want to delete "${task.title}"?`)) {
      try {
        await taskService.deleteTask(task._id);
        setRefreshTrigger(prev => prev + 1);
      } catch (err) {
        alert('Failed to delete task: ' + getErrorMessage(err));
      }
    }
  };

  const handleResendVerification = async () => {
    setResendLoading(true);
    try {
      await authService.resendVerification(user.email);
      alert('Verification email sent! Please check your inbox.');
    } catch (err) {
      alert('Failed to send email: ' + getErrorMessage(err));
    } finally {
      setResendLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Email Verification Banner */}
      {user && !user.is_verified && showVerificationBanner && (
        <div className="bg-yellow-50 border-b border-yellow-200">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div className="flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" />
              <div className="flex-1">
                <p className="text-sm text-yellow-800">
                  <strong>Email not verified.</strong> Please check your inbox for the verification link.
                </p>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={handleResendVerification}
                  disabled={resendLoading}
                  className="text-sm text-yellow-800 hover:text-yellow-900 font-medium disabled:opacity-50 flex items-center gap-1"
                >
                  <Mail className="w-4 h-4" />
                  {resendLoading ? 'Sending...' : 'Resend'}
                </button>
                <button
                  onClick={() => setShowVerificationBanner(false)}
                  className="text-yellow-600 hover:text-yellow-800"
                >
                  <Plus className="w-5 h-5 rotate-45" />
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Task Dashboard</h1>
            <p className="text-gray-600 mt-1">Manage your tasks with drag and drop</p>
          </div>
          <button
            onClick={() => setCreateModalOpen(true)}
            className="btn-primary flex items-center gap-2"
          >
            <Plus className="w-5 h-5" />
            New Task
          </button>
        </div>

        {/* Kanban Board */}
        <KanbanBoard
          onEditTask={handleEditTask}
          onDeleteTask={handleDeleteTask}
          refreshTrigger={refreshTrigger}
        />
      </div>

      {/* Modals */}
      <CreateTaskModal
        isOpen={createModalOpen}
        onClose={() => setCreateModalOpen(false)}
        onTaskCreated={handleTaskCreated}
      />

      <EditTaskModal
        isOpen={editModalOpen}
        onClose={() => setEditModalOpen(false)}
        task={selectedTask}
        onTaskUpdated={handleTaskUpdated}
      />
    </div>
  );
};

export default DashboardPage;