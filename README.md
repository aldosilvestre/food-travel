# food-travel
Aplicación de tour de comidas para curso python

# Getting stared

## Instalacion
### Requisitos
- Mongo DB
- Mongo Compass
- Python
- Pip
- Python IDE
- Opcional (Docker o Podman) *Se puede descargar la imagen de mongo, y evitar instalar el servidor local*

## Correr Aplicación

  1. Levantar base de datos
  2. Levantar aplicacion
      - (shell)
        
             python -m venv .
             source bin/activate
             python app/App.py

      - (IDE)
          Posicionarse en el archivo App.py y presionar ejecutar.

  3. Crear un usuario administrador en la base de datos. La coleccion es UserLogin y no requiere tener la contraseña hasheada. Ej

         {
          "id": "cb41dc41-7e88-4280-8e0b-9e168cafe877",
          "name": "Aldo",
          "last_name": "Silvestre",
          "password": "123456",
          "is_admin": true,
          "username": "asilvestre"
          }

## Dependencias
![image](https://github.com/aldosilvestre/food-travel/assets/64880747/d6fcff2c-9936-4b54-b231-05705a05f520)


# Capturas

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/bd7a3d7d-4939-4980-936e-3a41c3696ab8)

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/d6faf02b-3804-4d20-920c-e7b8e2f483fa)

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/74129f28-1773-4604-a34c-3e4ab5cc86e8)

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/b5f93765-03ce-4ada-bf4f-b358c784d766)

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/696fd2af-8abe-4dcc-a27c-83ac41a2fabd)

![image](https://github.com/aldosilvestre/food-travel/assets/64880747/33bd0436-9d44-4575-8da7-4939abf1587f)

# Notas

- *La aplicacion no se penso con fines productivos, con lo cual la misma sufre de falta de validaciones, encripaciones y erroes, tampoco se contemplo el clean code ni clean architecture.*
- *La aplicacion contiene errores que se iran solucionando en proximas versiones*

