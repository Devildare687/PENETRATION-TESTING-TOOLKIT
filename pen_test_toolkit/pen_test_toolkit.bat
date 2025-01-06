@echo off
:: Check if Python is installed
python --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to the PATH.
    pause
    exit /b
)

:: Run the Penetration Testing Toolkit (main.py)
echo Running Penetration Testing Toolkit...
python main.py

:: Pause the terminal after the script completes
pause
