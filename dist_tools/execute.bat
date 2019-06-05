netstat -o -n -a | grep LISTEN | findstr 5000
if %ERRORLEVEL% equ 0 goto START
cd pmtk-services-NEW && nircmd.exe exec hide execute.bat
cd ..
:START
netstat -o -n -a | grep LISTEN | findstr 5000
if %ERRORLEVEL% equ 0 goto FOUND
echo port not found
timeout /t 1
goto START
:FOUND
echo port found
cd pmtk-electron && pmtk.exe