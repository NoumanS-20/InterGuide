' InterGuide Launcher
' This launches the application with error handling

Set objShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Change to the script directory
objShell.CurrentDirectory = scriptDir

' Run Python with startup script (window visible)
Dim result
result = objShell.Run("cmd /k python startup.py", 1, False)

Set objShell = Nothing
Set fso = Nothing
