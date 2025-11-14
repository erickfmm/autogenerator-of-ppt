# Generador de Diapositivas - Probabilidad y Estadística

Sistema automatizado para generar presentaciones LaTeX Beamer a partir de archivos YAML.

## Estructura del Proyecto

```
probest/
├── tablas_graficos.yml          # Contenido tema 1
├── medidas_posicion.yml         # Contenido tema 2
├── reglas_probabilidades.yml    # Contenido tema 3
├── template.tex                 # Template LaTeX Beamer
├── generate_slides.py           # Script generador
├── pyproject.toml              # Configuración del proyecto
└── slides/                     # Directorio de salida (generado)
    ├── tablas_graficos.tex
    ├── tablas_graficos.pdf
    ├── medidas_posicion.tex
    ├── medidas_posicion.pdf
    ├── reglas_probabilidades.tex
    └── reglas_probabilidades.pdf
```

## Instalación

### Usando uv (recomendado)

```bash
# Instalar uv si no lo tienes
pip install uv

# Sincronizar dependencias
uv sync
```

### Usando pip tradicional

```bash
pip install -r requirements.txt
```

## Requisitos del Sistema

- Python >= 3.9
- LaTeX (TeX Live, MiKTeX o similar) para compilar PDFs
  - Si no tienes LaTeX, el script generará solo archivos .tex

## Uso

### Generar todas las diapositivas

```bash
# Con uv
uv run python generate_slides.py

# O directamente si está instalado
python generate_slides.py
```

### Modificar contenido

1. Edita los archivos YAML correspondientes a cada tema
2. Ejecuta el script generador
3. Las diapositivas se regenerarán automáticamente

### Personalizar template

Edita `template.tex` para cambiar:
- Tema de Beamer (`\usetheme{Madrid}`)
- Colores (`\usecolortheme{default}`)
- Estructura de las diapositivas

## Formato de los archivos YAML

Cada archivo YAML sigue esta estructura:

```yaml
tema: "Título del tema"
subtitulo: "Subtítulo"

diapositivas:
  - titulo: "Título de la diapositiva"
    contenido:
      - "Texto simple como viñeta"
      - tipo: "ejemplo"
        texto: "Contenido del ejemplo"
      - tipo: "formula"
        texto: "\\frac{a}{b}"
```

### Tipos de contenido soportados

- **string**: Viñeta simple
- **ejemplo**: Bloque de ejemplo
- **formula**: Fórmula matemática centrada
- **calculo**: Ecuaciones alineadas
- **nota**: Bloque de alerta
- **problema**: Bloque de problema
- **tabla**: Tabla con encabezados y filas
- **componentes**: Lista de componentes
- **solucion**: Bloque de solución con pasos

## Compilación Manual

Si prefieres compilar manualmente:

```bash
cd slides
pdflatex tablas_graficos.tex
pdflatex tablas_graficos.tex  # Segunda pasada para referencias
```

## Desarrollo

```bash
# Instalar dependencias de desarrollo
uv sync --all-extras

# Formatear código
black generate_slides.py

# Linting
ruff check generate_slides.py
```

## Licencia

Proyecto educativo para el Ministerio de Educación.
