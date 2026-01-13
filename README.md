Task Management System (Kanban Based)

TaskFlow is a production-ready, full-stack Task Management System built with a modern tech stack, featuring secure authentication, role-based access, a Kanban board with drag & drop, real-time CRUD operations, and email verification.
The application is fully deployed on AWS + MongoDB Atlas and follows clean architecture and best practices.

🎯 Key Features
🔐 Authentication & User Management

User Registration

Login & Logout

Email Verification (Gmail SMTP)

JWT-based authentication

Update & Delete Profile

Secure protected routes

👥 Role-Based Access Control

Admin

Can view and manage all users and tasks

User

Can manage only their own tasks

🗂️ Task Management (CRUD)

Create Task

Read Task (User-specific)

Update Task

Delete Task

Filter tasks by status (Pending / In Progress / Completed)

🧩 Kanban Board

Three columns:

Pending

In Progress

Completed

Drag & Drop support (Desktop)

Status automatically updates in backend

📧 Email Verification

New users receive verification email

Account becomes active only after verification

📱 Responsive Design

Works on Desktop, Tablet, and Mobile

Clean, minimal UI using Tailwind CSS

☁️ Production Ready

Backend deployed on AWS EC2

Frontend hosted on AWS S3 (Static Website)

Database on MongoDB Atlas

Environment variables managed securely

Systemd service for backend (24/7 uptime)
