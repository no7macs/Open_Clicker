@echo off

timeout 1
echo Starting Build

set mypath=%cd%
echo %mypath%

timeout 2

copy "%mypath%\Data\Images\" "%mypath%\build\program\Data\Images\"
copy "%mypath%\Data\Hotkey\Hotkey.txt" "%mypath%\build\program\Data\Hotkey" 

timeout 2

timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/data/Hotkey --specpath ./build --noconfirm --clean ./Data/Hotkey/Hotkey/HotKey.pyw
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --noconfirm --clean ./Data/Settings/Settings/Settings.pyw
timeout 2 

pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --runtime-tmpdir ./Data/tmp --noconfirm --clean ./Data/Settings/Settings/Clear_tmp_data/Clear_tmp_data.pyw
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/ --specpath ./build --runtime-tmpdir ./Data/tmp --onefile --noconfirm --clean ./Open_Clicker.pyw
timeout 2

timeout 10
