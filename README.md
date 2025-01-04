# M7-L4-ClavesPrimariasCRUD_03-01-2025
Proyecto educativo

# Django CRUD Project: Students & Courses

Este proyecto es una aplicación web desarrollada con Django que implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de **Estudiantes** y **Cursos**.

## 📚 **Características del Proyecto**

- **Gestión de Estudiantes:** Permite crear, leer, actualizar y eliminar estudiantes.
- **Gestión de Cursos:** Permite crear, leer, actualizar y eliminar cursos.
- **Interfaz Amigable:** Plantillas HTML para interactuar con los datos.
- **Relaciones entre Tablas:** Los estudiantes están relacionados con cursos mediante una relación de clave foránea.

---

## 🛠️ **Tecnologías Utilizadas**

- **Python 3.x**
- **Django 4.x**
- **SQLite3 (Base de datos por defecto de Django)**
- **HTML5 y CSS3**

---

## 🚀 **Instalación y Configuración**

Sigue los siguientes pasos en la terminal para configurar el proyecto:

### 1. **Clonar el repositorio**
```bash
$ git clone https://github.com/tu_usuario/tu_repositorio.git
$ cd tu_repositorio
```

### 2. **Crear un entorno virtual**
```bash
$ python -m venv venv
$ source venv/bin/activate   # En Linux/Mac
$ .\venv\Scripts\activate   # En Windows
```

### 3. **Instalar dependencias**
```bash
$ pip install -r requirements.txt
```

### 4. **Aplicar Migraciones**
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. **Crear un superusuario**
```bash
$ python manage.py createsuperuser
```

### 6. **Ejecutar el servidor**
```bash
$ python manage.py runserver
```

Abre tu navegador y visita: **http://127.0.0.1:8000/**

---

## 📝 **CRUD de Students**

### 1. **Crear un Estudiante**
- URL: `/student/create/`
- Método: `POST`
- Descripción: Permite crear un nuevo estudiante mediante un formulario.

### 2. **Leer Todos los Estudiantes**
- URL: `/`
- Método: `GET`
- Descripción: Muestra una lista de todos los estudiantes.

### 3. **Leer un Estudiante en Detalle**
- URL: `/student/<int:pk>/`
- Método: `GET`
- Descripción: Muestra los detalles de un estudiante específico.

### 4. **Actualizar un Estudiante**
- URL: `/student/<int:pk>/update/`
- Método: `POST`
- Descripción: Permite actualizar los datos de un estudiante.

### 5. **Eliminar un Estudiante**
- URL: `/student/<int:pk>/delete/`
- Método: `POST`
- Descripción: Permite eliminar un estudiante de la base de datos.

---

## 📝 **CRUD de Courses**

### 1. **Crear un Curso**
- URL: `/course/create/`
- Método: `POST`
- Descripción: Permite crear un nuevo curso mediante un formulario.

### 2. **Leer Todos los Cursos**
- URL: `/course/list`
- Método: `GET`
- Descripción: Muestra una lista de todos los cursos.

### 3. **Leer un Curso en Detalle**
- URL: `/course/<int:pk>/`
- Método: `GET`
- Descripción: Muestra los detalles de un curso específico.

### 4. **Actualizar un Curso**
- URL: `/course/<int:pk>/update/`
- Método: `POST`
- Descripción: Permite actualizar los datos de un curso.

### 5. **Eliminar un Curso**
- URL: `/course/<int:pk>/delete/`
- Método: `POST`
- Descripción: Permite eliminar un curso de la base de datos.

---

## 🔑 **Acceso al Panel de Administración**

- URL: **http://127.0.0.1:8000/admin/**
- Usuario: *(El usuario que creaste en createsuperuser)*

---

## 🐍 **Estructura del Proyecto**
```
crud/
├── app1/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── templates/app1/
├── app2/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── templates/app2/
├── crud/
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── requirements.txt
```

---

## 🐛 **Problemas Comunes**

- Si encuentras errores con migraciones, prueba:
```bash
$ python manage.py makemigrations
$ python manage.py migrate --fake
```

- Si el servidor no arranca, verifica que tu entorno virtual esté activado.

---

## 🤝 **Contribuciones**
¡Las contribuciones son bienvenidas! Si deseas colaborar, abre un **Pull Request** o crea un **Issue**.

---

## 📄 **Licencia**
Este proyecto está bajo la licencia **MIT**.

---

**¡Gracias por revisar este proyecto! 😊**