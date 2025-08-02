@echo off
echo === BMW Coding Guide - Build Script ===

REM Șterge folderul dist/ și build/ dacă există
rmdir /s /q build
rmdir /s /q dist
del BMW_Coding_Guide.spec 2>nul

REM Construiește aplicația cu PyInstaller
pyinstaller --windowed --name="BMW_Coding_Guide" ^
--icon="data\\icon_bmw.ico" ^
--add-data "data\\bmw_codari.json;data" ^
--add-data "data\\flag_ro.png;data" ^
--add-data "data\\flag_en.png;data" ^
main.py

echo.
echo === Build complet! EXE-ul se află în folderul dist\BMW_Coding_Guide ===
pause
