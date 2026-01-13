@echo off
echo =====================================
echo COPYING FRONTEND FILES
echo =====================================
echo.

set SOURCE_DIR=C:\Users\gauta\OneDrive\Desktop\OZI
set DEST_DIR=C:\Users\gauta\OneDrive\Desktop\OZI\frontend

echo Creating directories...
mkdir "%DEST_DIR%\src\contexts" 2>nul
mkdir "%DEST_DIR%\src\pages" 2>nul
mkdir "%DEST_DIR%\src\services" 2>nul
mkdir "%DEST_DIR%\src\utils" 2>nul
mkdir "%DEST_DIR%\src\components\auth" 2>nul
mkdir "%DEST_DIR%\src\components\kanban" 2>nul
mkdir "%DEST_DIR%\src\components\layout" 2>nul
mkdir "%DEST_DIR%\src\components\modals" 2>nul

echo.
echo Copying files...
echo.

REM Root files
copy "%SOURCE_DIR%\FRONTEND_package.json" "%DEST_DIR%\package.json" >nul 2>&1 && echo [OK] package.json || echo [FAIL] package.json
copy "%SOURCE_DIR%\FRONTEND_vite.config.js" "%DEST_DIR%\vite.config.js" >nul 2>&1 && echo [OK] vite.config.js || echo [FAIL] vite.config.js
copy "%SOURCE_DIR%\FRONTEND_tailwind.config.js" "%DEST_DIR%\tailwind.config.js" >nul 2>&1 && echo [OK] tailwind.config.js || echo [FAIL] tailwind.config.js
copy "%SOURCE_DIR%\FRONTEND_index.html" "%DEST_DIR%\index.html" >nul 2>&1 && echo [OK] index.html || echo [FAIL] index.html

REM Src root
copy "%SOURCE_DIR%\FRONTEND_src_index.css" "%DEST_DIR%\src\index.css" >nul 2>&1 && echo [OK] src/index.css || echo [FAIL] src/index.css
copy "%SOURCE_DIR%\FRONTEND_src_main.jsx" "%DEST_DIR%\src\main.jsx" >nul 2>&1 && echo [OK] src/main.jsx || echo [FAIL] src/main.jsx
copy "%SOURCE_DIR%\FRONTEND_src_App.jsx" "%DEST_DIR%\src\App.jsx" >nul 2>&1 && echo [OK] src/App.jsx || echo [FAIL] src/App.jsx

REM Contexts
copy "%SOURCE_DIR%\FRONTEND_src_contexts_AuthContext.jsx" "%DEST_DIR%\src\contexts\AuthContext.jsx" >nul 2>&1 && echo [OK] contexts/AuthContext.jsx || echo [FAIL] contexts/AuthContext.jsx

REM Services
copy "%SOURCE_DIR%\FRONTEND_src_services_api.js" "%DEST_DIR%\src\services\api.js" >nul 2>&1 && echo [OK] services/api.js || echo [FAIL] services/api.js
copy "%SOURCE_DIR%\FRONTEND_src_services_authService.js" "%DEST_DIR%\src\services\authService.js" >nul 2>&1 && echo [OK] services/authService.js || echo [FAIL] services/authService.js
copy "%SOURCE_DIR%\FRONTEND_src_services_taskService.js" "%DEST_DIR%\src\services\taskService.js" >nul 2>&1 && echo [OK] services/taskService.js || echo [FAIL] services/taskService.js

REM Utils
copy "%SOURCE_DIR%\FRONTEND_src_utils_helpers.js" "%DEST_DIR%\src\utils\helpers.js" >nul 2>&1 && echo [OK] utils/helpers.js || echo [FAIL] utils/helpers.js

