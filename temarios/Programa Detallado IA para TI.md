# **Programa de Capacitación Avanzada de 18 Horas para Equipos de TI: Ingeniería de Software, Análisis de Datos, Automatización y Gestión de Proyectos con Inteligencia Artificial**

La incorporación de la inteligencia artificial en los flujos de trabajo de tecnología de la información ha dejado de ser un mero complemento de autocompletado de texto para convertirse en un cambio fundamental en la arquitectura de sistemas y el desarrollo de software.1 La transición desde un modelo de chat informal hacia un sistema cognitivo integrado exige que los profesionales de TI comprendan la base matemática de los grandes modelos de lenguaje, dominen los entornos de desarrollo agéntico y utilicen metodologías de desarrollo basadas en especificaciones estrictas.1 El presente programa académico de 18 horas, estructurado en seis bloques temáticos, dota a los ingenieros de TI de las competencias teóricas y prácticas necesarias para actuar como directores y facilitadores de esta transformación tecnológica, utilizando la inteligencia artificial de forma continua como un colaborador analítico y de ejecución en cada etapa del ciclo de desarrollo de software.2

## **Estructura General y Distribución Horaria del Programa**

El programa de capacitación se organiza de forma modular para garantizar un balance óptimo entre la fundamentación científica, la demostración de patrones arquitectónicos y la experimentación directa por parte de los asistentes.

| Bloque Temático | Horas | Temas Clave de los Módulos | Herramientas de Experimentación |
| :---- | :---- | :---- | :---- |
| **I. Fundamentos de IA y NLP Moderno** | 1 a 3 | Teoría de sistemas, álgebra básica, aproximación universal, mecanismos de atención, modelos autoregresivos, MoE, LoRA y RoPE Scaling.4 | Visualizadores de mapas de atención y tokenización lineal. |
| **II. Prompting Avanzado y Arquitecturas RAG** | 4 a 6 | Ingeniería de prompts estructurada (STAR, RACE, CLEAR, GOLD), pipelines de RAG y GraphRAG, e interfaces de orquestación visual.5 | Entornos no-code como Dify y Flowise, bases vectoriales locales. |
| **III. Agentes Inteligentes y Entornos ADE** | 7 a 9 | Protocolo Model Context Protocol (MCP), entornos de desarrollo agénticos (IDEs vs. CLI autónomos) y Spec-Driven Development (SDD).2 | Claude Code, OpenCode, Codex, y suites de Gentle-AI.3 |
| **IV. Documentación, Memoria y Domain-Driven Design** | 10 a 12 | Documentación Markdown, Tolaria offline-first, bases de conocimiento, memorias MCP (Engram, Codebase-Memory) y DDD para contratos de APIs.5 | Tolaria Desktop, Engram TUI y generadores de contratos de APIs.9 |
| **V. EDA Automatizado y Pipelines de Automatización** | 13 a 15 | Análisis Exploratorio de Datos automático, Data Formulator con conectores SQL e integraciones de flujos de trabajo con n8n.4 | Sweetviz, YData-Profiler, Data Formulator local y n8n.13 |
| **VI. Pruebas de Software, Gestión e Interfaz Gráfica** | 16 a 18 | TDD/BDD con Gherkin, Selenium frente a Playwright, gestión de licitaciones (AEPD/LCSP), resúmenes Teams y generación frontend con OpenPencil.2 | Playwright Codegen, OpenPencil con servidor MCP.17 |

## **Módulo I: Fundamentos de Inteligencia Artificial y Procesamiento del Lenguaje Natural Moderno (Horas 1-3)**

### **Hora 1: Teoría de Sistemas, Álgebra y Aproximación Universal**

El bloque formativo se inicia con una aproximación rigurosa a la inteligencia artificial desde la teoría de sistemas, desmitificando la noción de la IA como una "entidad pensante" para definirla como un sistema de aproximación de funciones altamente complejo.4 Se analiza el proceso de formalización que permite abstraer un fenómeno natural y convertirlo en un sistema matemático gobernable expresado mediante entradas y salidas bajo la formulación básica ![][image1].4

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Portada de la Sesión.** Título claro que enuncie las nociones del aprendizaje de máquinas y la abstracción sistémica del software.4 Se debe incluir un esquema gráfico minimalista que represente un fenómeno del mundo real transformándose en un diagrama de contexto estructurado.4  
* **Diapositiva 2: Clasificación de Sistemas de Información.** Un cuadro comparativo que explique las diferencias entre sistemas lineales de pocas variables calculables mediante álgebra elemental, sistemas de variables masivas tratables estadísticamente, y sistemas complejos altamente no lineales y diferenciables que justifican el uso de la optimización basada en gradientes.4  
* **Diapositiva 3: Redes Neuronales como Funciones Plantilla.** Explicación matemática de cómo una red neuronal representa una "función plantilla" parametrizable cuyos coeficientes libres se ajustan a través de procesos de optimización probabilística y cálculo de derivadas.4  
* **Diapositiva 4: El Teorema de Aproximación Universal.** Demostración formal de que una red neuronal densa con capas ocultas y funciones de activación no lineales puede modelar cualquier función continua sobre espacios compactos, sentando las bases del Deep Learning 4:  
  ![][image2]

#### **Laboratorio Práctico y Experimentación con IA**

Los ingenieros interactúan con un entorno interactivo en Python para inicializar una red neuronal básica de clasificación utilizando funciones de activación no lineales. Guiados por el instructor, utilizan un prompt estructurado para solicitarle a un modelo de lenguaje que genere un script que optimice visualmente el descenso de gradiente sobre una función de costo compleja no lineal, observando en tiempo real cómo los pesos y sesgos se ajustan iterativamente.4

#### **Preguntas Clave y Debate**

* ¿Cómo limita la naturaleza no diferenciable de ciertos algoritmos clásicos de TI su resolución mediante el descenso de gradiente directo? 4  
* ¿Qué implicaciones de infraestructura técnica surgen cuando un sistema pasa de requerir cálculo analítico cerrado a requerir simulaciones computacionales intensivas? 4

### **Hora 2: Grandes Modelos de Lenguaje (LLMs) y Procesamiento del Lenguaje Natural Moderno**

Se profundiza en los mecanismos que permiten a un sistema informático estructurar el lenguaje natural.4 Se cubren los procesos algorítmicos que transforman los caracteres de un texto plano en unidades matemáticas procesables denominadas tokens, analizando las implicaciones de la ventana de contexto y los retos de la vectorización semántica.4

Texto Plano: "Desarrollo agéntico"   
  └── Tokenizador ──\>  (Tokens)  
        └── Embeddings ──\> Vector N-Dimensional \[0.12, \-0.45,..., 0.89\] (Espacio Semántico)

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Desafío Algorítmico de la Tokenización.** Análisis de las limitaciones de la segmentación por espacios simples y cómo los tokenizadores modernos utilizan expresiones regulares y diccionarios entrenados para resolver caracteres especiales, signos de puntuación y morfemas complejos.4  
* **Diapositiva 2: Stemming, Lemmatization y Representación de Significado.** Comparación gráfica entre la reducción heurística a la raíz (Stemming) y la transformación morfológica precisa basada en inteligencia artificial (Lemmatization).4  
* **Diapositiva 3: Embeddings Vectoriales.** Visualización de un espacio n-dimensional donde las palabras se proyectan en vectores semánticos continuos obtenidos durante la fase de entrenamiento.4 Se representa gráficamente la aritmética vectorial semántica 4:  
  ![][image3]  
* **Diapositiva 4: Modelos Autoregresivos y Causales.** Diagrama que ilustra la naturaleza de los modelos generativos decodificadores que predicen secuencialmente el siguiente token basándose de forma exclusiva en la ventana de contexto izquierda.4

#### **Laboratorio Práctico y Experimentación con IA**

Uso de un visualizador de tokenización en línea para analizar cómo un fragmento de código fuente en TypeScript o Go es fragmentado por diferentes tokenizadores (e.g., LLaMA, GPT-4). Los participantes experimentarán solicitando a un modelo local la conversión de términos del dominio de TI a embeddings vectoriales, calculando la distancia de coseno para identificar qué términos de infraestructura presentan mayor similitud en el espacio latente.

