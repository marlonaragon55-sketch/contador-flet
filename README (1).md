# Contador interactivo con Flet

**Asignatura:** Programación Orientada a Objetos
**Tema:** Interfaces gráficas y programación orientada a eventos
**Autor:** Marlon Aragon Ponce — Corporación Universitaria Americana
**Biblioteca investigada:** [Flet](https://flet.dev/docs) (Python)

## Descripción

Flet es una biblioteca de Python para construir interfaces gráficas sin necesidad de experiencia en desarrollo frontend. Sus controles (botones, textos, campos de entrada, etc.) están basados en widgets de Flutter y permiten crear aplicaciones de escritorio, web y móviles con el mismo código.

Este repositorio contiene una aplicación mínima: un **contador** que inicia en cero y aumenta cada vez que el usuario presiona un botón. Incluye dos versiones:

| Archivo | Descripción |
|---|---|
| `main.py` | Versión básica con una función que responde al evento |
| `main_poo.py` | Versión con programación orientada a objetos (reto adicional) |

## Instalación

Requisito: tener Python instalado (consulta la versión mínima en la [guía oficial de instalación](https://flet.dev/docs/getting-started/installation)).

```bash
# 1. Clonar el repositorio
git clone https://github.com/marlonaragon55-sketch/contador-flet.git
cd TU_REPOSITORIO

# 2. Crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

# 3. Instalar dependencias
pip install -r requirements.txt
```

> El archivo `requirements.txt` fija la versión de Flet (`flet==0.28.3`), porque la API de la biblioteca ha cambiado entre versiones y así el código funciona igual en cualquier equipo.

## Ejecución

```bash
python main.py        # versión básica
python main_poo.py    # versión con POO
```

También se puede ejecutar como aplicación web:

```bash
flet run --web main.py
```

## Captura de pantalla

![Aplicación funcionando](capturas/captura.png)

## Explicación del ejemplo

### 1. ¿Cómo se crea la ventana principal?
Con `ft.app(target=main)`. Flet inicia la aplicación y le entrega a la función `main` un objeto `Page`, que representa la ventana. Desde ese objeto se configuran propiedades como el título (`page.title`) y la alineación del contenido.

### 2. ¿Cómo se crean y muestran los componentes gráficos?
Se crean como objetos: un `ft.Text` que muestra el valor del contador y un `ft.ElevatedButton` que el usuario puede presionar. Luego se muestran en la ventana con `page.add(...)`.

### 3. ¿Qué evento se implementó y cómo se detecta?
El evento es el **clic del usuario sobre el botón**. Se detecta asignando una función a la propiedad `on_click` del botón:

```python
boton = ft.ElevatedButton("Sumar 1", on_click=incrementar)
```

### 4. ¿Qué función o método responde al evento?
La función `incrementar(e)` en `main.py` y el método `incrementar(self, e)` de la clase `Contador` en `main_poo.py`. El parámetro `e` contiene la información del evento.

### 5. ¿Cómo se modifica la interfaz después de la interacción?
Dentro del manejador se cambia el valor del texto y se llama a `update()` para que Flet redibuje el control:

```python
contador.value = str(int(contador.value) + 1)
page.update()
```

## Funcionamiento del evento

```
Usuario hace clic en "Sumar 1"
        │
        ▼
Flet detecta el evento on_click
        │
        ▼
Se ejecuta incrementar(e)
        │
        ▼
Se actualiza contador.value
        │
        ▼
page.update() → la pantalla muestra el nuevo número
```

## Reto adicional: programación orientada a objetos

Flet permite construir interfaces con clases y objetos: se puede **heredar de un control existente** (por ejemplo `ft.Column`) para crear controles personalizados y reutilizables. En `main_poo.py` la clase `Contador` hereda de `ft.Column`.

### Responsabilidades de cada clase / componente

| Clase / función | Responsabilidad |
|---|---|
| `Contador` (hereda de `ft.Column`) | Guarda el estado (`valor`), construye sus propios componentes (texto y botones) y define los métodos que responden a los eventos (`incrementar`, `reiniciar`) |
| `ft.Text`, `ft.ElevatedButton`, `ft.OutlinedButton` | Componentes gráficos de Flet que muestran información y reciben las acciones del usuario |
| `main(page)` | Configura la ventana (`Page`) y agrega el control `Contador` |

## Ventajas y limitaciones frente a Tkinter

**Ventajas**
- Apariencia moderna sin configuración adicional.
- Un mismo código sirve para escritorio, web y móvil.
- Código de interfaz corto y legible.

**Limitaciones**
- Biblioteca más joven; su API ha cambiado entre versiones.
- Requiere instalación (`pip install flet`), mientras que Tkinter viene incluida con Python.
- Depende de un motor basado en Flutter que se descarga en el primer uso.

## Fuentes consultadas

- Documentación oficial de Flet: https://flet.dev/docs
- Guía de instalación: https://flet.dev/docs/getting-started/installation
- Referencia de controles: https://flet.dev/docs/controls
- Página de Flet en PyPI: https://pypi.org/project/flet/
- Repositorio oficial de Flet: https://github.com/flet-dev/flet
