@REM This script is used to create a standalone executable file for Winrate Tracker

@REM Create a standalone executable file for Winrate Tracker
@REM Path must be correct so that the db, etc can be accessed
echo Installing Winrate Tracker...
pyinstaller ..\src\winrate_tracker.py --distpath ..\ --workpath ..\build --specpath ..\app_spec --clean --name "Winrate Tracker" --log-level ERROR --onefile

@REM Create a db folder if it does not exist
@echo off
set "dbFolder=db"
if not exist "%dbFolder%" (
    mkdir "%dbFolder%"
    > "winrate.csv"
    echo Folder "%dbFolder%" created.
) else (
    echo Folder "%dbFolder%" already exists.
)

@REM Developer Mode so don't delete build and app_spec folders
if "%1"!="true" (
    rd /S /Q  ..\build
    rd /S /Q ..\app_spec
)

echo Press Enter to exit...
PAUSE