#### **Preguntas Clave y Debate**

* ¿Por qué la tokenización de código fuente consume más ventana de contexto en promedio en comparación con el lenguaje natural estructurado? 4  
* ¿Cuáles son las implicaciones operativas en la latencia del sistema debido a la naturaleza estrictamente secuencial y causal de los modelos autorregresivos? 4

### **Hora 3: La Arquitectura del Transformer, Modelos Sequence-to-Sequence y Técnicas de Escalamiento**

Esta hora aborda los hitos de la arquitectura profunda que posibilitaron la revolución actual de la IA generativa, analizando el funcionamiento interno del mecanismo de autoatención y los esquemas de optimización y escalamiento de parámetros.4

| Arquitectura / Técnica | Enfoque Operacional | Ventana de Contexto | Ventaja Crítica | Limitación en Producción |
| :---- | :---- | :---- | :---- | :---- |
| **Modelos Decodificadores Causales** | Generación de texto unidireccional paso a paso.4 | Alta (Desde 4k hasta más de 128k tokens).4 | Óptimo para generación de código y razonamiento agéntico general.4 | Elevado costo computacional en inferencia secuencial.4 |
| **Modelos Bidireccionales (BERT)** | Análisis de contexto izquierdo y derecho simultáneamente.4 | Corta (Típicamente limitada a 512 tokens). | Máxima precisión en clasificación, etiquetado POS y extracción.4 | Incapacidad estructural para tareas de generación fluida.4 |
| **Mezcla de Expertos (MoE)** | Activación dinámica de subredes especializadas por token.4 | Alta y optimizada dinámicamente. | Inferencia de alto rendimiento reduciendo parámetros activos en GPU.4 | Elevados requerimientos de memoria VRAM para cargar todos los expertos.4 |

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Mecanismo de Autoatención (Self-Attention).** Explicación del avance introducido en 2017 por Google.4 Representación de la matriz de atención bidimensional que evalúa el peso relativo de importancia de cada término en relación con la secuencia completa.4  
* **Diapositiva 2: El Modelo BERT y los Modelos Sequence-to-Sequence (SLM).** Explicación de BERT como modelo representacional bidireccional de bajo cómputo (típicamente 300 MB).4 Introducción a los modelos de secuencia a secuencia como mT5 diseñados específicamente para traducción y síntesis directa.4  
* **Diapositiva 3: Arquitecturas de Mezcla de Expertos (MoE).** Esquema arquitectónico de modelos como Mixtral ![][image4], ilustrando cómo una red de enrutamiento distribuye secuencialmente los tokens de entrada hacia expertos especializados bajo un mapa de atención común.4  
* **Diapositiva 4: Fine-Tuning Eficiente con LoRA y Escalamiento de Contexto con RoPE.** Análisis matemático de Low-Rank Adaptation (LoRA) para el entrenamiento de parámetros con bajo poder de cómputo GPU y el escalamiento de ventanas de contexto mediante Rotary Position Embedding (RoPE).4

#### **Laboratorio Práctico y Experimentación con IA**

Carga de modelos de lenguaje pequeños (SLMs) como TinyLlama o Phi-2 en entornos locales del equipo de TI. Se ejecutan scripts de prueba para cuantificar el impacto del uso de adaptadores LoRA ligeros en la especialización de términos de APIs de la compañía, midiendo tiempos de inferencia y consumo de VRAM.4

#### **Preguntas Clave y Debate**

* ¿Cómo puede la arquitectura de Mezcla de Expertos optimizar los costos de cómputo en servidores locales en comparación con el despliegue de modelos monolíticos gigantes? 4  
* ¿Qué riesgos de pérdida de consistencia se presentan al escalar artificialmente la ventana de contexto de un modelo de lenguaje utilizando técnicas de RoPE Scaling sin reentrenamiento masivo? 4

## **Módulo II: Ingeniería de Prompts Avanzada, Gestión de Contexto y Arquitecturas de Recuperación (RAG) (Horas 4-6)**

### **Hora 4: Estructuración Metódica de Prompts y Marcos de Trabajo Corporativos**

Se trasciende el uso intuitivo de los prompts de lenguaje natural para estudiar la ingeniería de prompts como un paradigma de programación declarativa, estructurando instrucciones rigurosas basadas en variables y restricciones operativas.8

Prompt Estructurado (STAR / GOLD)  
 ├── S: Situación corporativa e infraestructura de TI   
 ├── T: Tarea u Objetivo de código / especificación   
 ├── A: Apariencia del formato de salida (e.g., JSON estructurado)   
 └── R: Refinamientos, límites sintácticos y exclusiones técnicas 

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: La Ingeniería de Prompts como Disciplina.** Explicación de por qué la precisión del software depende de la limitación semántica del prompt.8 El concepto de inyección de restricciones y el control de la aleatoriedad en el comportamiento del modelo (temperatura y top-p).21  
* **Diapositiva 2: Técnicas Fundamentales: STAR y RTF.** Explicación paso a paso de la técnica STAR (Situation, Task, Appearance, Refine) y su aplicabilidad en la generación de scripts de infraestructura.8 Introducción al marco ágil RTF (Role, Task, Format) para comandos rápidos en consola.7  
* **Diapositiva 3: Marcos Avanzados: RACE, CLEAR, RISEN y GOLD.** Comparación de metodologías estructuradas para tareas de análisis de código.6 Detalle del marco GOLD (Goal, Obstacles, Logic, Data) para la resolución de algoritmos y diagnóstico de fallas complejas de sistemas.6  
* **Diapositiva 4: Razonamiento Secuencial de la IA: Chain-of-Thought (CoT) y Tree-of-Thought (ToT).** Demostración de cómo la instrucción explícita de desglosar secuencialmente el pensamiento ("pensemos paso a paso") eleva la precisión lógica en dominios complejos de programación.6

#### **Laboratorio Práctico y Experimentación con IA**

Los asistentes toman un prompt vago de generación de código heredado y lo reconstruyen utilizando los marcos STAR y GOLD.6 Evaluarán comparativamente los resultados devueltos por un modelo avanzado, cuantificando la reducción de código redundante y la incorporación de mejores prácticas de seguridad en el código autogenerado.21

#### **Preguntas Clave y Debate**

* ¿Por qué los modelos de lenguaje tienden a omitir restricciones complejas cuando se les acumulan instrucciones contradictorias en un único prompt monolítico? 21  
* ¿En qué escenarios técnicos de automatización es preferible utilizar Few-Shot Prompting en lugar de extender las instrucciones del prompt del sistema mediante Zero-Shot? 6

### **Hora 5: Gestión de Contexto, Embeddings Vectoriales y Arquitecturas RAG**

Esta sesión capacita al equipo de TI en la arquitectura del patrón Retrieval-Augmented Generation (RAG), permitiendo que los modelos de lenguaje accedan a bases de conocimiento corporativas cerradas en tiempo real sin requerir costosas fases de reentrenamiento.4

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Fundamentos de RAG.** Diagrama de flujo de datos que describe la ingesta de documentos corporativos no estructurados, su fragmentación en bloques, la generación de embeddings, el almacenamiento vectorial y la inyección dinámica del contexto recuperado durante la inferencia.4  
* **Diapositiva 2: Limitaciones de RAG Clásico sobre Repositorios de Código.** Análisis de por qué la fragmentación secuencial estándar de texto destruye la jerarquía sintáctica y semántica del código fuente de software, produciendo alucinaciones al consultar dependencias lógicas complejas.5  
* **Diapositiva 3: Introducción a GraphRAG.** Explicación del modelado de conocimiento a través de grafos semánticos estructurados que conectan entidades y relaciones, permitiendo búsquedas contextuales de mayor nivel jerárquico.5  
* **Diapositiva 4: Grafos de Dependencia de Código con Tree-Sitter.** Ilustración de cómo herramientas modernas compilan el código fuente en árboles sintácticos abstractos (AST) almacenados en bases de datos SQLite locales expuestas mediante el protocolo Model Context Protocol (MCP).5

#### **Laboratorio Práctico y Experimentación con IA**

