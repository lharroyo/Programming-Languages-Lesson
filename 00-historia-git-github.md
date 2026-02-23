# Historia y Evolución de Git y GitHub

**Material de apoyo para clase**

---

## Parte 1: Origen de Git

### El Contexto (2002-2005)

Antes de Git, el desarrollo del kernel de Linux utilizaba un sistema llamado **BitKeeper**, un software propietario de control de versiones. Linus Torvalds, creador de Linux, lo adoptó en 2002 a pesar de las críticas de la comunidad open source por usar software cerrado.

En abril de 2005, la relación entre la comunidad Linux y BitMover (empresa detrás de BitKeeper) se rompió debido a una disputa de licencias. Andrew Tridgell, creador de Samba, intentó hacer ingeniería inversa del protocolo de BitKeeper, lo que provocó que Larry McVoy (fundador de BitMover) revocara la licencia gratuita para el desarrollo de Linux.

### El Nacimiento de Git

**Fecha de creación:** 3 de abril de 2005

Linus Torvalds decidió crear su propio sistema de control de versiones. Lo que ocurrió después es legendario en la historia del software:

- **3 de abril de 2005:** Linus comienza el desarrollo
- **6 de abril de 2005:** Anuncia el proyecto públicamente
- **7 de abril de 2005:** Primer commit oficial de Git
- **18 de abril de 2005:** Primera fusión de múltiples ramas
- **29 de abril de 2005:** Git ya podía procesar 6.7 parches por segundo
- **16 de junio de 2005:** Git gestiona el lanzamiento del kernel 2.6.12
- **26 de julio de 2005:** Linus entrega el mantenimiento a Junio Hamano
- **21 de diciembre de 2005:** Lanzamiento de Git 1.0

En aproximadamente 10 días, Linus desarrolló una versión funcional de Git. El sistema fue creado con estos objetivos:

1. Velocidad extrema
2. Diseño simple
3. Soporte para desarrollo no lineal (miles de ramas paralelas)
4. Completamente distribuido
5. Capaz de manejar proyectos grandes eficientemente

### ¿Por qué se llama "Git"?

Linus Torvalds explicó que eligió el nombre por varias razones:

- Es una combinación de tres letras pronunciable y no usada por ningún comando UNIX
- En inglés británico, "git" es un insulto coloquial que significa "persona tonta o desagradable"
- Torvalds bromeó: "Soy un bastardo egoísta y nombro todos mis proyectos en honor a mí mismo"

La documentación oficial lo describe como "the stupid content tracker" (el rastreador de contenido estúpido).

### Los Sistemas Anteriores a Git

Para entender la importancia de Git, hay que conocer sus predecesores:

**CVS (Concurrent Versions System) - 1980s:**
- Sistema centralizado
- Rastreaba cambios archivo por archivo
- Requería conexión al servidor central

**SVN (Subversion) - 2000:**
- Mejora sobre CVS
- Seguía siendo centralizado
- Problemas con el manejo de ramas

**BitKeeper - 2000:**
- Primer sistema distribuido popular
- Propietario y de pago
- Influyó directamente en el diseño de Git

---

## Parte 2: De Git a GitHub

### Antes de GitHub

Git es solo la herramienta de línea de comandos. Durante los primeros años, los desarrolladores subían código a servidores propios o usaban servicios básicos de hosting.

### Fundación de GitHub

**Fecha:** Febrero de 2008

GitHub fue fundado por:
- Tom Preston-Werner
- Chris Wanstrath
- PJ Hyett
- Scott Chacon

Scott Chacon, uno de los cofundadores, también es autor de "Pro Git", el libro de referencia sobre Git disponible gratuitamente en git-scm.com.

### Crecimiento de GitHub

- **2008:** Lanzamiento público
- **2012:** 1 millón de usuarios
- **2018:** Microsoft adquiere GitHub por 7.5 mil millones de dólares
- **2025:** Más de 150 millones de usuarios y más de 420 millones de repositorios

### Junio Hamano: El Guardián de Git

Desde julio de 2005, Junio Hamano ha sido el mantenedor principal de Git. Mientras Linus regresó al desarrollo de Linux, Hamano ha liderado Git por casi 20 años, supervisando todas las versiones desde la 1.0.

---

## Parte 3: Versiones Importantes de Git

### Git 1.0 (Diciembre 2005)
Primera versión estable. Incluía las operaciones básicas que conocemos hoy.

### Git 2.0 (Mayo 2014)
Primera versión con cambios incompatibles hacia atrás. Cambió comportamientos predeterminados para hacerlos más intuitivos.

