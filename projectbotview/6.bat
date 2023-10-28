@echo off
SET "URL=https://addons.mozilla.org/th/firefox/addon/urban-vpn/"


start "" "C:\Program Files\Mozilla Firefox\firefox.exe" -P 06 -no-remote "%URL%"
timeout /t 3 >nul
echo wscript.sleep 1000 > "%temp%\keypress.vbs"
echo wscript.createobject("wscript.shell").sendkeys "{ESC}" >> "%temp%\keypress.vbs"
cscript //nologo "%temp%\keypress.vbs"
del "%temp%\keypress.vbs"
python python.py


