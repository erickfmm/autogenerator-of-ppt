# 🎯 Guía Rápida: Generar Presentaciones PowerPoint

## Instalación de Dependencias

Primero, instala la librería necesaria:

```bash
pip install python-pptx
```

## Generar Presentaciones

### Método 1: Archivo Batch (Más Fácil - Windows)

Simplemente ejecuta el archivo batch haciendo doble clic:

```
run_pptx.bat
```

Esto generará todas las presentaciones por defecto en la carpeta `pptx/`.

### Método 2: Línea de Comandos

```bash
# Generar todas las presentaciones por defecto
python generate_pptx.py

# Generar una presentación específica
python generate_pptx.py "clases/probabilidad y estadistica/0-introduccion.yml"

# Generar todas las presentaciones de la carpeta clases
python generate_pptx.py "clases/probabilidad y estadistica/*.yml"

# Especificar carpeta de salida personalizada
python generate_pptx.py -o mi_carpeta "clases/probabilidad y estadistica/0-introduccion.yml"
```

## 📂 Archivos Generados

Las presentaciones se guardan por defecto en `pptx/`:

- `0-introduccion.pptx`
- `1-tablas_graficos.pptx`
- `2-medidas_posicion.pptx`
- `3-reglas_probabilidades.pptx`

## ✨ Características Principales

### 1. Portada Automática
Cada presentación comienza con una portada colorida con:
- Título del tema
- Subtítulo (si está definido en el YAML)
- Fondo de color azul vibrante

### 2. Gráficos Interactivos
- **Gráficos de Barras**: Para comparar categorías
- **Gráficos de Líneas**: Para mostrar tendencias
- **Gráficos Circulares**: Para mostrar proporciones

Todos los gráficos son editables en PowerPoint.

### 3. Tablas Formateadas
- Encabezados con fondo azul
- Filas con colores alternados
- Texto centrado

### 4. Bloques de Contenido Especiales
- 💡 **Notas**: Información importante (amarillo)
- 📝 **Ejemplos**: Casos prácticos (verde)
- ❓ **Problemas**: Desafíos (rojo)
- 📐 **Fórmulas**: Ecuaciones (morado)
- 🔢 **Cálculos**: Paso a paso (azul)

## 🎨 Personalización

### Cambiar Colores

Edita el diccionario `COLORES` en `generate_pptx.py`:

```python
COLORES = {
    'primario': RGBColor(41, 128, 185),    # Tu color aquí
    'secundario': RGBColor(231, 76, 60),   # Tu color aquí
    # ...
}
```

Los valores RGB van de 0 a 255.

### Cambiar Tamaño de Diapositiva

Modifica en la función `crear_presentacion_base()`:

```python
prs.slide_width = Inches(10)   # Ancho
prs.slide_height = Inches(7.5)  # Alto
```

## 🔄 Comparación con LaTeX

| Aspecto | PowerPoint (.pptx) | LaTeX (.pdf) |
|---------|-------------------|--------------|
| **Edición** | ✅ Fácil en PowerPoint | ❌ Requiere recompilar |
| **Compatibilidad** | ✅ Office, Google Slides | ✅ Universal (PDF) |
| **Fórmulas** | ⚠️ Limitadas | ✅ Excelente |
| **Gráficos** | ✅ Interactivos | ✅ Alta calidad |
| **Velocidad** | ✅✅ Rápido | ⚠️ Requiere compilación |

## 💡 Consejos de Uso

1. **Para Presentaciones Editables**: Usa `generate_pptx.py`
2. **Para Documentos Finales**: Usa `generate_slides.py` (LaTeX → PDF)
3. **Para Compartir**: PowerPoint es más accesible
4. **Para Imprimir**: PDF tiene mejor calidad

## 🐛 Problemas Comunes

### Error: "No module named 'pptx'"

**Solución**: Instala la librería:
```bash
pip install python-pptx
```

### Las diapositivas se ven vacías

**Solución**: Verifica que el archivo YAML tenga la estructura correcta:
```yaml
tema: "Título"
subtitulo: "Subtítulo"
diapositivas:
  - titulo: "Diapositiva 1"
    contenido:
      - "Elemento 1"
```

### Los gráficos no aparecen

**Solución**: Verifica que:
- Las listas `categorias` y `valores` tengan el mismo tamaño
- Los valores sean números, no texto
- El tipo de gráfico esté bien escrito

## 📚 Más Información

- Ver `README_PPTX.md` para documentación completa
- Ver `GUIA_GRAFICOS.md` para ejemplos de todos los tipos de contenido
- Ver `clases/probabilidad y estadistica/ejemplo-graficos.yml` para ejemplos prácticos

## 🚀 Inicio Rápido (30 segundos)

1. Instala la dependencia:
   ```bash
   pip install python-pptx
   ```

2. Ejecuta:
   ```bash
   python generate_pptx.py
   ```

3. Abre las presentaciones en la carpeta `pptx/`

¡Listo! 🎉
