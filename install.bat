@echo off
cls

echo Installing Miniconda and setting up a Python environment locally.

set "ROOT_DIR=%~dp0"
set "ENV_DIR=%ROOT_DIR%environment"
set "MINICONDA_INSTALLER=Miniconda3-latest-Windows-x86_64.exe"
set "MINICONDA_URL=https://repo.anaconda.com/miniconda/%MINICONDA_INSTALLER%"

echo ROOT_DIR is set to %ROOT_DIR%
cd /D %ROOT_DIR%

if not exist "%ENV_DIR%" mkdir "%ENV_DIR%"

if not exist "%MINICONDA_INSTALLER%" (
    echo Downloading Miniconda...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%MINICONDA_URL%', '%MINICONDA_INSTALLER%')"
)

echo Installing Miniconda...
start /wait "" %MINICONDA_INSTALLER% /InstallationType=JustMe /RegisterPython=0 /AddToPath=0 /NoRegistry=1 /S /D=%ENV_DIR%
del /F /Q %MINICONDA_INSTALLER%

echo Setting up environment variables to use local Miniconda...
SET "PATH=%ENV_DIR%\Scripts;%ENV_DIR%\Library\bin;%ENV_DIR%\bin;%PATH%"
SET "CONDA_PREFIX=%ENV_DIR%"
SET "CONDA_SHLVL=0"

echo Creating a new Conda environment...
call conda create --prefix "%ENV_DIR%\myenv" python=3 -y

echo Miniconda and environment setup complete, use the start.bat to run the server.
pause
