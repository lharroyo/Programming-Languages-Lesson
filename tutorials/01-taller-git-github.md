# Taller Práctico: Control de Versiones con Git y GitHub

**Duración estimada:** 2 horas  
**Nivel:** Principiante  
**Prerrequisitos:** Conocimientos básicos de línea de comandos

---

## Introducción

El control de versiones es una práctica fundamental en el desarrollo de software moderno. Git, creado por Linus Torvalds en 2005, se ha convertido en el estándar de la industria para gestionar código fuente. Este taller proporciona una guía práctica para comenzar a trabajar con Git y GitHub.

---

## Módulo 1: Fundamentos Teóricos

### 1.1 ¿Qué es un Sistema de Control de Versiones?

Un sistema de control de versiones (VCS) es una herramienta que registra los cambios realizados en archivos a lo largo del tiempo. Permite:

- Recuperar versiones anteriores de un proyecto
- Comparar cambios entre versiones
- Identificar quién modificó qué y cuándo
- Trabajar en equipo sin sobrescribir el trabajo de otros

### 1.2 Git: Sistema Distribuido

A diferencia de sistemas centralizados, Git es distribuido. Cada desarrollador tiene una copia completa del repositorio, incluyendo todo el historial. Esto permite trabajar sin conexión y proporciona redundancia natural.

### 1.3 GitHub como Plataforma de Colaboración

GitHub es un servicio de alojamiento para repositorios Git que añade funcionalidades de colaboración: revisión de código, gestión de issues, integración continua, entre otras.

---

## Módulo 2: Instalación y Configuración

### 2.1 Instalación de Git

**En Windows:**

1. Acceder a https://git-scm.com/download/win
2. Descargar el instalador correspondiente a la arquitectura del sistema
3. Ejecutar el instalador manteniendo las opciones predeterminadas

**Verificación de la instalación:**

```
git --version
```

### 2.2 Configuración Inicial

Antes de comenzar a trabajar, es necesario configurar la identidad del usuario. Esta información se incluirá en cada commit realizado.

```
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
```

Para verificar la configuración actual:

```
git config --list
```

Configuración adicional recomendada:

```
git config --global init.defaultBranch main
git config --global core.autocrlf true
```

---

## Módulo 3: Operaciones Básicas

### 3.1 Crear un Repositorio Local

Crear y acceder a la carpeta del proyecto:

```
mkdir mi-proyecto
cd mi-proyecto
```

Inicializar el repositorio:

```
git init
```

Este comando crea un directorio oculto `.git` que contiene toda la información del repositorio.

### 3.2 El Ciclo de Trabajo en Git

Git maneja tres áreas principales:

1. **Working Directory:** Archivos en su estado actual
2. **Staging Area:** Cambios preparados para el próximo commit
3. **Repository:** Historial de commits almacenado

### 3.3 Comandos del Ciclo Básico

**Verificar el estado actual:**

```
git status
```

**Agregar archivos al área de preparación:**

```
git add nombre_archivo.txt
```

Para agregar todos los archivos modificados:

```
git add .
```

**Confirmar los cambios (commit):**

```
git commit -m "Descripción breve del cambio realizado"
```

**Consultar el historial:**

```
git log
```

Formato condensado:

```
git log --oneline
```

### 3.4 Ejercicio Práctico 1

1. Crear un archivo README.md con el contenido:
   ```
   echo "# Proyecto de Ejemplo" > README.md
   ```

2. Verificar el estado del repositorio
3. Agregar el archivo al staging
4. Realizar el primer commit
5. Verificar el historial

---

## Módulo 4: Trabajo con Repositorios Remotos

### 4.1 Crear un Repositorio en GitHub

1. Iniciar sesión en https://github.com
2. Seleccionar "New repository" desde el menú
3. Asignar nombre al repositorio
4. Seleccionar visibilidad (público o privado)
5. No seleccionar inicialización con README si ya existe localmente
6. Confirmar la creación

### 4.2 Vincular Repositorio Local con Remoto

Agregar la referencia al repositorio remoto:

```
git remote add origin https://github.com/usuario/nombre-repositorio.git
```

Verificar la configuración:

```
git remote -v
```

### 4.3 Sincronización

**Subir cambios al repositorio remoto:**

```
git push -u origin main
```

El parámetro `-u` establece la rama remota como predeterminada para futuros push.

**Descargar cambios del repositorio remoto:**

```
git pull origin main
```

