@echo off

timeout 1
echo Starting Build

set mypath=%cd%
echo %mypath%

timeout 2

copy "%mypath%\Data\Images\" "%mypath%\build\program\Data\Images\"
copy "%mypath%\Data\Register\" "%mypath%\build\program\Data\Register\"
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/data/Hotkey --specpath ./build --ascii --noconfirm --clean ./Data/Hotkey/HotKey.pyw
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --ascii --noconfirm --clean ./Data/Settings/Settings.pyw
timeout 2 

pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --runtime-tmpdir ./Data/tmp --ascii --noupx --noconfirm --clean ./Data/Settings/Clear_tmp_data.pyw
timeout 2

pyinstaller --workpath ./build/working --distpath ./build/program/ --specpath ./build --runtime-tmpdir ./Data/tmp --ascii --noupx --noconfirm --clean ./Open_Clicker.pyw -wF
timeout 2

timeout 10
