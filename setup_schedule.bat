@echo off
REM Run this file as Administrator
REM Right-click and select "Run as administrator"

setlocal enabledelayedexpansion

set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
set SCRIPT_PATH=C:\Users\KrishnaSiram\Desktop\BAAgents Krishna Siram\pull_calendar_draft_email.py
set WORK_DIR=C:\Users\KrishnaSiram\Desktop\BAAgents Krishna Siram

powershell -ExecutionPolicy Bypass -Command ^
  "$Trigger = New-ScheduledTaskTrigger -Daily -At 09:30; " ^
  "$Action = New-ScheduledTaskAction -Execute '!PYTHON_PATH!' -Argument '\"!SCRIPT_PATH!\"' -WorkingDirectory '!WORK_DIR!'; " ^
  "$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable; " ^
  "Register-ScheduledTask -TaskName 'Daily Weekly Priorities Email' -Description 'Pull Outlook calendar and draft weekly priorities email' -Trigger $Trigger -Action $Action -Settings $Settings -RunLevel Highest -Force; " ^
  "Write-Host 'Task registered successfully!'"

pause
