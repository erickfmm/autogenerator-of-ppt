#!/usr/bin/env bash
set -euo pipefail

echo "============================================================"
echo "Generando todas las presentaciones desde clases/**/*.yml"
echo "============================================================"
echo ""

echo "[1/2] Generando presentaciones LaTeX/PDF..."
echo "------------------------------------------------------------"
python generate_slides.py
if [ $? -ne 0 ]; then
    echo "ERROR: Fallo al generar PDFs"
    exit 1
fi

echo ""
echo "[2/2] Generando presentaciones PowerPoint..."
echo "------------------------------------------------------------"
python generate_pptx.py
if [ $? -ne 0 ]; then
    echo "ERROR: Fallo al generar PPTX"
    exit 1
fi

echo ""
echo "============================================================"
echo "Proceso completado exitosamente!"
echo ""
echo "Archivos generados:"
echo "  - PDFs en:  pdfs/[materia]/"
echo "  - PPTXs en: pptx/[materia]/"
echo "  - TEXs en:  slides/"
echo "============================================================"
