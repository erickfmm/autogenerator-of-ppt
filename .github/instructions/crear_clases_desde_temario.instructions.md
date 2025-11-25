# Esquema YAML para Generación de Clases

Este documento describe el esquema y campos necesarios para crear archivos YAML de clases educativas que pueden ser convertidos automáticamente a presentaciones LaTeX Beamer y PowerPoint.

## 📋 Estructura General

Cada archivo YAML de clase debe seguir esta estructura base:

```yaml
tema: "Título principal del tema"
subtitulo: "Subtítulo descriptivo (opcional)"

diapositivas:
  - titulo: "Título de la diapositiva"
    contenido:
      - "Texto simple o bullet point"
      - tipo: "elemento_especial"
        texto: "Contenido del elemento"
```

---

## 🎯 Campos Principales

### 1. **tema** (requerido)
- **Tipo:** String
- **Descripción:** Título principal de la clase/presentación
- **Ejemplo:** `"Introducción a la Probabilidad y Estadística"`

### 2. **subtitulo** (opcional)
- **Tipo:** String
- **Descripción:** Subtítulo o frase descriptiva
- **Ejemplo:** `"¡Una aventura con números y adivinanzas!"`

### 3. **diapositivas** (requerido)
- **Tipo:** Lista de objetos
- **Descripción:** Colección de todas las diapositivas de la presentación

---

## 📊 Estructura de Diapositivas

Cada diapositiva es un objeto con:

### **titulo** (requerido)
- **Tipo:** String
- **Descripción:** Título visible en la diapositiva
- **Ejemplo:** `"¿Qué vamos a aprender?"`

### **contenido** (requerido)
- **Tipo:** Lista mixta
- **Descripción:** Elementos de contenido (texto, elementos especiales, gráficos)

---

## 📝 Tipos de Contenido

El campo `contenido` puede incluir:

### 1. **Texto Simple**
Strings directos se convierten en bullet points:

```yaml
contenido:
  - "Primera idea importante"
  - "Segunda idea importante"
  - " Con emoji para énfasis 🎯"
```

**Características:**
- Automáticamente se renderizan como viñetas
- Pueden incluir emojis
- Soportan espacios iniciales para énfasis visual

---

### 2. **Notas** 💡
Para destacar información importante:

```yaml
contenido:
  - tipo: "nota"
    texto: "¡Bienvenidos, exploradores de datos! "
```

**Uso:** Avisos, recordatorios, puntos clave
**Color:** Amarillo dorado (advertencia)

---

### 3. **Ejemplos** 📝
Para ilustrar conceptos con casos prácticos:

```yaml
contenido:
  - tipo: "ejemplo"
    texto: "Estadística es ver qué sabor de helado fue el más vendido ayer."
```

**Uso:** Casos de aplicación, ilustraciones
**Color:** Verde esmeralda (acento)

---

### 4. **Problemas** ❓
Para plantear ejercicios o preguntas:

```yaml
contenido:
  - tipo: "problema"
    texto: "Preguntamos a 10 amigos su sabor de helado favorito."
```

**Uso:** Ejercicios, retos, preguntas para resolver
**Color:** Rojo coral (secundario)

---

### 5. **Fórmulas** 📐
Para expresiones matemáticas:

```yaml
contenido:
  - tipo: "formula"
    texto: "Promedio = (Suma de todos los datos) / (Cuántos datos hay)"
```

**Uso:** Ecuaciones, definiciones matemáticas
**Color:** Morado amigable
**Nota:** En LaTeX se puede usar sintaxis matemática estándar

---

### 6. **Cálculos** 🔢
Para mostrar operaciones y resultados:

```yaml
contenido:
  - tipo: "calculo"
    texto: "10 + 12 + 17 = 39"
```

**Uso:** Pasos de resolución, operaciones
**Color:** Azul vibrante (primario)

---

## 📊 Elementos Visuales

### 1. **Tablas**

```yaml
contenido:
  - tipo: "tabla"
    encabezados: ["Columna 1", "Columna 2", "Columna 3"]
    filas:
      - ["Dato 1A", "Dato 1B", "Dato 1C"]
      - ["Dato 2A", "Dato 2B", "Dato 2C"]
      - ["Dato 3A", "Dato 3B", "Dato 3C"]
```

**Campos:**
- `encabezados` (requerido): Lista de títulos de columnas
- `filas` (requerido): Lista de listas con los datos

**Ejemplo completo:**
```yaml
- tipo: "tabla"
  encabezados: ["Sabor", "Nº de Fans"]
  filas:
    - ["Chocolate ", "4"]
    - ["Vainilla ", "3"]
    - ["Fresa ", "2"]
    - ["Limón ", "1"]
```

