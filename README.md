# ASM-PyPas 🚀

ASM-PyPas es un intérprete experimental con interfaz web. El proyecto combina:

- 🌐 Backend en Flask para servir la interfaz y exponer una API.
- 🧠 Motor de interpretación en Python (tokenización, estructuras y ejecución básica).
- 📝 Editor web con CodeMirror para crear, guardar y ejecutar archivos dentro de la carpeta codes.

## ✨ Estado actual

Actualmente puedes:

- 📁 Crear y eliminar archivos de código desde la UI.
- 🔄 Cargar archivos existentes al abrir la aplicación.
- 💾 Guardar cambios automáticamente cada segundo cuando detecta modificaciones.
- ▶️ Ejecutar código vía API y visualizar resultado/errores en la terminal integrada.

## 🏗️ Arquitectura

- ⚙️ main.py: arranque del servidor Flask.
- 🧩 modules/interpreter: lógica del lenguaje (tokens, expresiones, estructuras y ejecución).
- 🔌 modules/web: rutas web, API, validaciones de payload y utilidades.
- 🖥️ gui: frontend estático (HTML, CSS, JS, CodeMirror).
- 📂 codes: archivos fuente editables desde la interfaz.

## 🌳 Estructura del repositorio

```text
asm-pypas/
├── main.py
├── README.md
├── requirements.txt
├── codes/
├── docs/
├── gui/
├── modules/
│   ├── generic/
│   ├── interpreter/
│   └── web/
└── scripts/
```

## 📋 Requisitos

- 🐍 Python 3.10+ (recomendado).
- 📦 pip.

Dependencias actuales en requirements.txt:

- ✅ flask

## 🛠️ Instalación

```bash
git clone https://github.com/VIRUSGAMING64/Interpreter.git
cd Interpreter

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Ejecución

Opción 1 (directo):

```bash
python3 main.py
```

Opción 2 (script):

```bash
bash scripts/run.sh
```

El servidor inicia en:

- 🌍 http://127.0.0.1:8000
- 🌍 http://localhost:8000

## 🔄 Flujo de uso

1. Abre la aplicación en el navegador.
2. Crea un archivo nuevo con el botón +.
3. Escribe código en el editor.
4. El contenido se guarda automáticamente en segundo plano.
5. Ejecuta con el botón Play para ver salida y errores en la terminal inferior.

## 🔗 API disponible

Rutas principales expuestas por Flask:

- GET /: interfaz principal.
- GET /gui/<subpath>: recursos estáticos de la UI.
- POST /api/run: ejecuta el archivo actual. Body JSON: {"name": string, "code": string}.
- POST /api/save: guarda el archivo actual. Body JSON: {"name": string, "code": string}.
- POST /api/getcode?name=<archivo>: obtiene el contenido de un archivo.
- GET /api/getcodes?name=<archivo>: obtiene contenido de un archivo.
- GET /api/initcodes: lista nombres disponibles en codes.
- GET /api/newcode?name=<archivo>: crea entrada de archivo vacía.
- GET /api/delcurr?name=<archivo>: elimina un archivo.

Notas técnicas:

- 🛡️ Se valida nombre de archivo para prevenir path traversal.
- 📏 Tamaño máximo de código por request: 128 MB.

## 🧰 Scripts útiles

- 🚀 scripts/run.sh: ejecuta la app con optimizaciones y luego limpia temporales.
- 🧹 scripts/clean.sh: elimina archivos auxiliares log/aux y __pycache__.
- 📚 scripts/builddocs.sh: compila documentos LaTeX en docs y limpia temporales.

## 📖 Documentación

La documentación técnica del lenguaje/proyecto está en la carpeta docs.

## ⚠️ Limitaciones actuales

- El intérprete está en evolución y no cubre todas las construcciones de un lenguaje completo.
- Algunos mensajes de error y resultados aún están orientados a depuración.
- No hay suite formal de tests automatizados incluida en este repositorio.
