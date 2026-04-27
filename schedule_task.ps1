$TaskName = "Daily Weekly Priorities Email"
$TaskDescription = "Pull Outlook calendar and draft weekly priorities email at 9:30 AM"
$ScriptPath = "C:\Users\KrishnaSiram\Desktop\BAAgents Krishna Siram\pull_calendar_draft_email.py"
$PythonPath = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"

# Task trigger: Daily at 9:30 AM
$Trigger = New-ScheduledTaskTrigger -Daily -At 09:30

# Action: Run Python script
$Action = New-ScheduledTaskAction `
    -Execute $PythonPath `
    -Argument "`"$ScriptPath`"" `
    -WorkingDirectory "C:\Users\KrishnaSiram\Desktop\BAAgents Krishna Siram"

# Settings: Run with highest privileges, allow on-demand runs
$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable

# Register the task
Register-ScheduledTask `
    -TaskName $TaskName `
    -Description $TaskDescription `
    -Trigger $Trigger `
    -Action $Action `
    -Settings $Settings `
    -RunLevel Highest `
    -Force

Write-Host "✓ Task scheduled successfully!"
Write-Host "   Task: $TaskName"
Write-Host "   Time: 09:30 AM daily"
Write-Host "   Script: $ScriptPath"