---

### 2. **Gráfico de Barras** 📊

```yaml
contenido:
  - tipo: "grafico_barras"
    categorias: ["Cat1", "Cat2", "Cat3"]
    valores: [10, 20, 15]
    etiqueta_x: "Eje X"
    etiqueta_y: "Eje Y"
    titulo_serie: "Nombre de la serie"
    ancho_barra: "30pt"  # Opcional, solo LaTeX
```

**Campos:**
- `categorias` (requerido): Lista de nombres para el eje X
- `valores` (requerido): Lista de valores numéricos
- `etiqueta_x` (opcional): Etiqueta del eje horizontal
- `etiqueta_y` (opcional): Etiqueta del eje vertical
- `titulo_serie` (opcional): Nombre de la serie de datos
- `ancho_barra` (opcional): Ancho de barras en LaTeX (ej: "25pt")

**Ejemplo:**
```yaml
- tipo: "grafico_barras"
  categorias: ["Fútbol", "Básquet", "Vóley"]
  valores: [45, 32, 28]
  etiqueta_x: "Deportes"
  etiqueta_y: "Participantes"
  titulo_serie: "Preferencias"
  ancho_barra: "30pt"
```

---

### 3. **Gráfico de Líneas** 📈

```yaml
contenido:
  - tipo: "grafico_lineas"
    datos_x: [1, 2, 3, 4, 5]
    datos_y: [10, 15, 13, 18, 20]
    etiqueta_x: "Eje X"
    etiqueta_y: "Eje Y"
    titulo_serie: "Serie de datos"
    posicion_leyenda: "north east"  # Opcional, solo LaTeX
```

**Campos:**
- `datos_x` (requerido): Lista de valores del eje X
- `datos_y` (requerido): Lista de valores del eje Y
- `etiqueta_x` (opcional): Etiqueta del eje horizontal
- `etiqueta_y` (opcional): Etiqueta del eje vertical
- `titulo_serie` (opcional): Nombre de la serie
- `posicion_leyenda` (opcional): Posición de leyenda en LaTeX

**Posiciones de leyenda válidas (LaTeX):**
- `"north east"`, `"north west"`, `"south east"`, `"south west"`
- `"outer north east"`, etc.

**Ejemplo:**
```yaml
- tipo: "grafico_lineas"
  datos_x: [1, 2, 3, 4, 5, 6, 7]
  datos_y: [22, 24, 23, 25, 27, 26, 24]
  etiqueta_x: "Día de la semana"
  etiqueta_y: "Temperatura (°C)"
  titulo_serie: "Temperatura"
  posicion_leyenda: "north east"
```

---

### 4. **Gráfico Circular** 🥧

```yaml
contenido:
  - tipo: "grafico_circular"
    etiquetas: ["Categoría A", "Categoría B", "Categoría C"]
    valores: [30, 45, 25]
```

**Campos:**
- `etiquetas` (requerido): Lista de nombres de las porciones
- `valores` (requerido): Lista de valores (pueden ser porcentajes o números)

**Ejemplo:**
```yaml
- tipo: "grafico_circular"
  etiquetas: ["Apps", "Fotos", "Música"]
  valores: [50, 30, 20]
```

---

## 🎨 Consejos de Diseño

### Estructura de una Clase Efectiva

Una clase típica debería incluir:

1. **Diapositiva de Portada** (implícita con `tema` y `subtitulo`)
2. **Introducción/Motivación** (2-3 diapositivas)
   - ¿Qué vamos a aprender?
   - ¿Por qué es importante?
   
3. **Conceptos Principales** (5-8 diapositivas)
   - Definiciones con ejemplos
   - Usar bloques de `nota`, `ejemplo`, `formula`
   
4. **Ejemplos Prácticos** (3-5 diapositivas)
   - Problemas resueltos paso a paso
   - Usar `problema`, `calculo`, gráficos
   
5. **Ejercicios/Práctica** (2-3 diapositivas)
   - Problemas para resolver
   - Soluciones opcionales
   
6. **Resumen** (1 diapositiva)
   - Puntos clave aprendidos
   - Usar viñetas simples

### Balance de Contenido

**Por diapositiva:**
- ✅ 3-6 puntos principales
- ✅ 1 elemento visual (tabla o gráfico) máximo
- ✅ Mezclar texto simple con 1-2 bloques especiales
- ❌ Evitar más de 8 líneas de texto
- ❌ No sobrecargar con múltiples gráficos

