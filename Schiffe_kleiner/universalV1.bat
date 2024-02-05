echo Bearbeite %arg1%.xml
setlocal EnableDelayedExpansion
set search=
set replace=
for /F "tokens=1,2 delims=:" %%a in (drittel.txt) do (
   set "search=!search!|%%a"
   set "replace=!replace!|%%b"
)
set "search=!search:~1!"
set "replace=!replace:~1!"
set arg1=%1
< ..\..\data\%arg1%.xml findRepl =search /A =replace > %arg1%.xml
echo %arg1%.xml in Modordner geschrieben
))