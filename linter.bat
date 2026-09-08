@echo off
setlocal ENABLEDELAYEDEXPANSION

set RUST_LOG_STYLE=always

echo ==========================================
echo Activating virtual environment...
echo ==========================================

if exist "%~dp0.venv\Scripts\activate.bat" (
    CALL "%~dp0.venv\Scripts\activate.bat"
) else (
    echo WARNING: VENV not found at "%~dp0.venv"
)

echo.
echo ==========================================
echo Running Ruff CHECK + FIX
echo ==========================================

ruff check . --fix
if %errorlevel% neq 0 (
    echo WARNING: Ruff CHECK returned issues.
)

echo.
echo ==========================================
echo Running Ruff FORMAT
echo ==========================================

ruff format .
if %errorlevel% neq 0 (
    echo WARNING: Ruff FORMAT returned issues.
)

echo.
echo ==========================================
echo Running Mypy
echo ==========================================

mypy .
if %errorlevel% neq 0 (
    echo WARNING: Mypy found type issues.
)

echo.
echo ==========================================
echo Linting Completed
echo ==========================================

endlocal
