# Documentos de Entrega

### 1 - Presentación de PowerPoint

`SIC_Capstone_<nombre_proyecto>.ppt`

### 2 - Cuaderno jupyter notebook.ipynb 

`SIC_Capstone_<nombre_proyecto>.ipynb`

### 3 - Fichero de casos de pruebas

 `test_city_simulation.py`

## Presentación PowerPoint

Descripción del contenido de la presentación de entrega.

------

### Diapositiva 1: Introducción

- **Título del Proyecto**: Simulador de Ciudad <especificación del grupo y agentes de interación>
- **Nombre del Equipo**: [Nombres de los integrantes]
- **Fecha**: [Fecha de entrega]

------

### Diapositiva 2: Descripción del Proyecto

- **Objetivo**: Desarrollar un simulador interactivo de una ciudad que permita gestionar <especificación del grupo>, mediante comandos.
- Funcionalidad:
  - <descripción de la funcionalidad el grupo>

### Diapositiva 3: Clases Implementadas

- **Clase [Agent]() (Base)**
  - Atributos:
    - **name** (nombre del agente).
  - Métodos:
    - **describe()**: Devuelve una descripción del agente.
- **Clase `<TipoEspecífico>` (Ejemplo: [Client], `Supermarket`, `School`, etc.)**
  - Atributos:
    - Atributos específicos según el tipo de agente (por ejemplo, [services](), [queue](), [stack](), etc.).
  - Métodos:
    - Métodos específicos para gestionar las interacciones entre agentes (por ejemplo, add_service(), `request_service()`, etc.).

Describir la herencia entre ellas (Debe existir)

------

### Diapositiva 4: Gestión de Datos

- Estructuras de datos utilizadas:
  - **Diccionario [agents]()**: Almacena todos los agentes del sistema, organizados por nombre.
  - **Clase [Stack]()**: Utilizada para rastrear ubicaciones o estados temporales (por ejemplo, ubicación actual de un cliente).
  - **Clase [Queue]()**: Utilizada para gestionar colas de solicitudes o procesos pendientes (por ejemplo, servicios en espera).
  - **Otras estructuras**: `Tuplas`, `Listas`, `Conjuntos`, etc, etc.

------

### Diapositiva 5: Búsquedas

- Búsquedas implementadas:
  - Por nombre:
    - Método [get_agent_by_name(agent_name, agent_type)]() para buscar agentes específicos por nombre y tipo.
  - Por tipo:
    - Método [filter_agents(*agent_types)]() para filtrar agentes según su tipo (por ejemplo, [Client](), `Supermarket`, `School`, etc.).

------

### Diapositiva 6: Ordenación y Filtrado

- Filtrado:
  - Uso de comprensión de diccionarios en [filter_agents]() para filtrar agentes por tipo.
- Ordenación:
  - Uso de métodos como `sorted` con claves personalizadas para ordenar listas de agentes o servicios según criterios específicos.

------

### Diapositiva 7: Validación y Procesamiento

- **Validaciones**:
  - Validación de comandos con el método [validate_command]().
  - Validación de relaciones entre agentes (por ejemplo, si un cliente está en un supermercado o colegio) con métodos como [validate_client_location()]().
  - Validación de disponibilidad de servicios con `validate_service_in_<AgentType>()`.
- **Procesamiento**:
  - Procesamiento de solicitudes en cola con métodos como [process_request_service()]() en agentes específicos.
  - Verificación de condiciones para ejecutar acciones (por ejemplo, tiempo de espera o disponibilidad de recursos).

------

### Diapositiva 8 a n: Descripción del Funcionamiento de Cada Comando

1. Comando (son aproximadamente 20 comandos por equipo.
   
   Cada diapositiva debe tener como máximo 4 comandos con la siguiente estructura:
   
   - **Descripción**: 
   - **Ejemplo de uso**: 
   - **Salida esperada:**

------

### Diapositiva n+1: Conclusiones

- **Aprendizaje**: Implementación de un sistema de comandos, gestión de clases y objetos en Python.
- **Futuras Mejoras**: Incorporación de más funcionalidades, optimización de la interfaz de usuario.