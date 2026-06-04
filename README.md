# cryton2

<p align="center">
  <strong>Un intérprete experimental con backend en Python y una interfaz web moderna para el desarrollo ágil.</strong>
</p>

---

## Descripción

Un simple interpreter (proposito educativo solamente)

## Características Principales

- **Núcleo Propio:** Implementación completa de Lexer, Parser y Árbol de Sintaxis Abstracta (AST).
- **Interfaz Web:** Editor de código integrado con resaltado de sintaxis (CodeMirror).
- **Persistencia:** Sistema de guardado y carga de snippets en el servidor.
- **Ejecución en Tiempo Real:** Feedback inmediato de la ejecución del código a través de una API REST.
- **Herramientas de Build:** Scripts automatizados para la generación y limpieza del frontend.

## Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python 3.10+ & Flask |
| **Frontend** | React, Tailwind CSS |
| **Editor** | CodeMirror |
| **Persistencia** | Filesystem (JSON/Plain Text) |
| **Contenedor** | Docker |

## Inicio Rápido

### Requisitos Previos

- Python 3.10 o superior
- Pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/VIRUSGAMING64/asm-pypas.git
   cd asm-pypas
   ```

2. **Configurar el entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

Simplemente ejecuta el script principal:
```bash
python3 main.py
```
O utiliza los scripts de automatización:
```bash
bash scripts/run.sh
```

Accede a la interfaz en: `http://localhost:8000`

## Referencia de la API

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/api/run` | Ejecuta el código enviado. |
| `POST` | `/api/save` | Guarda el contenido en un archivo. |
| `GET` | `/api/getcode` | Obtiene el contenido de un snippet. |
| `GET` | `/api/initcodes` | Lista todos los archivos disponibles. |
| `GET` | `/api/newcode` | Crea un nuevo archivo vacío. |
| `GET` | `/api/delcurr` | Elimina el archivo especificado. |
| `GET` | `/api/kill` | Detiene la ejecución actual. |

## Estructura del Proyecto

Este proyecto sigue una estructura modular para facilitar el desarrollo y mantenimiento:

-   `main.py`: El punto de entrada principal de la aplicación. Configura y arranca el servidor Flask.

-   `modules/`: Contiene la lógica central del backend, dividida en submódulos:
    -   `interpreter/`: El corazón del intérprete. Incluye:
        -   `Lexer.py`: Encargado del análisis léxico, transformando el código fuente en tokens.
        -   `ExprParser.py`: Implementa el parser para construir el Árbol de Sintaxis Abstracta (AST).
        -   `structures.py`: Define las estructuras de datos usadas durante la interpretación (ej. para variables, funciones).
        -   `memory/`: Gestión de la memoria del intérprete.
        -   `builtin/`: Implementaciones de funciones y operadores predefinidos del lenguaje.
        -   `auxiliar/`: Utilidades internas y valores estáticos para el intérprete.
    -   `web/`: Módulos relacionados con la capa web y la API REST.
        -   `index.py`: Define las rutas principales del servidor Flask.
        -   `api/endpoints.py`: Maneja los endpoints de la API para interacción con el intérprete y gestión de código.
        -   `core/`: Contiene utilidades para la configuración, manejo de errores y persistencia (ej. `saver.py`).

-   `gui/`: La carpeta fuente del frontend, desarrollada con React y JSX.
    -   `index.jsx`: El componente principal de la aplicación React.
    -   `app/`: Contiene los estilos, assets y componentes reutilizables del frontend.
        -   `components/`: Componentes React como `Button.jsx` y `Saves.jsx`.
        -   `libs/`: Librerías de terceros como CodeMirror (editor de código) e Iconfont (iconos).

-   `guic/`: La salida generada y compilada del frontend a partir de `gui/`, lista para ser servida por el servidor Flask.

-   `codes/`: Directorio donde se almacenan los snippets de código que los usuarios crean y guardan a través de la interfaz web.

-   `scripts/`: Contiene scripts de automatización para diversas tareas:
    -   `run.sh`: Script principal para levantar el entorno de desarrollo.
    -   `buildpage.sh`: Script para compilar el frontend (`gui/` a `guic/`).
    -   `clean`: Scripts para limpiar artefactos generados.
    -   `interpreter_extreme_tests.py`: Pruebas de estrés para el intérprete.

-   `tests/`: Directorio para pruebas unitarias y de integración del backend.

-   `requirements.txt`: Lista de dependencias de Python necesarias para el proyecto

-   `Dockerfile`: Archivo para construir la imagen Docker de la aplicación.

## Roadmap

- [ ] Implementar límites de tiempo (timeouts) para ejecuciones.
- [ ] Expandir la gramática del lenguaje soportado.
