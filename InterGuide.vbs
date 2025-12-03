' InterGuide Launcher (Silent VBScript)
' This launches the application without showing a command prompt window

Set objShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Change to the script directory and run Python
objShell.CurrentDirectory = scriptDir
objShell.Run "python main.py", 0, False

Set objShell = Nothing
Set fso = Nothing
