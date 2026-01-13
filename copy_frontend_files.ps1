# PowerShell script to copy all frontend files
$ErrorActionPreference = "Stop"

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "COPYING FRONTEND FILES" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

$sourceDir = "C:\Users\gauta\OneDrive\Desktop\OZI"
$destDir = "C:\Users\gauta\OneDrive\Desktop\OZI\frontend"

# Create all required directories
Write-Host "`nCreating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$destDir\src\contexts" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\pages" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\services" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\utils" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\components\auth" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\components\kanban" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\components\layout" | Out-Null
New-Item -ItemType Directory -Force -Path "$destDir\src\components\modals" | Out-Null

# File mapping
$fileMap = @{
    # Root files
    "FRONTEND_package.json" = "package.json"
    "FRONTEND_vite.config.js" = "vite.config.js"
    "FRONTEND_tailwind.config.js" = "tailwind.config.js"
    "FRONTEND_index.html" = "index.html"

    # Src root files
    "FRONTEND_src_index.css" = "src\index.css"
    "FRONTEND_src_main.jsx" = "src\main.jsx"
    "FRONTEND_src_App.jsx" = "src\App.jsx"

    # Contexts
    "FRONTEND_src_contexts_AuthContext.jsx" = "src\contexts\AuthContext.jsx"

    # Services
    "FRONTEND_src_services_api.js" = "src\services\api.js"
    "FRONTEND_src_services_authService.js" = "src\services\authService.js"
    "FRONTEND_src_services_taskService.js" = "src\services\taskService.js"

    # Utils
    "FRONTEND_src_utils_helpers.js" = "src\utils\helpers.js"

    # Pages
    "FRONTEND_src_pages_LoginPage.jsx" = "src\pages\LoginPage.jsx"
    "FRONTEND_src_pages_RegisterPage.jsx" = "src\pages\RegisterPage.jsx"
    "FRONTEND_src_pages_VerifyEmailPage.jsx" = "src\pages\VerifyEmailPage.jsx"
    "FRONTEND_src_pages_DashboardPage.jsx" = "src\pages\DashboardPage.jsx"
    "FRONTEND_src_pages_ProfilePage.jsx" = "src\pages\ProfilePage.jsx"

    # Components - Auth
    "FRONTEND_src_components_auth_LoginForm.jsx" = "src\components\auth\LoginForm.jsx"
    "FRONTEND_src_components_auth_RegisterForm.jsx" = "src\components\auth\RegisterForm.jsx"
    "FRONTEND_src_components_auth_VerifyEmail.jsx" = "src\components\auth\VerifyEmail.jsx"

    # Components - Kanban
    "FRONTEND_src_components_kanban_KanbanBoard.jsx" = "src\components\kanban\KanbanBoard.jsx"
    "FRONTEND_src_components_kanban_KanbanColumn.jsx" = "src\components\kanban\KanbanColumn.jsx"
    "FRONTEND_src_components_kanban_TaskCard.jsx" = "src\components\kanban\TaskCard.jsx"

    # Components - Layout
    "FRONTEND_src_components_layout_Navbar.jsx" = "src\components\layout\Navbar.jsx"
    "FRONTEND_src_components_layout_ProtectedRoute.jsx" = "src\components\layout\ProtectedRoute.jsx"

    # Components - Modals
    "FRONTEND_src_components_modals_CreateTaskModal.jsx" = "src\components\modals\CreateTaskModal.jsx"
    "FRONTEND_src_components_modals_EditTaskModal.jsx" = "src\components\modals\EditTaskModal.jsx"
}

Write-Host "`nCopying files..." -ForegroundColor Yellow
$copied = 0
$errors = 0

foreach ($source in $fileMap.Keys) {
    $sourcePath = Join-Path $sourceDir $source
    $destPath = Join-Path $destDir $fileMap[$source]

    if (Test-Path $sourcePath) {
        try {
            Copy-Item -Path $sourcePath -Destination $destPath -Force
            Write-Host "✓ Copied: $($fileMap[$source])" -ForegroundColor Green
            $copied++
        } catch {
            Write-Host "✗ Error copying: $($fileMap[$source])" -ForegroundColor Red
            Write-Host "  $_" -ForegroundColor Red
            $errors++
        }
    } else {
        Write-Host "✗ Source not found: $source" -ForegroundColor Red
        $errors++
    }
}

Write-Host "`n=====================================" -ForegroundColor Cyan
Write-Host "SUMMARY" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "Files copied: $copied" -ForegroundColor Green
Write-Host "Errors: $errors" -ForegroundColor $(if ($errors -eq 0) { "Green" } else { "Red" })

if ($errors -eq 0) {
    Write-Host "`n✓ All files copied successfully!" -ForegroundColor Green
    Write-Host "`nNext steps:" -ForegroundColor Yellow
    Write-Host "1. Stop Vite server (Ctrl+C)" -ForegroundColor White
    Write-Host "2. Delete cache: Remove-Item -Recurse -Force node_modules\.vite" -ForegroundColor White
    Write-Host "3. Restart: npm run dev" -ForegroundColor White
} else {
    Write-Host "`n⚠ Some files failed to copy. Check errors above." -ForegroundColor Yellow
}

Write-Host "`nPress any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
