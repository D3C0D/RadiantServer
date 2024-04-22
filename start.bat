@echo off
setlocal

:: Define the directory of the script and the virtual environment
set SCRIPT_DIR=%~dp0
set ENV_DIR=%SCRIPT_DIR%environment

:: Check if the Python script exists
if not exist "%SCRIPT_DIR%RadiantServer.py" (
    echo Error: RadiantServer.py not found in %SCRIPT_DIR%
    exit /b 1
)

:: Activate the virtual environment
call "%ENV_DIR%\Scripts\activate.bat" "%ENV_DIR%\myenv"

:: Execute the Python script
echo Running RadiantServer.py...
python "%SCRIPT_DIR%RadiantServer.py"

:: Deactivate the virtual environment
call conda deactivate

endlocal
