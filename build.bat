@echo off

timeout 1
echo Starting Build

set mypath=%cd%
echo %mypath%

timeout 2
copy "%mypath%\Data\Images\" "%mypath%\build\program\Data\Images\"

timeout 2
pyinstaller --workpath ./build/working --distpath ./build/program/data/Hotkey --specpath ./build --ascii --noconfirm ./Data/Hotkey/HotKey.pyw

pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --ascii --noconfirm ./Data/Settings/Settings.pyw
timeout 2 

pyinstaller --workpath ./build/working --distpath ./build/program --specpath ./build --runtime-tmpdir ./Data/tmp --ascii --noupx --noconfirm ./Open_Clicker.pyw -wF
timeout 2

timeout 10
