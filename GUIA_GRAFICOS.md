# 📊 Guía de Uso de Gráficos en la Plantilla

## Tipos de Gráficos Disponibles

### 1. Gráfico de Barras (`grafico_barras`)

Ideal para comparar categorías.

```yaml
- tipo: "grafico_barras"
  categorias: ["Categoría 1", "Categoría 2", "Categoría 3"]
  valores: [10, 25, 15]
  etiqueta_x: "Eje X"
  etiqueta_y: "Eje Y"
  titulo_serie: "Nombre de la serie"  # Opcional
  ancho_barra: "20pt"  # Opcional, por defecto 20pt
```

**Campos:**
- `categorias`: Lista de nombres para el eje X
- `valores`: Lista de valores numéricos (mismo tamaño que categorias)
- `etiqueta_x`: Texto para el eje horizontal
- `etiqueta_y`: Texto para el eje vertical
- `titulo_serie`: (Opcional) Nombre para la leyenda
- `ancho_barra`: (Opcional) Grosor de las barras

### 2. Gráfico de Líneas (`grafico_lineas`)

Perfecto para mostrar tendencias en el tiempo.

```yaml
- tipo: "grafico_lineas"
  datos_x: [1, 2, 3, 4, 5]
  datos_y: [10, 15, 13, 18, 20]
  etiqueta_x: "Tiempo"
  etiqueta_y: "Valor"
  titulo_serie: "Tendencia"  # Opcional
  posicion_leyenda: "north west"  # Opcional
```

**Campos:**
- `datos_x`: Lista de valores para el eje X
- `datos_y`: Lista de valores para el eje Y (mismo tamaño que datos_x)
- `etiqueta_x`: Texto para el eje horizontal
- `etiqueta_y`: Texto para el eje vertical
- `titulo_serie`: (Opcional) Nombre para la leyenda
- `posicion_leyenda`: (Opcional) Posición: "north west", "north east", "south west", "south east"

### 3. Gráfico Circular (`grafico_circular`)

Excelente para mostrar proporciones.

```yaml
- tipo: "grafico_circular"
  etiquetas: ["Parte 1", "Parte 2", "Parte 3"]
  valores: [40, 35, 25]
```

**Campos:**
- `etiquetas`: Lista de nombres para cada porción
- `valores`: Lista de valores o porcentajes (mismo tamaño que etiquetas)

## Otros Tipos de Contenido

### Bloques de Texto

```yaml
- tipo: "ejemplo"
  texto: "Este es un ejemplo práctico"

- tipo: "nota"
  texto: "¡Información importante!"

- tipo: "problema"
  texto: "Plantea un desafío"
```

### Fórmulas

```yaml
- tipo: "formula"
  texto: "E = mc^2"

- tipo: "calculo"
  texto: "x + y &= 10 \\\\ 2x - y &= 3"
```

### Tablas

```yaml
- tipo: "tabla"
  encabezados: ["Columna 1", "Columna 2"]
  filas:
    - ["Dato 1", "Dato 2"]
    - ["Dato 3", "Dato 4"]
```

### Listas

```yaml
- tipo: "componentes"
  lista:
    - "Elemento 1"
    - "Elemento 2"
    - "Elemento 3"

- tipo: "solucion"
  pasos:
    - "Paso 1"
    - "Paso 2"
    - "Paso 3"
```

### Texto Simple

```yaml
- "Este es un elemento de lista simple"
- "Otro elemento de lista"
```

## Colores Disponibles

La plantilla incluye estos colores lúdicos:
- 🔵 **colorPrimario**: Azul vibrante
- 🔴 **colorSecundario**: Rojo coral
- 🟢 **colorAccento**: Verde esmeralda
- 🟡 **colorAdvertencia**: Amarillo dorado
- 🟣 **colorMorado**: Morado amigable
- 🟠 **colorNaranja**: Naranja cálido

## Características de Diseño

✨ **Tema moderno y lúdico** con colores vibrantes
📊 **Gráficos interactivos** con TikZ y PGFPlots
🎨 **Tablas con colores alternados** para mejor legibilidad
💡 **Iconos en bloques** para hacer el contenido más visual
🎯 **Diseño limpio** con espaciado y tipografía optimizados

## Ejemplo Completo

Ver el archivo `ejemplo-graficos.yml` para una demostración completa de todos los tipos de gráficos.