### Hitos Recientes

**2017:** Después del ataque SHAttered, Git fue modificado para usar una variante de SHA-1 resistente.

**2020:** Se inició un plan para transicionar a una nueva función hash más segura.

**2024-2025:** Nuevas herramientas para repositorios masivos:
- Geometric repacking
- On-disk reverse indexes
- Reachability bitmaps para MIDX
- Soporte incremental de MIDX

---

## Parte 4: Lo Más Reciente en GitHub (2025-2026)

### GitHub Copilot y la Era de los Agentes

GitHub Universe 2025 introdujo cambios significativos:

**Agent Mode:**
- Copilot puede iterar sobre su propio código
- Reconoce y corrige errores automáticamente
- Sugiere comandos de terminal
- Capacidades de auto-reparación

**Next Edit Suggestions:**
- Identifica automáticamente la siguiente edición necesaria
- Con solo presionar Tab, implementa sugerencias en todo el archivo

**Prompt Files:**
- Archivos markdown reutilizables con instrucciones
- Se pueden compartir entre equipos

### Copilot Spaces

Permite crear espacios de trabajo con contexto curado del proyecto:
- Espacios públicos con enlaces compartibles
- Compartir individualmente
- Agregar archivos directamente desde el visor de código

### Modelos de IA Disponibles

GitHub Copilot ahora ofrece múltiples modelos:
- OpenAI GPT-5.1-Codex-Max (preview)
- Google Gemini 2.0 Flash
- OpenAI o3-mini

### GitHub Copilot Workspace

Capacidades agénticas para:
- Ir de la idea al código funcional en minutos
- Generar planes de implementación
- Encontrar y corregir errores automáticamente
- Sistema de sub-agentes para colaboración

### Seguridad Avanzada

**CodeQL:**
- Análisis semántico del código
- Genera correcciones automáticas para el 90% de los tipos de alertas
- Soporta JavaScript, TypeScript, Java y Python

**Secret Scanning:**
- Detecta secretos expuestos en repositorios públicos y privados
- Capacidades de IA para detectar contraseñas

**Dependabot:**
- Alertas automáticas de vulnerabilidades
- Pull requests automáticos para actualizar dependencias

### GitHub Actions

Sistema de CI/CD integrado:
- Automatización de workflows
- Miles de actions disponibles de la comunidad
- Integración con testing, deployment y más

---

## Parte 5: Estadísticas Relevantes

### Adopción de Git

Según encuestas de Stack Overflow:
- 2015: 69.3% de desarrolladores usaban Git
- 2017: 69% de adopción
- 2018: 88.4% de adopción
- 2021: 94% de adopción

Git es tan dominante que Stack Overflow dejó de preguntar sobre control de versiones en 2019.

### Actividad en GitHub (2025)

- 986 millones de code pushes en 2025
- La tendencia es hacia commits más pequeños y frecuentes
- Feature flags y pipelines automatizados son ahora esenciales

---

## Parte 6: Conceptos Clave para Explicar en Clase

### ¿Por qué Git es Distribuido?

A diferencia de sistemas centralizados:
- Cada desarrollador tiene una copia completa del repositorio
- Incluye todo el historial de cambios
- Permite trabajar sin conexión a internet
- Proporciona redundancia natural

### Las Tres Áreas de Git

1. **Working Directory:** Los archivos tal como están en el disco
2. **Staging Area (Index):** Cambios preparados para el próximo commit
3. **Repository (.git):** El historial completo de commits

### Los Cuatro Tipos de Objetos en Git

1. **Blob:** Contenido de un archivo
2. **Tree:** Estructura de directorios
3. **Commit:** Instantánea del proyecto con metadatos
4. **Tag:** Referencia nombrada a un commit específico

---

## Parte 7: Cronología Resumida

| Año | Evento |
|-----|--------|
| 1991 | Linus Torvalds crea Linux |
| 2002 | Linux adopta BitKeeper |
| 2005 | Disputa de licencias, Linus crea Git |
| 2005 | Junio Hamano asume mantenimiento |
| 2005 | Git 1.0 lanzado |
| 2008 | GitHub es fundado |
| 2014 | Git 2.0 lanzado |
| 2018 | Microsoft adquiere GitHub |
| 2021 | GitHub Copilot lanzado |
| 2025 | Git cumple 20 años |
| 2025 | GitHub supera 150 millones de usuarios |

---

## Referencias

- Documentación oficial: https://git-scm.com/doc
- Pro Git Book: https://git-scm.com/book
- GitHub Docs: https://docs.github.com
- GitHub Roadmap: https://github.com/github/roadmap
