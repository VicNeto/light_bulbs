# light_bulbs

# Instalación

## Clonar el repositorio

## Crear ambiente virtual
- Crear un ambiente virtual para evitar un posible conflicto con versiones de los paquetes previamente instaldas.

En entornos unix se puede crear un ambiente virtual usando virtualenv fácilmente.

- virtualenv env
- source /env/bin/activate

## Instalar requerimientos
Una vez creado y activado el ambiente virtual, moverse a a carpeta del proyecto clonado y posteriormente instalar los requerimientos.

- cd light_bulbs
- pip install -R requirements.txt

# Correr al programa
Instalados los requerimientos, simplemente correr el archivo app.py, esto iniciará una aplicación Flask

- python app.py

## Revisar respuesta
Abrir un navegador e ir a la dirección http://localhost:5000

# Cambiar la matriz
Simplemente hay que sobreescribir el archivo room.txt con la matriz de unos y ceros a evaluar.