**Clonar un repositorio existente:**

```
git clone https://github.com/usuario/repositorio.git
```

---

## Módulo 5: Gestión de Ramas

### 5.1 Concepto de Rama

Una rama es una línea independiente de desarrollo. Permite trabajar en funcionalidades o correcciones sin afectar la rama principal hasta que el trabajo esté completo.

### 5.2 Operaciones con Ramas

**Listar ramas existentes:**

```
git branch
```

**Crear una nueva rama:**

```
git branch nombre-rama
```

**Cambiar a otra rama:**

```
git checkout nombre-rama
```

**Crear y cambiar en un solo comando:**

```
git checkout -b nombre-rama
```

**Fusionar una rama con la actual:**

```
git merge nombre-rama
```

**Eliminar una rama:**

```
git branch -d nombre-rama
```

### 5.3 Ejercicio Práctico 2

1. Crear una rama llamada "desarrollo"
2. Cambiar a la nueva rama
3. Crear un archivo nuevo y hacer commit
4. Regresar a la rama main
5. Fusionar los cambios de "desarrollo"
6. Eliminar la rama "desarrollo"

---

## Módulo 6: Resolución de Problemas Frecuentes

### 6.1 Deshacer Cambios

**Descartar cambios en un archivo (antes de add):**

```
git checkout -- nombre_archivo.txt
```

**Quitar un archivo del staging (después de add):**

```
git reset HEAD nombre_archivo.txt
```

**Deshacer el último commit (manteniendo los cambios):**

```
git reset --soft HEAD~1
```

### 6.2 Errores Comunes y Soluciones

**"fatal: not a git repository"**

Se está ejecutando un comando Git fuera de un repositorio. Verificar la ubicación o ejecutar `git init`.

**"error: failed to push some refs"**

El repositorio remoto tiene cambios que no existen localmente. Ejecutar primero:

```
git pull origin main
```

**Conflictos de fusión**

Cuando Git no puede fusionar automáticamente, marca los archivos en conflicto. Es necesario:

1. Abrir los archivos marcados
2. Resolver manualmente las diferencias
3. Ejecutar `git add` sobre los archivos resueltos
4. Completar con `git commit`

---

## Módulo 7: Buenas Prácticas

### 7.1 Mensajes de Commit

Un buen mensaje de commit debe:

- Ser conciso pero descriptivo
- Usar tiempo presente o imperativo
- Explicar el "qué" y el "por qué", no el "cómo"

Ejemplos apropiados:
- "Corregir validación de formulario de registro"
- "Agregar endpoint para consulta de usuarios"
- "Actualizar dependencias de seguridad"

### 7.2 Flujo de Trabajo Recomendado

1. Actualizar la rama principal: `git pull origin main`
2. Crear rama para la nueva funcionalidad
3. Desarrollar y hacer commits frecuentes
4. Subir la rama al remoto
5. Crear Pull Request para revisión
6. Fusionar tras la aprobación
7. Eliminar la rama utilizada

---

## Referencia Rápida de Comandos

**Configuración**
- `git config --global user.name "nombre"` - Establecer nombre
- `git config --global user.email "email"` - Establecer correo
- `git config --list` - Ver configuración

**Repositorio**
- `git init` - Inicializar repositorio
- `git clone url` - Clonar repositorio remoto
- `git status` - Ver estado actual

**Cambios**
- `git add archivo` - Agregar al staging
- `git add .` - Agregar todos los cambios
- `git commit -m "mensaje"` - Confirmar cambios
- `git log` - Ver historial

**Ramas**
- `git branch` - Listar ramas
- `git branch nombre` - Crear rama
- `git checkout nombre` - Cambiar de rama
- `git checkout -b nombre` - Crear y cambiar
- `git merge nombre` - Fusionar rama

**Sincronización**
- `git remote add origin url` - Vincular remoto
- `git push origin rama` - Subir cambios
- `git pull origin rama` - Descargar cambios

---

## Recursos Complementarios

- Documentación oficial de Git: https://git-scm.com/doc
- Guías de GitHub: https://docs.github.com
- Práctica interactiva: https://learngitbranching.js.org

---

## Evaluación del Taller

Al finalizar, el estudiante debe ser capaz de:

1. Configurar Git en su equipo local
2. Crear y gestionar un repositorio
3. Realizar el ciclo completo: add, commit, push
4. Trabajar con ramas básicas
5. Resolver problemas comunes de sincronización
