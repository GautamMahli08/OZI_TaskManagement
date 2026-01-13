import React, { useState, useEffect } from 'react';
import {
  DndContext,
  DragOverlay,
  closestCorners,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import { arrayMove } from '@dnd-kit/sortable';
import KanbanColumn from './KanbanColumn';
import TaskCard from './TaskCard';
import taskService from '../../services/taskService';
import { getErrorMessage } from '../../utils/helpers';
import { Loader2, AlertCircle } from 'lucide-react';

const KanbanBoard = ({ onEditTask, onDeleteTask, refreshTrigger }) => {
  const [tasks, setTasks] = useState({
    pending: [],
    'in-progress': [],
    completed: [],
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [activeTask, setActiveTask] = useState(null);

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 8, // 8px of movement required to start drag
      },
    })
  );

  // Load tasks
  const loadTasks = async () => {
    try {
      setLoading(true);
      const groupedTasks = await taskService.getTasksGroupedByStatus();
      setTasks(groupedTasks);
      setError('');
    } catch (err) {
      setError(getErrorMessage(err));
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, [refreshTrigger]);

  const handleDragStart = (event) => {
    const { active } = event;
    // Find the task being dragged
    const task = Object.values(tasks)
      .flat()
      .find((t) => t._id === active.id);
    setActiveTask(task);
  };

  const handleDragOver = (event) => {
    const { active, over } = event;

    if (!over) return;

    const activeId = active.id;
    const overId = over.id;

    if (activeId === overId) return;

    // Find which columns the tasks are in
    const activeColumn = Object.keys(tasks).find((key) =>
      tasks[key].some((task) => task._id === activeId)
    );

    const overColumn =
      Object.keys(tasks).find((key) =>
        tasks[key].some((task) => task._id === overId)
      ) || overId; // overId might be a column id

    if (!activeColumn) return;

    // Moving within the same column or to a different column
    if (activeColumn !== overColumn) {
      setTasks((prev) => {
        const activeItems = prev[activeColumn];
        const overItems = prev[overColumn] || [];

        const activeIndex = activeItems.findIndex((t) => t._id === activeId);
        const overIndex = overItems.findIndex((t) => t._id === overId);

        let newOverItems;
        if (overId in prev) {
          // Dropped on column header
          newOverItems = [...overItems, activeItems[activeIndex]];
        } else {
          // Dropped on a task
          newOverItems = [
            ...overItems.slice(0, overIndex),
            activeItems[activeIndex],
            ...overItems.slice(overIndex),
          ];
        }

        return {
          ...prev,
          [activeColumn]: activeItems.filter((t) => t._id !== activeId),
          [overColumn]: newOverItems,
        };
      });
    }
  };

  const handleDragEnd = async (event) => {
    const { active, over } = event;
    setActiveTask(null);

    if (!over) return;

    const activeId = active.id;
    const overId = over.id;

    // Find which column the task ended up in
    const newColumn = Object.keys(tasks).find(
      (key) => tasks[key].some((task) => task._id === activeId) || key === overId
    );

    if (!newColumn) return;

    // Update task status on backend
    try {
      await taskService.updateTask(activeId, { status: newColumn });
      // Reload tasks to get fresh data
      await loadTasks();
    } catch (err) {
      alert('Failed to update task: ' + getErrorMessage(err));
      // Reload tasks to revert the change
      await loadTasks();
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <Loader2 className="w-12 h-12 text-primary-600 animate-spin mx-auto mb-4" />
          <p className="text-gray-600">Loading tasks...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="bg-red-50 border border-red-200 rounded-lg p-6 max-w-md">
          <div className="flex items-start gap-3">
            <AlertCircle className="w-6 h-6 text-red-600 flex-shrink-0" />
            <div>
              <h3 className="font-semibold text-red-900 mb-1">Error Loading Tasks</h3>
              <p className="text-red-700 text-sm">{error}</p>
              <button
                onClick={loadTasks}
                className="mt-3 text-sm text-red-600 hover:text-red-700 font-medium"
              >
                Try Again
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCorners}
      onDragStart={handleDragStart}
      onDragOver={handleDragOver}
      onDragEnd={handleDragEnd}
    >
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 h-full">
        <KanbanColumn
          status="pending"
          tasks={tasks.pending}
          onEdit={onEditTask}
          onDelete={onDeleteTask}
        />
        <KanbanColumn
          status="in-progress"
          tasks={tasks['in-progress']}
          onEdit={onEditTask}
          onDelete={onDeleteTask}
        />
        <KanbanColumn
          status="completed"
          tasks={tasks.completed}
          onEdit={onEditTask}
          onDelete={onDeleteTask}
        />
      </div>

      {/* Drag Overlay */}
      <DragOverlay>
        {activeTask ? (
          <div className="rotate-3 opacity-90">
            <TaskCard task={activeTask} onEdit={() => {}} onDelete={() => {}} />
          </div>
        ) : null}
      </DragOverlay>
    </DndContext>
  );
};

export default KanbanBoard;