REM Pages
copy "%SOURCE_DIR%\FRONTEND_src_pages_LoginPage.jsx" "%DEST_DIR%\src\pages\LoginPage.jsx" >nul 2>&1 && echo [OK] pages/LoginPage.jsx || echo [FAIL] pages/LoginPage.jsx
copy "%SOURCE_DIR%\FRONTEND_src_pages_RegisterPage.jsx" "%DEST_DIR%\src\pages\RegisterPage.jsx" >nul 2>&1 && echo [OK] pages/RegisterPage.jsx || echo [FAIL] pages/RegisterPage.jsx
copy "%SOURCE_DIR%\FRONTEND_src_pages_VerifyEmailPage.jsx" "%DEST_DIR%\src\pages\VerifyEmailPage.jsx" >nul 2>&1 && echo [OK] pages/VerifyEmailPage.jsx || echo [FAIL] pages/VerifyEmailPage.jsx
copy "%SOURCE_DIR%\FRONTEND_src_pages_DashboardPage.jsx" "%DEST_DIR%\src\pages\DashboardPage.jsx" >nul 2>&1 && echo [OK] pages/DashboardPage.jsx || echo [FAIL] pages/DashboardPage.jsx
copy "%SOURCE_DIR%\FRONTEND_src_pages_ProfilePage.jsx" "%DEST_DIR%\src\pages\ProfilePage.jsx" >nul 2>&1 && echo [OK] pages/ProfilePage.jsx || echo [FAIL] pages/ProfilePage.jsx

REM Components - Auth
copy "%SOURCE_DIR%\FRONTEND_src_components_auth_LoginForm.jsx" "%DEST_DIR%\src\components\auth\LoginForm.jsx" >nul 2>&1 && echo [OK] components/auth/LoginForm.jsx || echo [FAIL] components/auth/LoginForm.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_auth_RegisterForm.jsx" "%DEST_DIR%\src\components\auth\RegisterForm.jsx" >nul 2>&1 && echo [OK] components/auth/RegisterForm.jsx || echo [FAIL] components/auth/RegisterForm.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_auth_VerifyEmail.jsx" "%DEST_DIR%\src\components\auth\VerifyEmail.jsx" >nul 2>&1 && echo [OK] components/auth/VerifyEmail.jsx || echo [FAIL] components/auth/VerifyEmail.jsx

REM Components - Kanban
copy "%SOURCE_DIR%\FRONTEND_src_components_kanban_KanbanBoard.jsx" "%DEST_DIR%\src\components\kanban\KanbanBoard.jsx" >nul 2>&1 && echo [OK] components/kanban/KanbanBoard.jsx || echo [FAIL] components/kanban/KanbanBoard.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_kanban_KanbanColumn.jsx" "%DEST_DIR%\src\components\kanban\KanbanColumn.jsx" >nul 2>&1 && echo [OK] components/kanban/KanbanColumn.jsx || echo [FAIL] components/kanban/KanbanColumn.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_kanban_TaskCard.jsx" "%DEST_DIR%\src\components\kanban\TaskCard.jsx" >nul 2>&1 && echo [OK] components/kanban/TaskCard.jsx || echo [FAIL] components/kanban/TaskCard.jsx

REM Components - Layout
copy "%SOURCE_DIR%\FRONTEND_src_components_layout_Navbar.jsx" "%DEST_DIR%\src\components\layout\Navbar.jsx" >nul 2>&1 && echo [OK] components/layout/Navbar.jsx || echo [FAIL] components/layout/Navbar.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_layout_ProtectedRoute.jsx" "%DEST_DIR%\src\components\layout\ProtectedRoute.jsx" >nul 2>&1 && echo [OK] components/layout/ProtectedRoute.jsx || echo [FAIL] components/layout/ProtectedRoute.jsx

REM Components - Modals
copy "%SOURCE_DIR%\FRONTEND_src_components_modals_CreateTaskModal.jsx" "%DEST_DIR%\src\components\modals\CreateTaskModal.jsx" >nul 2>&1 && echo [OK] components/modals/CreateTaskModal.jsx || echo [FAIL] components/modals/CreateTaskModal.jsx
copy "%SOURCE_DIR%\FRONTEND_src_components_modals_EditTaskModal.jsx" "%DEST_DIR%\src\components\modals\EditTaskModal.jsx" >nul 2>&1 && echo [OK] components/modals/EditTaskModal.jsx || echo [FAIL] components/modals/EditTaskModal.jsx

echo.
echo =====================================
echo COMPLETE!
echo =====================================
echo.
echo Next steps:
echo 1. Stop Vite server (Ctrl+C)
echo 2. Delete cache: rmdir /s /q frontend\node_modules\.vite
echo 3. Restart: cd frontend ^&^& npm run dev
echo.
pause
