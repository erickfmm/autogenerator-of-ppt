# 📊 Generador de Presentaciones PowerPoint

Este script genera presentaciones PowerPoint (.pptx) a partir de archivos YAML con el mismo formato usado para generar las diapositivas LaTeX.

## 🚀 Instalación

Primero, instala la librería necesaria:

```bash
pip install python-pptx
```

O si usas Poetry (según tu `pyproject.toml`):

```bash
poetry add python-pptx
```

## 📝 Uso Básico

### Opción 1: Usando el script directamente

```bash
# Generar todos los archivos por defecto
python generate_pptx.py

# Generar un archivo específico
python generate_pptx.py clases/probabilidad\ y\ estadistica/0-introduccion.yml

# Generar múltiples archivos
python generate_pptx.py clases/probabilidad\ y\ estadistica/*.yml

# Especificar directorio de salida
python generate_pptx.py -o mis_presentaciones clases/probabilidad\ y\ estadistica/0-introduccion.yml
```

### Opción 2: Usando el archivo batch (Windows)

```cmd
run_pptx.bat
```

## 📂 Estructura de Salida

Por defecto, las presentaciones se guardan en el directorio `pptx/`:

```
pptx/
  ├── 0-introduccion.pptx
  ├── 1-tablas_graficos.pptx
  ├── 2-medidas_posicion.pptx
  └── 3-reglas_probabilidades.pptx
```

## 🎨 Características

### Diseño Visual
- ✨ **Colores vibrantes** basados en la plantilla LaTeX
- 🎯 **Portada atractiva** con fondo de color
- 📊 **Diseño profesional** con líneas decorativas
- 🎨 **Tipografía optimizada** para presentaciones

### Tipos de Contenido Soportados

#### 1. Texto Simple
```yaml
contenido:
  - "Texto normal en viñeta"
  - "Otro elemento de lista"
```

#### 2. Bloques Especiales
```yaml
- tipo: "nota"
  texto: "¡Información importante! 💡"

- tipo: "ejemplo"
  texto: "Un ejemplo práctico 📝"

- tipo: "problema"
  texto: "Un desafío a resolver ❓"

- tipo: "formula"
  texto: "Ecuación matemática 📐"

- tipo: "calculo"
  texto: "Cálculo paso a paso 🔢"
```

#### 3. Tablas
```yaml
- tipo: "tabla"
  encabezados: ["Columna 1", "Columna 2"]
  filas:
    - ["Dato 1", "Dato 2"]
    - ["Dato 3", "Dato 4"]
```

#### 4. Gráficos

**Gráfico de Barras:**
```yaml
- tipo: "grafico_barras"
  categorias: ["A", "B", "C"]
  valores: [10, 25, 15]
  etiqueta_x: "Categorías"
  etiqueta_y: "Valores"
  titulo_serie: "Serie 1"
```

**Gráfico de Líneas:**
```yaml
- tipo: "grafico_lineas"
  datos_x: [1, 2, 3, 4, 5]
  datos_y: [10, 15, 13, 18, 20]
  etiqueta_x: "Tiempo"
  etiqueta_y: "Valor"
  titulo_serie: "Tendencia"
```

**Gráfico Circular:**
```yaml
- tipo: "grafico_circular"
  etiquetas: ["Parte 1", "Parte 2", "Parte 3"]
  valores: [40, 35, 25]
```

#### 5. Listas Especiales
```yaml
- tipo: "componentes"
  lista:
    - "Elemento 1"
    - "Elemento 2"

- tipo: "solucion"
  pasos:
    - "Paso 1"
    - "Paso 2"
```

## 🎨 Paleta de Colores

El script utiliza los mismos colores que la plantilla LaTeX:

- 🔵 **Primario**: Azul vibrante (títulos, gráficos)
- 🔴 **Secundario**: Rojo coral (problemas, líneas)
- 🟢 **Acento**: Verde esmeralda (ejemplos, decoración)
- 🟡 **Advertencia**: Amarillo dorado (notas)
- 🟣 **Morado**: Morado amigable (fórmulas)
- 🟠 **Naranja**: Naranja cálido (énfasis)

## 📊 Ejemplos

Ver el archivo `clases/probabilidad y estadistica/ejemplo-graficos.yml` para una demostración completa de todos los tipos de contenido.

## 🔧 Personalización

Puedes modificar los colores editando el diccionario `COLORES` en `generate_pptx.py`:

```python
COLORES = {
    'primario': RGBColor(41, 128, 185),
    'secundario': RGBColor(231, 76, 60),
    # ... más colores
}
```

## 🆚 Diferencias con generate_slides.py

| Característica | generate_slides.py | generate_pptx.py |
|----------------|-------------------|------------------|
| Formato salida | LaTeX (.tex) → PDF | PowerPoint (.pptx) |
| Dependencias | pdflatex, Jinja2 | python-pptx |
| Gráficos | TikZ/PGFPlots | Gráficos nativos de PowerPoint |
| Fórmulas | LaTeX nativo | Texto simple (limitado) |
| Editable | Requiere recompilar | Editable directamente en PowerPoint |

## 💡 Consejos

1. **Fórmulas complejas**: PowerPoint tiene limitaciones para ecuaciones matemáticas. Para fórmulas complejas, usa mejor `generate_slides.py` para generar PDFs.

2. **Edición posterior**: Las presentaciones generadas pueden abrirse y editarse en PowerPoint, Google Slides o LibreOffice Impress.

3. **Gráficos interactivos**: Los gráficos en PowerPoint son editables y los datos pueden modificarse después.

4. **Compatibilidad**: El archivo .pptx es compatible con Office 2007 y versiones superiores.

## 🐛 Solución de Problemas

**Error: No module named 'pptx'**
```bash
pip install python-pptx
```

**Los gráficos no se ven correctamente**
- Verifica que los valores en `categorias` y `valores` tengan la misma longitud
- Asegúrate de que los valores sean números, no strings

**El texto se sale de la diapositiva**
- Reduce la cantidad de contenido por diapositiva
- Divide el contenido en múltiples diapositivas

## 📚 Recursos

- [Documentación de python-pptx](https://python-pptx.readthedocs.io/)
- [GUIA_GRAFICOS.md](GUIA_GRAFICOS.md) - Guía completa de tipos de contenido
