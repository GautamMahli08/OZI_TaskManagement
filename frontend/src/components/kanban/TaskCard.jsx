import React from 'react';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { Calendar, Clock, Edit2, Trash2, GripVertical } from 'lucide-react';
import { formatDate } from '../../utils/helpers';

const TaskCard = ({ task, onEdit, onDelete }) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: task._id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.5 : 1,
  };

  // Determine if task is overdue
  const isOverdue = task.due_date && new Date(task.due_date) < new Date() && task.status !== 'completed';

  return (
    <div
      ref={setNodeRef}
      style={style}
      className={`bg-white rounded-lg shadow-sm border-2 hover:shadow-md transition-all duration-200 ${
        isDragging ? 'border-primary-400 shadow-lg' : 'border-gray-200'
      }`}
    >
      {/* Drag Handle */}
      <div
        {...attributes}
        {...listeners}
        className="px-4 pt-3 pb-2 cursor-grab active:cursor-grabbing flex items-start gap-2"
      >
        <GripVertical className="w-5 h-5 text-gray-400 flex-shrink-0 mt-1" />
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-gray-900 mb-1 break-words">{task.title}</h3>
          {task.description && (
            <p className="text-sm text-gray-600 line-clamp-2 break-words">{task.description}</p>
          )}
        </div>
      </div>

      {/* Task Info & Actions */}
      <div className="px-4 pb-3 space-y-2">
        {task.due_date && (
          <div className={`flex items-center gap-2 text-xs ${isOverdue ? 'text-red-600' : 'text-gray-500'}`}>
            <Calendar className="w-4 h-4" />
            <span className="font-medium">{formatDate(task.due_date)}</span>
          </div>
        )}

        {/* Action Buttons */}
        <div className="flex items-center gap-2 pt-2 border-t border-gray-100">
          <button
            onClick={() => onEdit(task)}
            className="flex-1 flex items-center justify-center gap-1 px-3 py-1.5 text-sm text-blue-600 hover:bg-blue-50 rounded transition-colors"
          >
            <Edit2 className="w-4 h-4" />
            Edit
          </button>
          <button
            onClick={() => onDelete(task)}
            className="flex-1 flex items-center justify-center gap-1 px-3 py-1.5 text-sm text-red-600 hover:bg-red-50 rounded transition-colors"
          >
            <Trash2 className="w-4 h-4" />
            Delete
          </button>
        </div>
      </div>
    </div>
  );
};

export default TaskCard;