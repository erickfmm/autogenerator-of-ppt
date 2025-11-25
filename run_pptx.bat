@echo off
echo ========================================
echo Generador de PowerPoint - Probabilidad y Estadistica
echo ========================================
echo.

REM Ejecutar el script de Python
python generate_pptx.py %*

echo.
echo ========================================
echo Presiona cualquier tecla para salir...
pause >nul