**Ejemplo de buena estructura:**
```yaml
- titulo: "Ejemplo de Estadística: La Guerra de Helados"
  contenido:
    - tipo: "problema"
      texto: "Preguntamos a 10 amigos su sabor de helado favorito."
    - tipo: "tabla"
      encabezados: ["Sabor", "Nº de Fans"]
      filas:
        - ["Chocolate ", "4"]
        - ["Vainilla ", "3"]
    - tipo: "calculo"
      texto: "Conclusión: ¡El chocolate es el rey!"
```

---

## 📖 Plantilla Completa de Ejemplo

```yaml
tema: "Nombre del Tema"
subtitulo: "Frase descriptiva emocionante 🚀"

diapositivas:
  # === INTRODUCCIÓN ===
  - titulo: "¿Qué vamos a aprender?"
    contenido:
      - tipo: "nota"
        texto: "¡Bienvenidos a esta aventura de aprendizaje! "
      - "Objetivo 1: Comprender el concepto principal"
      - "Objetivo 2: Aplicarlo en ejemplos reales"
      - tipo: "ejemplo"
        texto: "Como cuando usas [analogía cotidiana]"

  # === CONCEPTO PRINCIPAL ===
  - titulo: "Definición del Concepto"
    contenido:
      - "Es la descripción clara y concisa del concepto."
      - tipo: "formula"
        texto: "Concepto = Definición matemática"
      - tipo: "nota"
        texto: "¡Recuerda este punto clave! "

  # === EJEMPLO CON DATOS ===
  - titulo: "Ejemplo Práctico con Datos"
    contenido:
      - tipo: "problema"
        texto: "Planteamiento del problema concreto"
      - tipo: "tabla"
        encabezados: ["Variable", "Valor"]
        filas:
          - ["Dato 1", "10"]
          - ["Dato 2", "20"]

  # === VISUALIZACIÓN ===
  - titulo: "Visualización del Ejemplo"
    contenido:
      - tipo: "grafico_barras"
        categorias: ["A", "B", "C"]
        valores: [10, 20, 15]
        etiqueta_y: "Valores"
        titulo_serie: "Resultados"

  # === EJERCICIO ===
  - titulo: "¡Tu Turno de Practicar! "
    contenido:
      - tipo: "problema"
        texto: "Resuelve este ejercicio aplicando lo aprendido"
      - "Paso 1: Identifica los datos"
      - "Paso 2: Aplica la fórmula"
      - tipo: "nota"
        texto: "¡Puedes hacerlo! "

  # === RESUMEN ===
  - titulo: "¡Resumen de lo Aprendido!"
    contenido:
      - " Concepto 1: Definición breve"
      - " Concepto 2: Aplicación práctica"
      - " Concepto 3: Visualización"
      - tipo: "nota"
        texto: "¡Ahora dominas este tema! "
```

---

## 🔄 Flujo de Trabajo Recomendado

### Paso 1: Partir del Temario
Revisar el archivo `temarios/*.yml` para identificar temas a desarrollar:

```yaml
PROBABILIDAD Y ESTADÍSTICA:
  Representación de datos a través de tablas y gráficos:
    - Tablas de frecuencia absoluta y relativa.
    - Tipos de gráficos que permitan representar datos.
```

### Paso 2: Crear Estructura de Clase
Para cada subtema del temario, crear un archivo YAML en `clases/[materia]/`:

**Nombrado:** `numero-nombre_tema.yml`
- `0-introduccion.yml`
- `1-tablas_graficos.yml`
- `2-medidas_posicion.yml`

### Paso 3: Desarrollar Contenido
Seguir la estructura:
1. Definir `tema` y `subtitulo`
2. Crear diapositivas siguiendo el patrón: Intro → Conceptos → Ejemplos → Práctica → Resumen
3. Usar elementos especiales apropiados para cada tipo de contenido

### Paso 4: Validar y Generar
Ejecutar los scripts de generación:
```bash
# Para LaTeX/PDF
python generate_slides.py clases/probabilidad y estadistica/1-tablas_graficos.yml

# Para PowerPoint
python generate_pptx.py clases/probabilidad y estadistica/1-tablas_graficos.yml
```

---

## ✅ Checklist de Calidad

Antes de finalizar un archivo YAML, verificar:

- [ ] El `tema` es claro y descriptivo
- [ ] Hay entre 10-20 diapositivas (ideal: 12-15)
- [ ] Cada diapositiva tiene un `titulo` único
- [ ] Se mezclan diferentes tipos de contenido (texto, notas, ejemplos, etc.)
- [ ] Hay al menos 2-3 elementos visuales (tablas o gráficos)
- [ ] Los ejemplos son relevantes y fáciles de entender
- [ ] Se incluyen ejercicios prácticos
- [ ] Hay una diapositiva de resumen al final
- [ ] Los emojis agregan valor (no saturan)
- [ ] Las fórmulas son claras y precisas
- [ ] Las tablas tienen encabezados descriptivos
- [ ] Los gráficos tienen etiquetas en los ejes