Inicialización local de una base de datos vectorial liviana (e.g., ChromaDB). Los ingenieros de TI generan embeddings de un conjunto de archivos Markdown corporativos y simulan un flujo de búsqueda semántica comparando la relevancia del contexto devuelto contra una búsqueda tradicional por palabras clave.

#### **Preguntas Clave y Debate**

* ¿Cómo afecta la estrategia de fragmentación (Chunking) y el solapamiento de caracteres a la calidad de la respuesta final de un sistema RAG? 4  
* ¿Cuáles son las diferencias críticas de almacenamiento y tiempo de cómputo en inferencia al implementar un buscador semántico vectorial frente a una arquitectura de GraphRAG? 5

### **Hora 6: Orquestadores de RAG, Agentes y Plataformas No-Code / Low-Code**

Se estudian las herramientas de orquestación lógica que permiten construir aplicaciones de inteligencia artificial estables e integradas con el ecosistema corporativo de TI, abarcando desde frameworks basados en código hasta plataformas visuales.2

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Orquestación de Datos frente a Orquestación Agéntica.** Diagrama que posiciona a LangChain y LlamaIndex como capas de abstracción para la recuperación y estructuración de información, diferenciándolos de frameworks agénticos que admiten ciclos complejos de decisión y ejecución como Haystack y LangGraph.2  
* **Diapositiva 2: LangGraph y Arquitecturas Agénticas Cíclicas.** Explicación de cómo modelar flujos de trabajo de IA utilizando grafos de estado cíclicos, permitiendo que un agente reintente operaciones en caso de falla o valide su propio código antes de responder.2  
* **Diapositiva 3: Frameworks de Autonomía Agéntica.** Análisis de herramientas como AutoAgent y ADK (Agent Development Kit), evaluando la interacción colaborativa entre múltiples agentes autónomos organizados jerárquicamente.2  
* **Diapositiva 4: Plataformas No-Code: Flowise y Dify.** Demostración del desarrollo ágil mediante interfaces visuales donde se configuran conectores de datos, variables de sistema, herramientas y modelos de lenguaje de forma centralizada sin escribir código de orquestación intermedio.

#### **Laboratorio Práctico y Experimentación con IA**

El equipo utiliza una instancia de **Dify** o **Flowise** para construir visualmente un flujo de análisis técnico que reciba logs de errores de servidores, los vectorice semánticamente, consulte la base de conocimiento local para identificar la solución histórica de la falla y devuelva un informe estructurado con el parche sugerido.

#### **Preguntas Clave y Debate**

* ¿Qué ventajas operativas presenta la persistencia de estado de LangGraph en comparación con los flujos estrictamente secuenciales de LangChain clásico? 2  
* ¿Cómo equilibrar la agilidad del prototipado visual en Dify con la necesidad de mantener el control de versiones y el despliegue continuo de código (CI/CD) de las herramientas de TI?

## **Módulo III: Entornos de Desarrollo Agéntico (ADE) y Spec-Driven Development (SDD) (Horas 7-9)**

### **Hora 7: Anatomía de un Agente Inteligente y el Protocolo Model Context Protocol (MCP)**

Esta sesión detalla cómo los agentes de IA interactúan directamente con el entorno de ejecución, analizando sus componentes internos y la estandarización abierta de herramientas y recursos del sistema a través del protocolo MCP.2

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Arquitectura de un Agente de IA Moderno.** Diagrama técnico que integra el Orquestador lógico (LLM), las Herramientas (Tools ejecutables), las Habilidades empaquetadas (Skills) y los Sistemas de Memoria persistente.2  
* **Diapositiva 2: El Protocolo Model Context Protocol (MCP).** Explicación detallada del estándar impulsado por Anthropic para habilitar de forma segura herramientas y acceso a datos locales de manera estandarizada mediante sockets de stdio o HTTP.5  
* **Diapositiva 3: Orquestación Multitarea y Dinámica Subagente.** Análisis del patrón de división de tareas complejos donde un agente padre delega la investigación y la implementación a subagentes específicos y enfocados de contexto delgado.2  
* **Diapositiva 4: Modificaciones Seguras del Sistema.** Explicación de cómo los agentes consumen y aplican parches lógicos de diferencias (archivos diff) para interactuar con sistemas de control de versiones Git sin necesidad de sobreescribir directorios masivos completos de manera ciega.2

#### **Laboratorio Práctico y Experimentación con IA**

Levantar localmente un servidor de demostración de Model Context Protocol (MCP). Configurar el entorno para exponer utilidades de terminal al cliente de IA local, verificando a través de los logs de la consola cómo el modelo de lenguaje de forma autónoma selecciona la herramienta adecuada para ejecutar un comando básico del sistema y recibir la respuesta formateada en JSON.5

#### **Preguntas Clave y Debate**

* ¿De qué manera el protocolo MCP resuelve los desafíos de seguridad y gobierno de TI en comparación con la ejecución libre de scripts de consola mediante funciones exec clásicas? 3  
* ¿Qué impacto tiene el diseño basado en subagentes independientes en la reducción del costo computacional de la ventana de contexto de los modelos? 2

### **Hora 8: Entornos de Desarrollo de Agentes (ADE) Híbridos y CLI**

Se evalúa el ecosistema de herramientas de desarrollo integradas con capacidades agénticas avanzadas, comparando los entornos gráficos frente a los asistentes autónomos basados estrictamente en interfaces de línea de comando (CLI).3

                 Entornos de Desarrollo Agéntico (ADE)  
       ┌───────────────────────────┴───────────────────────────┐  
       ▼                                                       ▼  
IDEs Gráficos Híbridos                                  CLI Autónomos de Consola  
(Cursor, Windsurf, VS Code Copilot)                      (Claude Code, OpenCode, Codex)  
 \- Enfoque interactivo visual                            \- Autonomía completa de archivos  
 \- Aprobación línea por línea                            \- Integración directa con bash y git 

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Evolución del Software de Desarrollo con IA.** De los asistentes de autocompletado en la sombra a los entornos de desarrollo agénticos de control bidireccional de código.3  
* **Diapositiva 2: IDEs Híbridos Gráficos.** Análisis profundo de Cursor, Windsurf y VS Code Copilot, describiendo sus capacidades de edición en paralelo sobre múltiples archivos y la predicción de líneas de código en tiempo real.  
* **Diapositiva 3: Clientes CLI Autónomos: Claude Code y OpenCode.** Demostración de herramientas que actúan de manera directa sobre la terminal del desarrollador, administrando tareas de exploración de dependencias, compilaciones rotas y refactorizaciones sin interfaz visual.3  
* **Diapositiva 4: Alternativas Especializadas: Codex, Gemini CLI y Hermes.** Análisis técnico de las capacidades, ventajas operativas y deficiencias críticas de cada herramienta en el manejo de contextos masivos y soporte multilenguaje.10

#### **Laboratorio Práctico y Experimentación con IA**

Los asistentes instalan y configuran de forma local **Claude Code** u **OpenCode** en sus máquinas.3 Ejecutan tareas de auditoría automáticas sobre un proyecto de código heredado, instruyendo al cliente CLI de IA a identificar vulnerabilidades lógicas y generar archivos de parche (diff format) correspondientes de manera autónoma.3

#### **Preguntas Clave y Debate**

* ¿Cuáles son las ventajas e ineficiencias críticas de los entornos CLI como Claude Code en comparación con el uso del panel Composer de un IDE gráfico como Cursor? 3  
* ¿Cómo deben los equipos de TI gestionar las claves de API locales y el presupuesto de tokens ante la ejecución descontrolada de llamadas automáticas de desarrollo agéntico? 24

### **Hora 9: Metodología Spec-Driven Development (SDD) Avanzado con la Suite de Gentleman-AI**

