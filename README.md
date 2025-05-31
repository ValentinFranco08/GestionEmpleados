# 🧑‍💼 Sistema de Gestión de Empleados

Este proyecto es una aplicación web desarrollada con **Flask** y **Bootstrap 5** para gestionar empleados de una organización. Permite registrar, editar, eliminar y visualizar empleados, diferenciando roles como **Empleado**, **Desarrollador** y **Gerente**.

## 📸 Captura de pantalla

![image](https://github.com/user-attachments/assets/2be8820d-eb1e-4f0c-b803-f3c269fa52ca)

---

### 👥 Gestión de Empleados
- 🆕 Registro de nuevos empleados con diferentes roles
- ✏️ Edición completa de información
- 🗑️ Eliminación segura con confirmación
  

### 🎨 Interfaz Moderna
- 🌙/☀️ Modo oscuro/claro persistente
- 📱 Diseño 100% responsive
- 🎨 UI intuitiva con Bootstrap 5
- 📊 Visualización de estadísticas

### ⚙️ Funcionalidades Técnicas
- 🗄️ Base de datos SQLite
- ⚡ ORM con SQLAlchemy

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.10+**
- **Flask 2.3.x** - Microframework web
- **SQLAlchemy 2.0** - ORM para base de datos
  

### Frontend
- **Bootstrap 5.3** - Diseño responsive
- **Bootstrap Icons** - Librería de iconos
- **Vanilla JavaScript** - Interactividad
- **CSS3** - Estilos personalizados

### Base de Datos
- **SQLite** - Base de datos embebida
---

## 🛠️ Requisitos previos

* Python 3.x instalado
* Git (opcional para clonar el repositorio)

---

## 📦 Instalación y uso

1. **Clonar el repositorio**

```bash
git clone https://github.com/ValentinFranco08/GestionEmpleados.git
cd GestionEmpleados
```

2. **Crear entorno virtual (recomendado)**

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

5. **Ejecutar la aplicación**

```bash
python3 app.py
```

La app estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📝 Estructura del proyecto

```
GestionEmpleados/
│
├── static/
│   ├── css/
│   │   ├── empleados.css
│   │   └── dark-mode.css
│   └── main.js
│
├── templates/
│   ├── index.html
│   ├── agregar.html
│   └── editar.html
│
├── models/
│   ├── desarrolador.py
│   ├── empleado.py
│   ├── __init__.py
│   └── gerente.py
├── app.py
└── README.md
```

---

