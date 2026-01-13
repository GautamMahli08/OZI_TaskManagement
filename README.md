# 🚀 Task Management System (Kanban Based) – TaskFlow

TaskFlow is a **production-ready, full-stack Task Management System** built with a modern tech stack, featuring secure authentication, role-based access, a Kanban board with drag & drop, real-time CRUD operations, and email verification.  
The application is fully deployed on **AWS + MongoDB Atlas** and follows clean architecture and best practices.

🔗 **Live Demo:**  
http://taskmanagement-btech10294-22-mahli.s3-website.eu-north-1.amazonaws.com/dashboard


##  Workflow

<img width="732" height="292" alt="OZI drawio" src="https://github.com/user-attachments/assets/73f5924d-31c5-47f0-b49a-d588dfb42211" />

---


##  Architecture Diagram
<img width="592" height="262" alt="awsoo drawio" src="https://github.com/user-attachments/assets/16a638ed-ecef-4493-980a-ae788057f9f0" />


## 🎯 Key Features

### 🔐 Authentication & User Management
- User Registration  
- Login & Logout  
- Email Verification (Gmail SMTP)  
- JWT-based Authentication  
- Update & Delete Profile  
- Secure Protected Routes  

---

### 👥 Role-Based Access Control

**Admin**
- Can view and manage all users and tasks  

**User**
- Can manage only their own tasks  

---

### 🗂️ Task Management (CRUD)
- Create Task  
- Read Task (User-specific)  
- Update Task  
- Delete Task  
- Filter tasks by status (Pending / In Progress / Completed)  

---

### 🧩 Kanban Board
- Three Columns:
  - Pending
  - In Progress
  - Completed
- Drag & Drop Support (Desktop)
- Status automatically updates in backend

---

### 📧 Email Verification
- New users receive verification email
- Account becomes active only after verification

---

### 📱 Responsive Design
- Works on Desktop, Tablet, and Mobile
- Clean, minimal UI using Tailwind CSS

---

### ☁️ Production Ready
- Backend deployed on AWS EC2
- Frontend hosted on AWS S3 (Static Website)
- Database on MongoDB Atlas
- Environment variables managed securely
- Systemd service for backend (24/7 uptime)

---

## 🏗️ Tech Stack

| Layer        | Technology                                |
|--------------|-------------------------------------------|
| **Frontend** | React + Vite + Tailwind CSS               |
| **Backend**  | FastAPI + Python + Pydantic               |
| **Database** | MongoDB Atlas                             |
| **Auth**     | JWT + Email Verification                  |
| **Email**    | Gmail SMTP                                |
| **Hosting**  | AWS EC2, S3, CloudFront                   |
| **DevOps**   | Systemd, Nginx (optional), Docker (ready) |

---

## 🚀 Live Deployment

| Component       | URL                                                                                               | Status |
|-----------------|---------------------------------------------------------------------------------------------------|--------|
| **Frontend**    | http://taskmanagement-btech10294-22-mahli.s3-website.eu-north-1.amazonaws.com                     | ✅ Live |
| **Backend API** | http://13.51.156.213:8000/docs                                                                     | ✅ Live |
| **Database**    | MongoDB Atlas (task_management_db)                                                                 | ✅ Live |

⚠️ **Note for Mobile Users:**  
Use **http://** (not https://) in the browser address bar.


## 📁 Project Structure
```bash
task/
├── backend/
│   ├── app/
│   │   ├── api/           # API Routes (auth, tasks, users)
│   │   ├── core/          # Config, DB connection, Email setup
│   │   ├── models/        # Pydantic Schemas
│   │   ├── services/      # Business Logic
│   │   └── main.py        # FastAPI entry point
│   ├── .env               # Environment Variables
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── components/    # React Components (Navbar, Board, Cards)
    │   ├── services/      # API Calls (Axios)
    │   └── App.jsx
    ├── dist/              # Production Build (for S3)
    └── vite.config.js


## 🔧 Setup & Deployment Guide

### Backend (AWS EC2)

```bash
# 1. SSH into EC2
ssh -i taskflow-key.pem ubuntu@13.51.156.213

# 2. Go to backend directory
cd ~/taskflow-backend

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start backend service
sudo systemctl start taskflow-backend
sudo systemctl enable taskflow-backend

Environment Variables (.env)
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/task_management_db
DATABASE_NAME=task_management_db
FRONTEND_URL=http://taskmanagement-btech10294-22-mahli.s3-website.eu-north-1.amazonaws.com
CORS_ORIGINS=["http://taskmanagement-btech10294-22-mahli.s3-website.eu-north-1.amazonaws.com"]
MAIL_USERNAME=your@gmail.com
MAIL_PASSWORD=app-password


Frontend (AWS S3)
# 1. Build frontend
npm run build

# 2. Upload to S3
aws s3 sync dist/ s3://taskmanagement-btech10294-22-mahli --delete


S3 Bucket Settings
Block Public Access: OFF
Static Website Hosting: ON
Bucket Policy: Public Read Access


| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| POST   | /api/auth/register | User Registration  |
| POST   | /api/auth/login    | User Login         |
| GET    | /api/auth/verify   | Email Verification |
| GET    | /api/tasks         | Get All Tasks      |
| POST   | /api/tasks         | Create Task        |
| PUT    | /api/tasks/{id}    | Update Task        |
| DELETE | /api/tasks/{id}    | Delete Task        |


📄 Full API Docs:
👉 http://13.51.156.213:8000/docs


📱 Mobile Drag & Drop (Planned Enhancement)

Currently drag & drop works on desktop.
For mobile support, touch events can be added:

onTouchStart={handleTouchStart}
onTouchMove={handleTouchMove}
onTouchEnd={handleTouchEnd}


| Issue              | Solution                                      |
| ------------------ | --------------------------------------------- |
| S3 Access Denied   | Enable public access + update bucket policy   |
| CORS Error         | Update `CORS_ORIGINS` in backend `.env`       |
| Mobile not loading | Use `http://` not `https://`                  |
| Backend 404        | `sudo systemctl status taskflow-backend`      |
| MongoDB auth error | Ensure Atlas user has **Read and Write** role |

```

📸 Screenshots

## 1.Login Page
<img width="3258" height="1716" alt="taskmanagement-btech10294-22-mahli s3-website eu-north-1 amazonaws com_login (1)" src="https://github.com/user-attachments/assets/11cee652-c5a1-4c2c-9697-507428747ffd" />

## 2. Register Page
<img width="3258" height="1748" alt="taskmanagement-btech10294-22-mahli s3-website eu-north-1 amazonaws com_login (2)" src="https://github.com/user-attachments/assets/e7ae61e0-ad76-4866-8bff-b8bacdd1049d" />

## 3. Dashboard With Filter
<img width="3258" height="1782" alt="taskmanagement-btech10294-22-mahli s3-website eu-north-1 amazonaws com_login (3)" src="https://github.com/user-attachments/assets/8ceff47a-a4f8-463e-8748-68a48840d44b" />

## 4. Profile 
<img width="3258" height="1716" alt="taskmanagement-btech10294-22-mahli s3-website eu-north-1 amazonaws com_login (5)" src="https://github.com/user-attachments/assets/76303d65-af55-4100-9f5b-4b401ad272e1" />

## 5.Create Task
<img width="3258" height="1782" alt="taskmanagement-btech10294-22-mahli s3-website eu-north-1 amazonaws com_login (6)" src="https://github.com/user-attachments/assets/bc365e35-78fd-4d85-8775-bb911e3c9e95" />


## Author
## Gautam Kumar Mahli
## Roll Number: BTECH/10294/22