Esta sesión presenta la metodología de desarrollo estructurada diseñada para erradicar el caos del código generado de forma aleatoria por la IA, introduciendo procesos rigurosos guiados por especificaciones previas.2

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Caos del Desarrollo Desordenado con Agentes.** Gráfico que ilustra la degeneración lógica y arquitectónica de los repositorios de software cuando los agentes omiten fases de planificación e inician refactorizaciones masivas sin control.2  
* **Diapositiva 2: Conceptos Fundamentales del Spec-Driven Development (SDD).** Explicación del ciclo virtuoso de SDD: definición de no-goals y requisitos funcionales detallados antes de generar código, asegurando la consistencia mediante validaciones rigurosas.2  
* **Diapositiva 3: El Ecosistema de Gentleman Dev.** Presentación de las herramientas que componen la suite de código abierto avanzada de Gentleman-Programming: Gentle-AI, el harness de ejecución gentle-pi, y los sistemas de memoria integrada Engram.2  
* **Diapositiva 4: Operación de las Fases SDD.** Diagrama de flujo de los comandos nativos de la metodología (/sdd-init, sdd-explore, sdd-propose, sdd-spec, sdd-design, sdd-tasks, sdd-apply, sdd-verify, sdd-archive).3

#### **Laboratorio Práctico y Experimentación con IA**

Inicialización guiada del flujo SDD en un repositorio local de Node.js o Python utilizando el comando /sdd-init.3 Los participantes analizan la estructura de directorios resultante (openspec/config.yaml, .atl/skill-registry.md) y ejecutan un ciclo de cambio simulado donde la IA genera primero el archivo de especificación detallado de un microservicio y valida sus aserciones antes de escribir las líneas lógicas de negocio.10

#### **Preguntas Clave y Debate**

* ¿Por qué la validación estricta de una especificación detallada escrita en Markdown es un mecanismo más efectivo para asegurar el comportamiento de la IA que la depuración interactiva de código de lenguaje de programación? 2  
* ¿De qué manera las heurísticas de delegación obligatoria de Gentle-AI protegen a los repositorios de cometer errores lógicos de mezcla accidentales de código? 2

## **Módulo IV: Documentación Técnica Avanzada, Sistemas de Memoria y Arquitectura Domain-Driven Design (DDD) (Horas 10-12)**

### **Hora 10: Documentación Técnica de Alta Calidad y Bases de Conocimiento Corporativas**

Se explora el rol clave de la documentación estructurada en formato Markdown como una interfaz representacional que actúa tanto de manual comprensible para el equipo de desarrollo como de mapa contextual para los agentes de inteligencia artificial.11

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Documentación Bidireccional Humano-IA.** Explicación de por qué la documentación corporativa debe estructurarse utilizando sintaxis Markdown con metadatos limpios en formato YAML frontmatter.11  
* **Diapositiva 2: Niveles de Especificación en SDD.** Diagrama que ilustra la jerarquía documental en el desarrollo guiado por especificaciones, desde los objetivos macro del negocio hasta las especificaciones detalladas a nivel de funciones.2  
* **Diapositiva 3: Bases de Conocimiento: Obsidian, Notion y Tolaria.** Comparación de herramientas corporativas analizando el impacto de su estructura en la agilidad de los agentes lectores.11  
* **Diapositiva 4: Tolaria: Arquitectura Documental Descentralizada.** Análisis profundo del paradigma de Tolaria Desktop: principios de primacía del sistema de archivos local, integración nativa con flujos Git, diseño offline-first y el uso de archivos de configuración AGENTS y relations.md para guiar de forma automática el análisis contextual de los agentes de IA.11

#### **Laboratorio Práctico y Experimentación con IA**

Los asistentes crean un repositorio documental en **Tolaria** u **Obsidian** configurando notas de tipo arquitectónico con YAML frontmatter estructurado.11 Ejecutan pruebas locales de lectura de su base documental mediante agentes CLI autónomos, verificando cómo la IA interpreta las relaciones declaradas de forma nativa para sintetizar dependencias lógicas complejas de la infraestructura corporativa.11

#### **Preguntas Clave y Debate**

* ¿Qué ventajas competitivas de privacidad de datos e independencia de plataforma ofrece el enfoque local-first y git-first de Tolaria frente a bases de conocimiento integradas basadas en nubes de terceros cerradas como Notion corporativo? 11  
* ¿Cómo puede el uso de metadatos tipados como "lentes conceptuales" en Tolaria guiar a la IA sin forzar validaciones restrictivas e inflexibles en la base documental? 11

### **Hora 11: Sistemas de Memoria Persistente para Modelos de Lenguaje en MCP**

Esta sesión aborda de manera rigurosa las limitaciones operativas de las ventanas de contexto frente a la pérdida de información por compactación temporal en sesiones de chat prolongadas, introduciendo arquitecturas de memoria persistente para entornos de terminal y servidores MCP.5

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Desafío de la Pérdida de Contexto en Sesiones Prolongadas.** Gráfico técnico que muestra cómo la latencia, el costo por llamadas a la API y el olvido de detalles críticos se disparan a medida que se acumula texto de chat no estructurado.  
* **Diapositiva 2: Engram: Arquitectura de Persistencia Local.** Diagrama de la arquitectura del binario en Go de Engram, mostrando cómo almacena de forma agnóstica decisiones de diseño y correcciones de fallas persistentes utilizando un motor relacional SQLite con búsqueda de texto completo FTS5.9  
* **Diapositiva 3: Codebase-Memory-MCP: Grafos de Conocimiento Indexados.** Ilustración de la solución técnica que realiza análisis estáticos de código en tiempo real, almacenando en bases de datos locales las firmas jerárquicas lógicas de dependencias complejas.5  
* **Diapositiva 4: Integración del Almacén en el Sistema Operativo Local.** Esquema de interacción que explica cómo herramientas como Glia y las interfaces TUI de Engram permiten a los ingenieros auditar, depurar o compartir el historial de memoria cognitiva de sus agentes entre múltiples entornos de forma local o en la nube.9

#### **Laboratorio Práctico y Experimentación con IA**

Instalar localmente el binario en Go de **Engram** y configurar su servidor MCP en un cliente como Claude Code o Cursor.9 Lanzar el servicio de fondo engram serve en puerto local y ejecutar el comando interactivo de terminal engram tui para visualizar en pantalla, a través de su interfaz de consola, cómo el agente guarda y recupera decisiones lógicas automáticas tras interactuar de forma experimental con el repositorio.9

#### **Preguntas Clave y Debate**

* ¿De qué manera el uso de herramientas de indexación estructural de código como Codebase-Memory-MCP reduce el consumo acumulado de tokens de entrada hasta en 120 veces en comparación con la exploración de archivos tradicionales mediante grepping secuencial? 23  
* ¿Cuáles son las implicaciones de implementar una memoria cognitiva agnóstica como Engram para compartir patrones de diseño exitosos entre los diferentes ingenieros del equipo de TI? 9

### **Hora 12: Arquitectura Domain-Driven Design (DDD) y Contratos de APIs**

Se analizan los patrones arquitectónicos de desarrollo orientados a estructurar de forma estricta las dependencias de negocio, facilitando que la IA autogenere implementaciones altamente modulares y libres de acoplamiento rígido.12

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Domain-Driven Design (DDD) como Escudo frente a la IA.** Explicación de cómo la definición estricta de contextos delimitados (Bounded Contexts) evita que los modelos de generación mezclen reglas lógicas de negocio con implementaciones de infraestructura de red o bases de datos.31  
* **Diapositiva 2: Capas de Arquitectura Limpia en DDD.** Gráfico del flujo de llamadas de software estructurado que separa la capa de Dominio pura (entidades y agregados), la capa de Aplicación (casos de uso) y la capa de Infraestructura técnica (bases de datos, controladores HTTP).31  
* **Diapositiva 3: APIs Contract-First.** Explicación de la metodología donde el contrato de la interfaz de comunicación se diseña formalmente antes de escribir cualquier línea de código, sirviendo como mapa inmutable de interconexión del sistema.12  
* **Diapositiva 4: Patrón JSON-First y Herramientas de Colaboración de Contratos.** Uso de herramientas de línea de comandos ágiles para sincronizar, estructurar de forma interactiva y versionar los esquemas y contratos de APIs empresariales de forma legible para humanos y agentes autónomos.12

#### **Laboratorio Práctico y Experimentación con IA**

Utilizar un prompt estructurado (marco GOLD o STAR) para instruir a una IA de generación avanzada a redactar el contrato OpenAPI estructurado (YAML/JSON) de un microservicio financiero corporativo ficticio.6 Una vez validado el contrato, los asistentes guían al agente para compilar automáticamente todo el andamiaje del servidor estructurado en capas limpias de DDD utilizando un lenguaje estructurado como Go o TypeScript.31

