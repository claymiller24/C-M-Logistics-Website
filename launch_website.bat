@echo off
REM Start Python HTTP server
start "C&M Logistics Website Server" /MIN python -m http.server 8000

REM Wait a moment for the server to start
timeout /t 2 /nobreak >nul

REM Open the website in default browser
start http://localhost:8000

echo Website launched! You can close this window to stop the server.
pause