---

## 🎓 Ejemplos por Tipo de Contenido

### Ejemplo: Clase Matemática
```yaml
tema: "Ecuaciones de Primer Grado"
subtitulo: "Resolviendo el misterio de la X 🔍"

diapositivas:
  - titulo: "¿Qué es una ecuación?"
    contenido:
      - "Es una igualdad que contiene una incógnita (X)"
      - tipo: "formula"
        texto: "2X + 5 = 13"
      - tipo: "nota"
        texto: "¡La X es el número misterioso que buscamos! "
```

### Ejemplo: Clase con Datos
```yaml
tema: "Análisis de Datos"
subtitulo: "Contando historias con números 📊"

diapositivas:
  - titulo: "Datos de Ventas del Mes"
    contenido:
      - tipo: "tabla"
        encabezados: ["Producto", "Ventas"]
        filas:
          - ["Producto A", "150"]
          - ["Producto B", "230"]
      - tipo: "grafico_barras"
        categorias: ["Producto A", "Producto B"]
        valores: [150, 230]
        titulo_serie: "Ventas"
```

### Ejemplo: Clase Experimental
```yaml
tema: "Experimentos con Probabilidad"
subtitulo: "Jugando con el azar 🎲"

diapositivas:
  - titulo: "Experimento: Lanzar una Moneda"
    contenido:
      - tipo: "problema"
        texto: "Lanzamos una moneda 10 veces"
      - tipo: "calculo"
        texto: "Caras: 6 veces = 60%"
      - tipo: "calculo"
        texto: "Sellos: 4 veces = 40%"
      - tipo: "nota"
        texto: "¡Teóricamente debería ser 50/50! Eso es el azar."
```

---

## 🚀 Casos de Uso Avanzados

### Múltiples Gráficos (Comparación)
```yaml
- titulo: "Comparación de Resultados"
  contenido:
    - "Resultados del Grupo A vs Grupo B:"
    - tipo: "grafico_barras"
      categorias: ["Test 1", "Test 2", "Test 3"]
      valores: [85, 90, 88]
      titulo_serie: "Grupo A"
    # Nota: En la práctica, limitar a 1 gráfico por slide
```

### Tablas Comparativas
```yaml
- titulo: "Diferencias Clave"
  contenido:
    - tipo: "tabla"
      encabezados: ["Método A", "Método B"]
      filas:
        - ["Rápido ✓", "Lento ✗"]
        - ["Costoso ✗", "Económico ✓"]
        - ["Preciso ✓", "Aproximado ✗"]
    - tipo: "nota"
      texto: "Cada método tiene pros y contras"
```

### Secuencias de Cálculo
```yaml
- titulo: "Resolución Paso a Paso"
  contenido:
    - tipo: "problema"
      texto: "Calcular el promedio de: 10, 15, 20"
    - tipo: "calculo"
      texto: "Paso 1: Sumar → 10 + 15 + 20 = 45"
    - tipo: "calculo"
      texto: "Paso 2: Dividir → 45 ÷ 3 = 15"
    - tipo: "calculo"
      texto: "Respuesta: El promedio es 15"
```

---

## 📚 Referencias

- **Templates:** `template.tex` (LaTeX Beamer)
- **Scripts de Generación:** 
  - `generate_slides.py` (LaTeX/PDF)
  - `generate_pptx.py` (PowerPoint)
- **Ejemplos Completos:** Ver carpeta `clases/probabilidad y estadistica/`
- **Temarios:** Ver carpeta `temarios/`

---

## 💡 Tips Finales

1. **Emojis:** Úsalos con moderación para agregar personalidad (especialmente en notas y títulos)
2. **Lenguaje:** Escribe de forma clara y cercana al estudiante ("tú", preguntas directas)
3. **Colores:** Confía en los tipos de bloque, cada uno tiene su color asignado
4. **Datos Reales:** Usa ejemplos con números realistas y contextos familiares
5. **Progresión:** Ve de lo simple a lo complejo dentro de cada clase
6. **Interactividad:** Incluye preguntas y ejercicios para mantener la atención
7. **Resumen:** Siempre concluye reforzando los conceptos clave

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Compatibilidad:** LaTeX Beamer, PowerPoint (.pptx)