#### **Preguntas Clave y Debate**

* ¿Cómo limita la inyección de interfaces de contrato estrictas la generación de código incoherente o redundante por parte de la IA en la capa de transporte de datos? 12  
* ¿Cuáles son las implicaciones de mantenimiento al migrar un sistema monolítico hacia microservicios estructurados en DDD con contratos JSON-First? 12

## **Módulo V: Análisis de Datos (EDA) y Automatización de Procesos con n8n (Horas 13-15)**

### **Hora 13: Análisis Exploratorio de Datos (EDA) Automatizado**

Esta sesión capacita al equipo de TI en la optimización de los flujos analíticos descriptivos, reduciendo drásticamente los tiempos de evaluación inicial de la calidad y distribución de grandes volúmenes de datos tabulares.4

               Pipeline de Análisis Exploratorio (EDA)  
  ┌──────────────────────────────┼──────────────────────────────┐  
  ▼                              ▼                              ▼  
Carga de DataFrame       Análisis de Distribuciones     Evaluación de Calidad  
\- Ingesta de datos       \- Sweetviz (Comparativo) \[13\] \- YData-Profiler (Alertas) \[34\]  
\- Tipado automático      \- Histogramas y Correlaciones  \- Detección de nulos e outliers 

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Rol de la Analítica Descriptiva en TI.** Diagrama conceptual que describe las etapas del flujo general de análisis de datos corporativos, desde la ingesta cruda de datos hasta la generación de valor descriptivo, diagnóstico y predictivo.4  
* **Diapositiva 2: El Concepto del Análisis Exploratorio de Datos (EDA).** Importancia del primer acercamiento analítico sistemático: toma de muestras estadísticas, validación de la calidad, identificación de registros duplicados, nulos y valores atípicos.4  
* **Diapositiva 3: Sweetviz: Visualizaciones Comparativas Rápidas.** Demostración de la biblioteca para compilar informes visuales interactivos enriquecidos, ideal para evaluar de forma comparativa la consistencia lógica entre dos conjuntos de datos independientes.13  
* **Diapositiva 4: YData-Profiler: Diagnósticos de Calidad Exhaustivos.** Análisis de la alternativa avanzada para generar perfiles de datos completos con matrices de correlación multidimensionales, detección de alertas de multicolinealidad y reportes de redundancia sintáctica listos para producción.13

#### **Laboratorio Práctico y Experimentación con IA**

Cargar un archivo masivo de logs o base de datos tabular local corporativo en un entorno de Python. El equipo genera automáticamente informes analíticos completos en formato HTML utilizando **Sweetviz** y **YData-Profiler** de forma local, identificando visualmente variables redundantes, variables con nulos y sesgos de sesgo en las muestras en menos de cinco minutos.13

#### **Preguntas Clave y Debate**

* ¿Qué consideraciones de escalamiento de cómputo y consumo de RAM se deben tener al ejecutar herramientas automáticas de EDA sobre volúmenes masivos de datos en comparación con muestras aleatorias representativas? 4  
* ¿Cómo resolver los desafíos de cumplimiento normativo y privacidad de datos corporativos confidenciales al utilizar estas bibliotecas frente a herramientas en la nube de terceros? 35

### **Hora 14: Data Formulator de Microsoft Research**

Se analiza la herramienta de visualización exploratoria guiada por inteligencia artificial interactiva desarrollada por Microsoft Research, la cual combina interfaces de arrastrar y soltar con flujos conversacionales estructurados basados en agentes.14

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Introducción a Data Formulator.** Presentación de la arquitectura del entorno visual e interactivo de código abierto para transformar datos complejos en conocimiento analítico claro.14  
* **Diapositiva 2: Ingesta Multimodal de Datos No Estructurados.** Cómo el agente de carga estructurado permite extraer información para análisis desde imágenes, capturas de pantalla, archivos estructurados o conexiones web simultáneamente.15  
* **Diapositiva 3: Hilos de Exploración y Sandbox Aislado (Data Threads).** Explicación del flujo donde un agente autónomo ejecuta código de transformación y generación gráfica en un entorno seguro aislado (sandbox), manteniendo el historial contextual ramificado (Branching) para evitar retrocesos costosos.14  
* **Diapositiva 4: Conectores y Estilización Inteligente.** Análisis de la versión 0.7 que incorpora conectores nativos corporativos robustos (PostgreSQL, BigQuery, MySQL, Cosmos, S3) e integra un agente especialista de estilo gráfico (Style-Refinement Agent) para adaptar de manera estética tipografías y paletas mediante lenguaje natural.14

#### **Laboratorio Práctico y Experimentación con IA**

Levantar localmente una instancia del sistema de visualización de **Data Formulator** utilizando el gestor de paquetes rápido de Python uv mediante la instrucción correspondiente 15:

Bash  
uvx data\_formulator

Los ingenieros de TI cargan un archivo de logs técnicos y realizan interacciones conversacionales continuas con el modelo conectado para generar visualizaciones analíticas complejas de rendimiento de red de forma fluida, refinando la estética visual directamente mediante comandos en lenguaje natural.15

#### **Preguntas Clave y Debate**

* ¿Cómo favorece la persistencia estructurada del hilo de conversación (Data Threads) al análisis analítico en comparación con las sesiones de chat lineales tradicionales de ChatGPT? 14  
* ¿Qué valor técnico aporta el aislamiento de la ejecución en sandbox sobre la seguridad integral de la infraestructura del analista en local? 15

### **Hora 15: Automatización de Flujos de Trabajo con n8n**

Esta sesión capacita a los asistentes en la orquestación de flujos de automatización lógicos y reactivos a eventos sin necesidad de escribir código repetitivo de integración de APIs.3

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Paradigma de n8n como Orquestador Técnico.** Diferencias operativas frente a herramientas rígidas cerradas y la importancia de su enfoque autohospedado para preservar la privacidad de los datos empresariales de TI.  
* **Diapositiva 2: Anatomía de un Workflow en n8n.** Análisis de los componentes: disparadores basados en eventos (Webhooks, eventos cron), nodos de procesamiento condicional, transformadores de datos estructurados JSON y conectores de salida.  
* **Diapositiva 3: Conexión nativa con Inteligencia Artificial.** Demostración de los nodos avanzados de n8n que admiten la inserción directa de agentes, memorias persistentes locales, recuperadores vectoriales e interacciones secuenciales con modelos de lenguaje.  
* **Diapositiva 4: Automatización de Tareas de TI.** Ejemplo práctico de un flujo reactivo que captura alertas de caída de base de datos de producción, analiza de forma agéntica los últimos logs y genera automáticamente un ticket de corrección detallado en los sistemas de seguimiento internos de la compañía.

#### **Laboratorio Práctico y Experimentación con IA**

El equipo inicializa un servidor local liviano de n8n. Guiados por el instructor, diseñan un flujo lógico automatizado básico que capture notificaciones a través de un webhook de prueba, procese de manera local la carga JSON del evento y utilice un modelo de lenguaje integrado para categorizar y estructurar la información del log recibido.

#### **Preguntas Clave y Debate**

* ¿Por qué n8n es una plataforma más adecuada para la integración segura de APIs corporativas en comparación con el desarrollo manual de scripts propietarios monolíticos de integración?  
* ¿Cómo estructurar de forma robusta el manejo de errores en n8n para asegurar que las fallas de red de los modelos de IA no rompan la ejecución de los flujos de automatización críticos de la compañía?

## **Módulo VI: Pruebas de Software Agénticas, Gestión de Proyectos con IA y Generación de Frontend (Horas 16-18)**

### **Hora 16: Aseguramiento de Calidad, Pirámide de Pruebas e IA**

