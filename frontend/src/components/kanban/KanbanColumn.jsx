import React from 'react';
import { useDroppable } from '@dnd-kit/core';
import { SortableContext, verticalListSortingStrategy } from '@dnd-kit/sortable';
import TaskCard from './TaskCard';
import { getStatusDisplayName } from '../../utils/helpers';

const KanbanColumn = ({ status, tasks, onEdit, onDelete }) => {
  const { setNodeRef, isOver } = useDroppable({
    id: status,
  });

  const columnColors = {
    pending: 'bg-yellow-50 border-yellow-200',
    'in-progress': 'bg-blue-50 border-blue-200',
    completed: 'bg-green-50 border-green-200',
  };

  const headerColors = {
    pending: 'bg-yellow-500',
    'in-progress': 'bg-blue-500',
    completed: 'bg-green-500',
  };

  return (
    <div className="flex flex-col h-full">
      {/* Column Header */}
      <div className={`${headerColors[status]} text-white px-4 py-3 rounded-t-lg`}>
        <div className="flex items-center justify-between">
          <h2 className="font-semibold text-lg">{getStatusDisplayName(status)}</h2>
          <span className="bg-white bg-opacity-30 px-2 py-1 rounded-full text-sm font-medium">
            {tasks.length}
          </span>
        </div>
      </div>

      {/* Droppable Area */}
      <div
        ref={setNodeRef}
        className={`flex-1 p-4 space-y-3 rounded-b-lg border-2 transition-colors ${
          columnColors[status]
        } ${isOver ? 'border-primary-500 bg-primary-50' : ''}`}
        style={{ minHeight: '500px' }}
      >
        <SortableContext items={tasks.map(t => t._id)} strategy={verticalListSortingStrategy}>
          {tasks.length === 0 ? (
            <div className="flex items-center justify-center h-full">
              <p className="text-gray-400 text-sm">No tasks</p>
            </div>
          ) : (
            tasks.map((task) => (
              <TaskCard
                key={task._id}
                task={task}
                onEdit={onEdit}
                onDelete={onDelete}
              />
            ))
          )}
        </SortableContext>
      </div>
    </div>
  );
};

export default KanbanColumn;