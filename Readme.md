# AIS Agentes Inteligentes Simulados

El proyecto de creación de **AIS**  **(agentes inteligentes simulados)**, es un proyecto de final de curso donde los estudiantes desarrollan pequeños sistemas autónomos que puedan tomar decisiones basadas en información estructurada (datos) y comportamientos predefinidos. 

Este proyecto simula una pequeña ciudad en la que se integran diferentes tipos de agentes (vehículos, personas, supermercados, clientes, ayuntamientos, colegios entre otros). 

Los equipos se conformaran por parejas para implementar funcionalidades específicas los agentes dentro de esta ciudad, y cada funcionalidad estará relacionada con la interacción entre dichos agentes. 

El proyecto será completamente interactivo a través de la **línea de comandos**. El sistema permitirá ingresar comandos para gestionar agentes, realizar interacciones entre los agentes y  permite su  gestión.

Cada pareja de estudiantes será responsable de implementar mínimo dos agentes y su interacción entre ellos.

## 1. Objetivo del Proyecto

Desarrollar un sistema de simulación de una ciudad en Python, donde diferentes tipos de agentes (vehículos, personas, supermercados, colegios, ayuntamientos, etc.) interactúan entre sí a través de un conjunto definido de comandos. El sistema debe ser completamente interactivo y operar a través de la línea de comandos.

## 2. Estructura del Sistema

Cada grupo debe crear un sistema que incluya:

- **Clases**: Cada agente debe tener su propia clase que encapsule su comportamiento y estado.
- **Gestión de Agentes**: Implementar un sistema que permita agregar, eliminar y gestionar agentes de manera eficiente.
- **Comandos**: Definir un conjunto de comandos que permitan la interacción con el sistema desde la línea de comandos.

## 3. Requisitos de Diseño

- **Principios de responsabilidad única**: Asegurarse de que las clases sigan los principios de Responsabilidad Única (`SRP`), para que cada clase se encargue de una única responsabilidad.
- **Modularidad**: Estructurar el código de manera que sea fácil de entender y mantener, dividiendo la lógica en módulos y funciones claramente definidas.
- **Interactividad**: El sistema debe permitir la interacción mediante una interfaz de línea de comandos, donde los usuarios puedan introducir comandos para gestionar los agentes.
- **Persistencia:** Los datos del simulador deberán ser almacenados en un fichero `JSON` que servirá también para recuperar el estado del simulador en el momento del almacenaje.

## 4. Especificaciones Técnicas

Cada grupo debe utilizar las siguientes especificaciones en su desarrollo:

- **Clases**:
  - Implementar clases para cada tipo de agente, como `Vehicle`, `Supermarket`, `Student`, `TownHall`, etc., según corresponda a la definición funcional de su grupo.

- **Gestión de Datos**:
  - Utilizar estructuras de datos como `listas`, `tuplas`, `diccionarios` y `conjuntos` para gestionar agentes, servicios y solicitudes.
  - Aplicar comprensión de listas para filtrar y transformar datos de manera eficiente.
  - Usar funciones de orden superior como `map`, `filter` y expresiones `lambda` para manipular datos y realizar operaciones específicas.

- **Búsqueda**:
  - Implementar búsquedas utilizando expresiones regulares para encontrar patrones en nombres de agentes, servicios o comandos.
  - Usar `closures` para encapsular lógica de búsqueda personalizada, si aplica.

- **Ordenación y Filtrado**:
  - Utilizar métodos integrados de Python como `sorted` con claves personalizadas para ordenar listas de agentes o servicios.
  - Aplicar filtros dinámicos con expresiones `lambda` y funciones como `filter` para mostrar datos según criterios específicos.

- **Validación y Procesamiento**:
  - Implementar validaciones dinámicas utilizando expresiones regulares para comandos y entradas del usuario.
  - Usar `closures` para encapsular lógica de validación y reutilizarla en diferentes partes del programa.

Estas especificaciones permiten aprovechar al máximo las características de Python, simplificando el código y mejorando su legibilidad y eficiencia.

## 5. Comandos Generales

Cada grupo tiene definido un conjunto de comandos que permitan gestionar sus agentes. 

Ejemplos de comandos que se encontrarán especificados en cada grupo, en general son de este tipo:

- `agent_type <add_agent_type> <agent_name>`: Añadir un nuevo agente al sistema.
- `agent_type <remove_agent_type> <agent_name>`: Eliminar un agente del sistema.
- `agent_type show_all`: Muestra todos los agentes existentes en el sistema

## 6. Desarrollo en Parejas

Cada grupo se conformará en parejas para implementar las funcionalidades específicas de sus agentes. 

Los roles serán como se describen a continuación, intercambiandose durante el desarrollo del mismo:

- **Desarrollador de Lógica**: Responsable de la implementación de la lógica del agente y sus métodos.

- **Integrador de Comandos**: Encargado de conectar la lógica del agente con los comandos de línea de comandos, asegurando que los usuarios puedan interactuar con el sistema de manera efectiva.

- **Documentador:** Encargado de cuidar los detalles, nombres de documentos, presentación a entregar.

- **Tester:** Encargado de la implementación de los casos de pruebas

- **Grupos:**

  [Clientes y Supermercados](1_Clientes_supermercados.md)

  [Clientes y Colegios](2_Clientes_Colegios.md)

  [Clientes y Vehículos](3_Clientes_Vehículos.md)

  [Clientes y Restaurantes](4_Clientes_Restaurantes.md)

  [Clientes y Teatros](5_Clientes_Teatros.md)

  [Clientes y Estadios de Fútbol](6_Clientes_Estadios_Futbol.md)

  [Cliente y Hospitales](8_Clientes_Hospitales.md)

  [Clientes y Parques de atracciones](9_Clientes_ParquesAtraciones.md)

## 7. Fecha de entrega

La fecha de entrega es el día <19 de mayo de 2025>

- **Planificación y diseño** 
- **Implementación**
- **Pruebas y ajuste**

## 8. Ejemplo de Código Base

El siguiente código base proporcionará un punto de partida para que cada grupo estructure su propio sistema. Este ejemplo define una estructura básica y permite la gestión de agentes 

[Clientes y Ayuntamiento](0_Clientes_Ayuntamiento.md)

[Jupyter Notebook - Town hall](SIC_Capstone_project.ipynb)

## 9. Documentos de entrega

[Especificaciones de la entrega](Presentacion_PowerPoint.md)

> # **Nota final**

Este trabajo será enviado a Samsung como **SIC Capstone project**.