Se aborda el aseguramiento de la calidad de software moderno desde una perspectiva agéntica, combinando el desarrollo guiado por comportamiento con la automatización robusta de pruebas continuas de extremo a extremo (E2E).2

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: La IA en el Aseguramiento de la Calidad (QA).** Por qué los modelos de lenguaje reducen el tiempo de cobertura de código lacio y elevan la confiabilidad de las aserciones de pruebas funcionales.2  
* **Diapositiva 2: TDD y BDD con Gherkin en Flujos de Desarrollo Agéntico (SDD).** Integración metodológica donde la especificación lógica del negocio escrita en formato estructurado Gherkin guía la autogeneración del andamiaje de pruebas automatizadas previo a la codificación de la lógica funcional 2:  
  Gherkin  
  Feature: Autenticación de API JSON-First   
    Scenario: Solicitud con contrato válido   
      Given que el cliente envía una trama estructurada válida  
      When realiza el consumo de la interfaz de red  
      Then el sistema valida la firma y responde con código de éxito HTTP 200

* **Diapositiva 3: Pruebas E2E: Selenium frente a Playwright.** Una tabla comparativa detallada que evalúe arquitectura, velocidad de ejecución, confiabilidad de esperas asíncronas de elementos y adecuación para inyecciones automatizadas de código de aserción guiado por agentes de IA.2  
* **Diapositiva 4: Pruebas de Regresión y Generación Autónoma de Casos.** Demostración de cómo los entornos ADE autónomos ejecutan el comando /sdd-init para activar el modo estricto de pruebas unitarias, impidiendo que el software avance a producción sin la validación matemática de sus casos de frontera.3

#### **Laboratorio Práctico y Experimentación con IA**

Los ingenieros de TI utilizan la suite de desarrollo agéntico local para implementar de manera estricta un ciclo TDD en un repositorio experimental.3 Utilizando el generador automático de código de pruebas E2E de Playwright (Codegen), los asistentes registran un flujo interactivo y solicitan a la IA que depure y estabilice el código del script resultante, inyectando aserciones dinámicas para validar respuestas lógicas bajo diferentes escenarios límites de manera asíncrona.3

#### **Preguntas Clave y Debate**

* ¿De qué manera el enfoque de esperas asíncronas nativas del protocolo WebSocket de Playwright reduce el "flakiness" de las pruebas de regresión automatizadas de TI en comparación con la arquitectura tradicional basada en drivers de Selenium WebDriver? 2  
* ¿Qué riesgos se asumen cuando un equipo de QA delega de forma exclusiva la cobertura lógica de código a generadores autónomos de IA sin revisiones explícitas de los casos de frontera por ingenieros senior? 2

### **Hora 17: Gestión de Proyectos de TI Asistida por IA**

Se analiza cómo la inteligencia artificial optimiza las tareas de gestión estratégica de TI, automatizando labores administrativas complejas de alta carga cognitiva, asegurando el cumplimiento normativo público y sintetizando la colaboración ejecutiva.16

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: Automatización de la Gestión de Adquisiciones de TI.** Uso de agentes autónomos para interactuar y consultar bases de conocimiento complejas, agilizando fases de diseño de bases de licitación técnica (RFP, RFQ) y solicitudes de cotizaciones de infraestructura.10  
* **Diapositiva 2: Evaluación Semántica Automática Parcial.** Demostración de flujos de análisis de ofertas técnicas de múltiples proveedores externos en segundos, evaluando precios, plazos de entrega y análisis estructurados de concordancia respecto a los pliegos originales del proyecto corporativo.36  
* **Diapositiva 3: Marco de Cumplimiento Legal y Privacidad.** Análisis riguroso de la guía de la Agencia Española de Protección de Datos (AEPD) para el despliegue ético de IA generativa en la contratación de servicios públicos.16 Explicación técnica de la prohibición estricta de delegar decisiones vinculantes a procesos autónomos ("cajas negras") y la obligación del registro detallado de interacciones.16  
* **Diapositiva 4: Síntesis de Colaboración Ejecutiva.** Integración de ReadAI y herramientas nativas de Microsoft Teams para transcribir reuniones de alta gerencia, abstrayendo planes de acción concretos, responsables, plazos críticos, resúmenes temáticos y niveles de interacción semántica de forma transparente.

#### **Laboratorio Práctico y Experimentación con IA**

El equipo simula un flujo de evaluación técnica corporativa rápida. Cargarán en el contexto de su agente local de IA dos ofertas técnicas de proveedores de infraestructura que compiten en una licitación simulada. Utilizando un prompt estructurado bajo el marco GOLD, instruyen a la IA a realizar una evaluación técnica automatizada parcial, detectando qué propuesta presenta mayor nivel de cumplimiento de requisitos técnicos del pliego formal sugerido, generando la matriz de puntuación final para revisión y validación final por parte del facilitador del curso.6

#### **Preguntas Clave y Debate**

* ¿Cómo asegura la organización el cumplimiento de las normativas de gobernanza de contratación pública (e.g., LCSP en España) al implementar un copiloto de recomendación asistida por IA para la evaluación de ofertas sin violar la transparencia ni delegar la firma administrativa final? 16  
* ¿Qué medidas de seguridad y privacidad se deben configurar de manera obligatoria al habilitar transcripciones y análisis inteligentes de ReadAI en sesiones ejecutivas donde se revelan datos de alta confidencialidad corporativa? 16

### **Hora 18: Generación de Interfaces Frontend y Canales de Comunicación Multimodal**

El curso culmina abordando la aceleración y automatización interactiva en el desarrollo del lado del cliente utilizando editores de diseño modernos de código abierto conectados a través del protocolo Model Context Protocol (MCP).17

#### **Guía Detallada para el Material de Diapositivas (PPT)**

* **Diapositiva 1: El Canal de Diseño a Código de Interfaces.** De las limitaciones cerradas de Figma y sus restricciones de herramientas de generación automáticas pagadas a la apertura de los entornos de código libre y locales-first de desarrollo.17  
* **Diapositiva 2: OpenPencil: El Editor Vectorial Libre.** Presentación de OpenPencil como alternativa abierta que soporta la importación y exportación de archivos nativos de Figma (.fig) utilizando el codificador binario estructurado en Kiwi, permitiendo copiar y pegar elementos bidireccionalmente con total coherencia visual.18  
* **Diapositiva 3: Conexión MCP con Agentes de Programación de Consola.** Explicación detallada de cómo herramientas CLI como Claude Code se conectan al servidor nativo @open-pencil/mcp para leer, modificar y exportar el lienzo visual e interactivo de diseño en local utilizando más de 100 herramientas agénticas tipadas.17  
* **Diapositiva 4: Más Allá de los Modelos de Lenguaje: Visualización Técnica Eficiente.** Introducción al uso coordinado de generadores automáticos de imágenes vectoriales, infografías estructuradas e ilustraciones técnicas para documentar arquitecturas de sistemas complejos.4

#### **Laboratorio Práctico y Experimentación con IA**

Iniciar la aplicación de escritorio local de **OpenPencil**.18 El instructor guía a los ingenieros en el proceso de configuración para conectar el editor con un agente de consola local.17 Mediante comandos de terminal en lenguaje natural, los participantes instruyen a la IA a diseñar de forma interactiva una pantalla de panel de administración corporativo (dashboard) sobre el lienzo de OpenPencil, ejecutando de forma final la conversión del diseño visual a componentes listos para producción en TypeScript con clases estructuradas de Tailwind CSS utilizando la interfaz CLI nativa @open-pencil/cli.17

#### **Preguntas Clave y Debate**

* ¿Cómo cambia la dinámica de colaboración entre diseñadores UX/UI e ingenieros de frontend al utilizar una única fuente de verdad abierta como OpenPencil compatible con el protocolo MCP en local? 17  
* ¿De qué manera la validación visual y las fases de renderizado con IA reducen la brecha tradicional entre las maquetas de diseño gráfico y la implementación final de código web en producción? 39

## **Lineamientos para la Ejecución del Facilitador en el Aula**

La correcta impartición de las 18 horas de este programa técnico por parte del facilitador descansa en la aplicación estricta de las siguientes directrices pedagógicas e institucionales:

### **Enfoque de Aprendizaje Práctico Continuo**

El docente debe evitar las exposiciones teóricas continuas de más de 45 minutos por sesión de clase. El núcleo del curso debe desarrollarse a través de laboratorios técnicos guiados donde la inteligencia artificial local se encuentre activada en todo momento.2 Cada hora lectiva especifica su práctica de laboratorio, y es mandatorio que el docente guíe en tiempo real la ejecución de los comandos y la construcción de prompts correctos utilizando el proyector del aula.8

