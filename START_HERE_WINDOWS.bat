@echo off
cd /d "%~dp0"
echo Starting ReconIQ at http://127.0.0.1:8080
start "" "http://127.0.0.1:8080"
py app\server.py
if errorlevel 1 python app\server.py
pause
