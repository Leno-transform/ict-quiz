@echo off
setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
echo ============================================================
echo  ICT mobile (static) server  --  port 8876
echo  Keep this window open. Close it to stop the server.
echo ============================================================
echo.
echo  Phone must be on the SAME Wi-Fi as this computer.
echo.

set "PY="
if exist "%USERPROFILE%\miniconda3\python.exe" set "PY=%USERPROFILE%\miniconda3\python.exe"
if not defined PY if exist "%USERPROFILE%\anaconda3\python.exe" set "PY=%USERPROFILE%\anaconda3\python.exe"
if not defined PY (
  py -3 -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul
  if not errorlevel 1 set "PY=py -3"
)
if not defined PY (
  python -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul
  if not errorlevel 1 set "PY=python"
)
if not defined PY (
  echo Python 3.10 or newer was not found.
  pause
  exit /b 1
)

"%PY%" -c "import socket;s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.settimeout(2);s.connect(('8.8.8.8',80));ip=s.getsockname()[0];s.close();print('  Phone entry :  http://%s:8876/mobile.html'%ip);print('  Practice page:  http://%s:8876/index.html'%ip)"
echo.
echo  If the phone cannot open it, allow Python through Windows Firewall
echo  for private networks, or check that both devices share one Wi-Fi.
echo.
echo  Serves mobile-site\dist (the ready-to-host site), not the whole project.
echo.
"%PY%" -m http.server 8876 --bind 0.0.0.0 --directory "%~dp0mobile-site\dist"
if not errorlevel 1 exit /b 0
echo.
echo Startup failed. Port 8876 may already be in use.
pause
exit /b 1