### **Uso Exclusivo de la Tercera Persona en el Material Visual (PPT)**

Para mantener la formalidad corporativa y el rigor académico que demanda un equipo de tecnología de la información, todas las diapositivas detalladas en esta guía de planificación curricular deben ser redactadas utilizando la voz pasiva impersonal del español (e.g., "se define", "se ejecuta", "se realiza el análisis comparativo").4 El docente (el usuario facilitador) actuará como el director y árbitro de las discusiones, asegurando el cumplimiento de las restricciones en los debates técnicos.2

### **Gobierno Técnico y Gestión de Errores de la IA**

Durante las horas de laboratorio es natural que las llamadas automáticas a las APIs de los modelos devuelvan excepciones de red, de límites de velocidad (rate limits) o generen código erróneo.21 El docente debe utilizar de forma pedagógica estas fallas operativas de los modelos para enseñar a los participantes a aplicar de manera disciplinada el Spec-Driven Development (SDD), forzando a los agentes a leer los logs de compilación rotos, consultar el historial de fallas guardado en la memoria local de Engram y aplicar parches de corrección de diferencias de forma autónoma, simulando los desafíos lógicos cotidianos de un flujo de producción técnica empresarial.2

#### **Obras citadas**

1. Gentleman-Programming/from-chat-to-cognitive-system: De Chat a Sistema Cognitivo — 40-slide presentation on building AI agent systems with SDD orchestration, Engram persistent memory, and modular skills architecture. Gentleman Kanagawa Blur theme. · GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/from-chat-to-cognitive-system](https://github.com/Gentleman-Programming/from-chat-to-cognitive-system)  
2. Gentleman-Programming/gentle-pi: Gentle AI made-to-measure Pi agent \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/gentle-pi](https://github.com/Gentleman-Programming/gentle-pi)  
3. Gentleman-Programming/gentle-ai \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)  
4. PPT \- Resumen de análisis de datos.pptx  
5. Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP \- arXiv, fecha de acceso: junio 30, 2026, [https://arxiv.org/html/2603.27277v1](https://arxiv.org/html/2603.27277v1)  
6. AI Prompt Frameworks | West Virginia School of Osteopathic Medicine, fecha de acceso: junio 30, 2026, [https://www.wvsom.edu/ai/prompt-frameworks](https://www.wvsom.edu/ai/prompt-frameworks)  
7. Prompt Architectures: An Overview of structured prompting strategies | by balaji bal | Medium, fecha de acceso: junio 30, 2026, [https://medium.com/@balajibal/prompt-architectures-an-overview-of-structured-prompting-strategies-05b69a494956](https://medium.com/@balajibal/prompt-architectures-an-overview-of-structured-prompting-strategies-05b69a494956)  
8. Master ChatGPT Prompts: The STAR Method For ChatGPT | Colin Scotland, fecha de acceso: junio 30, 2026, [https://colinscotland.com/the-star-method/](https://colinscotland.com/the-star-method/)  
9. GitHub \- Gentleman-Programming/engram: Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite \+ FTS5, MCP server, HTTP API, CLI, and TUI., fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)  
10. gentle-ai/docs/intended-usage.md at main \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/gentle-ai/blob/main/docs/intended-usage.md](https://github.com/Gentleman-Programming/gentle-ai/blob/main/docs/intended-usage.md)  
11. GitHub \- refactoringhq/tolaria: Desktop app to manage markdown knowledge bases, fecha de acceso: junio 30, 2026, [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)  
12. Development tools \- Lib.rs, fecha de acceso: junio 30, 2026, [https://lib.rs/development-tools](https://lib.rs/development-tools)  
13. Which Auto Visualization tools are more useful in EDA? \- Kaggle, fecha de acceso: junio 30, 2026, [https://www.kaggle.com/discussions/questions-and-answers/477917](https://www.kaggle.com/discussions/questions-and-answers/477917)  
14. Data Formulator \- Microsoft Foundry Labs, fecha de acceso: junio 30, 2026, [https://labs.ai.azure.com/innovations/data-formulator/](https://labs.ai.azure.com/innovations/data-formulator/)  
15. GitHub \- microsoft/data-formulator: Data Formulator is an interactive AI-powered data analysis system makes it easy to connect, explore and visualize data., fecha de acceso: junio 30, 2026, [https://github.com/microsoft/data-formulator](https://github.com/microsoft/data-formulator)  
16. La AEPD apuesta por la IA Generativa: un marco de referencia para la administración pública (y para Gobierto), fecha de acceso: junio 30, 2026, [https://www.gobierto.es/blog/la-aepd-apuesta-por-la-ia-generativa-un-marco-de-referencia-para-la-administracion-publica-y-para-gobierto](https://www.gobierto.es/blog/la-aepd-apuesta-por-la-ia-generativa-un-marco-de-referencia-para-la-administracion-publica-y-para-gobierto)  
17. GitHub \- open-pencil/open-pencil: AI-native design editor. Open-source Figma alternative., fecha de acceso: junio 30, 2026, [https://github.com/open-pencil/open-pencil](https://github.com/open-pencil/open-pencil)  
18. Open-source, AI-native design editor. Figma-compatible, AI-first, fully local. \- OpenPencil, fecha de acceso: junio 30, 2026, [https://open-pencil-open-pencil.mintlify.app/introduction](https://open-pencil-open-pencil.mintlify.app/introduction)  
19. OpenPencil \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/open-pencil](https://github.com/open-pencil)  
20. Prompting \- Generative Artificial Intelligence \- USMA Library Homepage at U.S. Military Academy, fecha de acceso: junio 30, 2026, [https://library.westpoint.edu/GenAI/prompting](https://library.westpoint.edu/GenAI/prompting)  
21. Issue with the Prompt and the framework : r/PromptEngineering \- Reddit, fecha de acceso: junio 30, 2026, [https://www.reddit.com/r/PromptEngineering/comments/1q110iv/issue\_with\_the\_prompt\_and\_the\_framework/](https://www.reddit.com/r/PromptEngineering/comments/1q110iv/issue_with_the_prompt_and_the_framework/)  
22. Data Formulator 0.7: AI-powered data analytics for enterprise data \- Microsoft Research, fecha de acceso: junio 30, 2026, [https://www.microsoft.com/en-us/research/blog/data-formulator-0-7-ai-powered-data-analytics-for-enterprise-data/](https://www.microsoft.com/en-us/research/blog/data-formulator-0-7-ai-powered-data-analytics-for-enterprise-data/)  
23. I built an MCP server that gives Claude Code a knowledge graph of your codebase — in average 20x fewer tokens for code exploration : r/ClaudeAI \- Reddit, fecha de acceso: junio 30, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1rp6pkr/i\_built\_an\_mcp\_server\_that\_gives\_claude\_code\_a/](https://www.reddit.com/r/ClaudeAI/comments/1rp6pkr/i_built_an_mcp_server_that_gives_claude_code_a/)  
24. I built an MCP server that gives coding agents a knowledge graph of your codebase — in average 20x fewer tokens for code exploration : r/codex \- Reddit, fecha de acceso: junio 30, 2026, [https://www.reddit.com/r/codex/comments/1rp9ks1/i\_built\_an\_mcp\_server\_that\_gives\_coding\_agents\_a/](https://www.reddit.com/r/codex/comments/1rp9ks1/i_built_an_mcp_server_that_gives_coding_agents_a/)  
25. agent-teams-lite/examples/antigravity/sdd-orchestrator.md at main \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/agent-teams-lite/blob/main/examples/antigravity/sdd-orchestrator.md](https://github.com/Gentleman-Programming/agent-teams-lite/blob/main/examples/antigravity/sdd-orchestrator.md)  
26. GitHub \- Gentleman-Programming/Gentleman-Skills: Community-driven AI agent skills for Claude Code, OpenCode, and other AI assistants. Curated patterns and community contributions., fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/Gentleman-Skills](https://github.com/Gentleman-Programming/Gentleman-Skills)  
27. agent-teams-lite/skills/sdd-init/SKILL.md at main \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/agent-teams-lite/blob/main/skills/sdd-init/SKILL.md](https://github.com/Gentleman-Programming/agent-teams-lite/blob/main/skills/sdd-init/SKILL.md)  
28. gentle-ai/docs/components.md at main \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/Gentleman-Programming/gentle-ai/blob/main/docs/components.md](https://github.com/Gentleman-Programming/gentle-ai/blob/main/docs/components.md)  
29. tolaria/docs/ARCHITECTURE.md at main \- GitHub, fecha de acceso: junio 30, 2026, [https://github.com/refactoringhq/tolaria/blob/main/docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/main/docs/ARCHITECTURE.md)  
30. Tolaria, fecha de acceso: junio 30, 2026, [https://tolaria.md/](https://tolaria.md/)  
31. How can I avoid transposing one implementation of a structure in to another? \- Reddit, fecha de acceso: junio 30, 2026, [https://www.reddit.com/r/golang/comments/1dqotvi/how\_can\_i\_avoid\_transposing\_one\_implementation\_of/](https://www.reddit.com/r/golang/comments/1dqotvi/how_can_i_avoid_transposing_one_implementation_of/)  
32. Authentication — list of Rust libraries/crates // Lib.rs, fecha de acceso: junio 30, 2026, [https://lib.rs/authentication](https://lib.rs/authentication)  
33. AWS Certified Data Engineer Exam Insights | PDF | Amazon Web Services \- Scribd, fecha de acceso: junio 30, 2026, [https://www.scribd.com/document/981411348/AWS-Certified-Data-Engineer-Associate-DEA-C01-152%E9%A2%98](https://www.scribd.com/document/981411348/AWS-Certified-Data-Engineer-Associate-DEA-C01-152%E9%A2%98)  
34. Streamlining Data Exploration: A Comparison of Profiling Tools for Effective EDA \- dataroots, fecha de acceso: junio 30, 2026, [https://dataroots.io/blog/streamlining-data-exploration-a-comparison-of-pandas-profiler-sweet-viz-and-pandas-gui-for-effective-eda](https://dataroots.io/blog/streamlining-data-exploration-a-comparison-of-pandas-profiler-sweet-viz-and-pandas-gui-for-effective-eda)  
35. Comparing the Five Most Popular EDA Tools \- Towards Data Science, fecha de acceso: junio 30, 2026, [https://towardsdatascience.com/comparing-five-most-popular-eda-tools-dccdef05aa4c/](https://towardsdatascience.com/comparing-five-most-popular-eda-tools-dccdef05aa4c/)  
36. Agentes IA | Wherex, fecha de acceso: junio 30, 2026, [https://wherex.com/sourcing/agentes-ia/](https://wherex.com/sourcing/agentes-ia/)  
37. Inteligencia artificial industrial para Polarion \- Siemens, fecha de acceso: junio 30, 2026, [https://www.siemens.com/es-es/products/polarion/industrial-ai/](https://www.siemens.com/es-es/products/polarion/industrial-ai/)  
38. Plataforma de Gestión de Procurement con IA \- Verdana, fecha de acceso: junio 30, 2026, [https://www.verdana.app/gestion-de-terceros/plataforma-de-gestion-de-procurement-con-ia/](https://www.verdana.app/gestion-de-terceros/plataforma-de-gestion-de-procurement-con-ia/)  
39. I tried an open-source Figma alternative, and its AI does what Figma's can't, fecha de acceso: junio 30, 2026, [https://www.xda-developers.com/ditched-figma-for-open-source-tool-ai-does-what-figma-cant/](https://www.xda-developers.com/ditched-figma-for-open-source-tool-ai-does-what-figma-cant/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE4AAAAaCAYAAAAZtWr8AAADDUlEQVR4Xu2YWahNURjHP/M8Zs5wiZQ5Qx4MHUQehJdrTMIb4kmJJ+WJKJlepGsoyZCpJHOK8EyRukVkKsODQuL/79v77nW+s8/e+xy3fe6u/atf957v+/bZa6+z9lp7bZGcnJycVGkHz8MhNpGAXvAS7G4TWaYOHoYv4F/4EI5xCzxYs9QGK2AevAHb2EQWGQnfw6+wHl4X7bwLbhFYBS+aWDUch9ttMIscFO0ojiay2/u8o6lCpDV8Cxc6sWqZDj/ATjaRNc6KdtQuJzbC+Z8shq9gKxOvlka42Qazxjkp7TjLKdGR2Vw0wNs2GAYbxca5cqIk+5wY55k04flsu84UVShcNOwIYfvtsRvhABP75B/gsAF+s8EwhovOD79Ev+yE6PJMODk/h0fhLC9WjgNS2tgo7+thZeH57ojWXoUFONYtAD1E80tMnO0vwL0SnG8BbA8fwZdwLpzp1bvMFq1nJyeCQ54HvBadcMkk+BsO9otSxr9Vj9mEx0TRPC82DF7HTdGaZ3An/AEnu0WGCaL142yiHDMk+HU44RI2mB1aK+I6bppofrxNOAwUXSn9a7O3tWWoaF3BxCN5KnrQNdhX9NfhEl0r4jrOH3H8G8VKCTou7iGZdxfr/Hk+EeslOMER+KA4HUmlc9xdPSySuI7j9or5crcq6SA6V34RreXfOrfAwFuUdVNtIgqe5LMEF7e8OJ06cR3XRTS/yCYc9ovO28MkWGweiy4UYXDBYE0/m4jDX4newLYmlyYFKV1Vezp5n0a41cT6i9bzDuLits6LT4F/RL+TdxRr+ng5n7Xwo4klgo8g/PJtNpEy/qh3LbgFHtxfnjax1VJ8HEduWJzaR5lD8IqJhcKtCpdgf+hyS/MddmuqaNlwNHGE8LVSc/AErrDBMLaI9vxl7/MeeDJIt3j4Do1vUJbZRBWMgu8k4RTFNw33YEe4RnSrM9otyACbRB+h/pcG0TkuEV1Fn65/ij5dx22tWiLcIfB93HybqIA5UtuH/ZrBd2hcBAbZRAJ6w1uws03k5ORkmn8IttCX6iaKVgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAZCAYAAABtnU33AAACn0lEQVR4Xu2XS6hNYRTH/97yiOsRRqKUZ2FAHqVQHqXMFPIoBoRLHpFSlDwyYSBFOUh5DYQUyitkIGVuRElmCGXC/2/tfc+31977O+feOpT2r37dzlrr7rPX3d/69neBior/lmn0Kr1Dr9FttEemorWMpy9pX58IuE1/RXxP2zuqI4yiT+jY5HM3eoue6qhoPYuRbyB0fVLXnb5KYiOSmOhNtyTxGqyHUg7R3S42jv6kA1y8VWxCvsnUt7RfvRRPk/iwIJbyEJZb5RMhF+gVFxsK+0X9/Bsco8tdTCN1ky5y8VjD52C5/T4RchBWdB31GdoJ+7JGaPYm+GDAcDrbBws4QAe72D56xMVErOHnsNw8nwjR8v0GK3xD99AXdGRYVIIauk9H+wQZApu3KT7RBBPpMxRvnEUN96Fnk/jWIF7KfPoZ9bk5QXtmKsoZA5udQUFMN6odX9ftCnfpah9MSBt+RB8kfqDf6Q402LBSjsOWtuY5bfp8piKOlq2+WE2r2Ut0ZaaieabSTyj/gxc9YTW5kX6F/aF7BbkcGvBa8HkObGfURZcF8UbMhTV9ka7LpjpFDXadMooaTtHeo5weYCFt9Aud7uJapoofdvEYeiL36GvY/HYFXUNPKXYGiDWs/UI53XvhCpkMK+jvE7BledQHS9DFb9ANdCZ9jOxMN8sM2P1ohy4j1nDaj9RhJMdA+oMu8QnYRrTUBwvQzF6GvUtTZsF27842rSOtbna7TwTEGt4Ly8VG4s8p5yNdAzu66XS1C/aEm0Ezexr53XEB7OaKVk8Zmj3d8GafCNCZWzXh0VIshL1e39FJLpdDm5MOGrqYDukrsulSVHcS+WZT9GrR7t8sa2ErThunp9E/D3otnUHxk6+oqKioqKj4x/wG53ugg2Et9lcAAAAASUVORK5CYII=>