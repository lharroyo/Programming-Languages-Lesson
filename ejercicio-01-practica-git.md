# Ejercicio Práctico: Gestión de un Proyecto con Git

**Objetivo:** Aplicar los conceptos del taller en un escenario realista  
**Tiempo estimado:** 30-45 minutos

---

## Escenario

Se requiere crear un repositorio para un proyecto web simple. El proyecto contendrá una página HTML básica y deberá gestionarse con control de versiones.

---

## Parte 1: Configuración Inicial

Verificar que Git esté configurado correctamente ejecutando:

```
git config user.name
git config user.email
```

Si no hay respuesta, configurar con los datos personales.

---

## Parte 2: Creación del Repositorio

1. Crear una carpeta llamada `proyecto-web` en el escritorio o ubicación preferida

2. Acceder a la carpeta desde la terminal

3. Inicializar el repositorio Git

4. Verificar que se creó el directorio `.git`

---

## Parte 3: Primer Commit

1. Crear un archivo `index.html` con el siguiente contenido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Proyecto</title>
</head>
<body>
    <h1>Bienvenido</h1>
    <p>Este es mi primer proyecto con control de versiones.</p>
</body>
</html>
```

2. Verificar el estado del repositorio

3. Agregar el archivo al área de preparación

4. Crear el commit con un mensaje descriptivo

5. Verificar el historial

---

## Parte 4: Modificaciones y Segundo Commit

1. Modificar `index.html` agregando una sección de navegación:

```html
<nav>
    <a href="index.html">Inicio</a>
    <a href="acerca.html">Acerca de</a>
    <a href="contacto.html">Contacto</a>
</nav>
```

2. Verificar las diferencias con el comando:
```
git diff
```

3. Agregar los cambios y realizar un nuevo commit

---

## Parte 5: Trabajo con Ramas

1. Crear una rama llamada `estilos`

2. Cambiar a la nueva rama

3. Crear un archivo `styles.css`:

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
}

h1 {
    color: #333;
}

nav {
    margin-bottom: 20px;
}

nav a {
    margin-right: 15px;
    text-decoration: none;
    color: #0066cc;
}
```

4. Modificar `index.html` para incluir el archivo CSS agregando en el `<head>`:

```html
<link rel="stylesheet" href="styles.css">
```

5. Agregar ambos archivos y hacer commit

6. Regresar a la rama principal

7. Fusionar la rama `estilos`

8. Eliminar la rama `estilos`

---

## Parte 6: Conexión con GitHub

1. Crear un repositorio en GitHub llamado `proyecto-web`

2. No inicializar con README

3. Copiar la URL del repositorio

4. En la terminal, vincular el repositorio local con el remoto

5. Subir el código al repositorio remoto

6. Verificar en GitHub que los archivos se subieron correctamente

---

## Parte 7: Simulación de Colaboración

1. Desde GitHub, editar directamente el archivo `index.html` agregando un párrafo adicional

2. Guardar los cambios (commit desde GitHub)

3. En la terminal local, intentar hacer un cambio y subirlo

4. Resolver el conflicto descargando primero los cambios remotos

5. Subir los cambios locales

---

## Entregables

Al finalizar el ejercicio, el estudiante debe tener:

- Un repositorio local con al menos 4 commits
- El repositorio sincronizado con GitHub
- Experiencia en creación y fusión de ramas
- Comprensión del flujo de sincronización

---

## Criterios de Evaluación

- Correcta inicialización del repositorio
- Mensajes de commit claros y descriptivos
- Uso apropiado de ramas
- Sincronización exitosa con GitHub
- Resolución de conflictos (si aplica)
