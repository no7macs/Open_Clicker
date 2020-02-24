@echo off

timeout 1
echo Starting Build

set mypath=%cd%
echo %mypath%

timeout 2

copy "%mypath%\Data\Images\" "%mypath%\build\program\Data\Images\"
copy "%mypath%\Data\Hotkey\Hotkey.txt" "%mypath%\build\program\Data\Hotkey.txt" 

timeout 2

timeout 2

REM pyinstaller --workpath ./build/working --distpath ./build/program/data --specpath ./build --noconfirm --clean ./HotKey.pyw
timeout 2

REM pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --noconfirm --clean ./Data/Settings/Settings/Settings.pyw
timeout 2 

REM pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --runtime-tmpdir ./Data/tmp --noconfirm --clean ./Data/Settings/Settings/Clear_tmp_data/Clear_tmp_data.pyw
timeout 2

rem pyinstaller --workpath ./build/working --distpath ./build/program --specpath ./build --noconfirm --clean --onefile ./Data/main/Open_Clicker.pyw
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program --specpath ./build --noconfirm --clean --onefile ./Updater.pyw

timeout 10
