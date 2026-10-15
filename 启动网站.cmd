@echo off
setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
echo Starting ICT Practice. Keep this window open.
echo Website: http://127.0.0.1:8765
echo.
if exist "%USERPROFILE%\miniconda3\python.exe" (
  "%USERPROFILE%\miniconda3\python.exe" "%~dp0app.py" %*
  goto finished
)
if exist "%USERPROFILE%\anaconda3\python.exe" (
  "%USERPROFILE%\anaconda3\python.exe" "%~dp0app.py" %*
  goto finished
)
py -3 -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul
if not errorlevel 1 (
  py -3 "%~dp0app.py" %*
  goto finished
)
python -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul
if not errorlevel 1 (
  python "%~dp0app.py" %*
  goto finished
)
echo Python 3.10 or newer was not found.
echo Install Python or Miniconda, then try again.
pause
exit /b 1
:finished
if not errorlevel 1 exit /b 0
echo.
echo Startup failed. Please keep this message for troubleshooting.
pause
exit /b 1
