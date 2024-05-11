@REM This script is used to create a standalone executable file for Winrate Tracker

@REM Create a standalone executable file for Winrate Tracker
@REM Path must be correct so that the db, etc can be accessed
echo Installing Winrate Tracker...
set "basepath=%~dp0..\Winrate Tracker"
@REM TODO do away with the warning
pyinstaller ..\src\winrate_tracker.py --distpath "%basepath%" --workpath ..\build --specpath ..\app_spec --clean --name "Winrate Tracker" --log-level ERROR --onefile

@REM Create a db folder if it does not exist
@echo off
set "dbFolder=db"
if not exist "%basepath%\%dbFolder%" (
    mkdir "%basepath%\%dbFolder%"
    echo map,wins,losses> "%basepath%\%dbFolder%\winrate.csv"
    echo Folder "%dbFolder%" created.
) else (
    echo Folder "%dbFolder%" already exists.
)

@REM Add the etl columns (so that we can remove)
python ..\src\etl\perform_etl.py

@REM Developer Mode so don't delete build and app_spec folders
if not "%1"=="true" (
    rd /S /Q %~dp0..\build
    rd /S /Q %~dp0..\app_spec
)

PAUSE