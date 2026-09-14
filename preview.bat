@echo off
REM ============================================================
REM  Vista previa local del sitio (sin Ruby/Jekyll)
REM  Doble clic para reconstruir _preview/ y abrirla en el navegador.
REM ============================================================
cd /d "%~dp0"

echo Generando vista previa...
python build_preview.py
if errorlevel 1 (
  echo.
  echo [!] Falta instalar dependencias. Ejecuta una sola vez:
  echo     python -m pip install markdown pyyaml
  echo.
  pause
  exit /b 1
)

echo Abriendo _preview\index.html ...
start "" "%~dp0_preview\index.html"
