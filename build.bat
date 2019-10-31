@echo off

timeout 1
echo Starting Build

set mypath=%cd%
echo %mypath%

timeout 2
copy "%mypath%\Data\Images\" "%mypath%\build\program\Data\Images\"

timeout 2
pyinstaller --workpath ./build/working --distpath ./build/program --specpath ./build --ascii --key test ./Open_Clicker.pyw -wF

timeout 2
pyinstaller --workpath ./build/working --distpath ./build/program/data/Hotkey --specpath ./build --ascii ./Data/Hotkey/HotKey.pyw  

timeout 2 
pyinstaller --workpath ./build/working --distpath ./build/program/data/Settings --specpath ./build --ascii ./Data/Settings/Settings.pyw


timeout 10
