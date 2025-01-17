### Clases y sus Atributos/Métodos

1. **Agent**
   - Atributos:
     - **name**: Nombre del agente.
   - Métodos:
     - `__init__`: Inicializa el agente con un nombre.
     - __str__: Devuelve el nombre del agente.
     - **describe**: Devuelve la representación en cadena del agente.
2. **Client (hereda de Agent)**
   - Atributos:
     - town_hall_stack: **Pila** que almacena los ayuntamientos visitados.
   - Métodos:
     - `__init__`: Inicializa el cliente con un nombre y una pila de ayuntamientos.
     - **enter_town_hall**: Marca la entrada en un ayuntamiento.
     - **exit_town_hall**: Marca la salida del último ayuntamiento visitado.
     - **current_town_hall**: Devuelve el ayuntamiento actual.
3. **TownHall (hereda de Agent)**
   - Atributos:
     - **services**: Lista de servicios ofrecidos.
     - **request_services**: Cola de solicitudes de servicios.
   - Métodos:
     - `__init__`: Inicializa el ayuntamiento con un nombre, lista de servicios y cola de solicitudes.
     - **add_service**: Añade un nuevo servicio.
     - **remove_service**: Elimina un servicio.
     - **show_services**: Muestra los servicios disponibles.
     - **show_services_queue**: Muestra la cola de servicios solicitados.
     - **add_request_service**: Añade una solicitud de servicio a la cola.
     - **process_request_service**: Atiende la primera solicitud en la cola.
4. **CitySimulation**
   - Atributos**:**
     - **TIME_THRESHOLD**: Umbral de tiempo para atender solicitudes.
   - Métodos:
     - `__filter_agents`: Filtra agentes según los tipos proporcionados.
     - `__get_agent_by_name`: Devuelve el agente con el nombre y tipo específico.
     - **add_agent**: Añade un nuevo agente al sistema.
     - **remove_agent**: Elimina un agente del sistema.
     - **list_agents**: Muestra todos los agentes o filtra por tipo.
     - **help_town_hall**: Muestra comandos disponibles para ayuntamientos.
     - **help_client**: Muestra comandos disponibles para clientes.
     - **help**: Muestra información general de ayuda.
     - **check_ready_services**: Verifica si hay servicios listos para ser atendidos.
     - **is_time_to_serve**: Verifica si es el momento de atender el siguiente servicio en la cola.
     - **command_loop**: Bucle principal para gestionar comandos del usuario.
     - **process_command**: Procesa los comandos ingresados por el usuario.
5. **Stack**
   - Atributos:
     - **stack**: Lista que representa la pila.
   - Métodos:
     - `__init__`: Inicializa la pila.
     - **is_empty**: Verifica si la pila está vacía.
     - **push**: Añade un elemento a la pila.
     - **pop**: Elimina y devuelve el último elemento de la pila.
     - **peek**: Devuelve el último elemento de la pila sin eliminarlo.
6. **Queue**
   - Atributos:
     - **queue**: Lista que representa la cola.
   - Métodos:
     - `__init__`: Inicializa la cola.
     - **is_empty**: Verifica si la cola está vacía.
     - **peek**: Devuelve el primer elemento de la cola sin eliminarlo.
     - **enqueue**: Añade un elemento a la cola.
     - **dequeue**: Elimina y devuelve el primer elemento de la cola.
     - **size**: Devuelve el tamaño de la cola.

### Relación entre Clases

- ***Client*** y ***TownHall*** heredan de **Agent**
- ***Client*** utiliza ***Stack*** para gestionar los ayuntamientos visitados.
- ***TownHall*** utiliza ***Queue*** para gestionar las solicitudes de servicios.
- ***CitySimulation*** gestiona la interacción entre **Client** y **TownHall**, y proporciona una interfaz de comandos para el usuario.

### No perder de vista:

- El uso de herencia para ***Client*** y ***TownHall*** desde **Agent**
- Implementación de estructuras de datos ***Stack*** y ***Queue***
- Sistema de comandos para interactuar con la simulación.
- Gestión de tiempo para procesar solicitudes de servicios en ***TownHall***



## Diagrama de clases

```bash
+-----------------+
|     Agent       |
+-----------------+
| - name: str     |
+-----------------+
| + __init__(name)|
| + __str__()     |
| + describe()    |<------------------------------------+
+-----------------+                                     |
          ^                                             |
          |                                             |
          |                                             |
+----------------------------------+            +-------------------------------------+
|     Client (Agent)               |            |    TownHall (Agent)                 |
+----------------------------------+            +-------------------------------------+
| - town_hall_stack: Stack         |            | - services: list                    |
+----------------------------------+            | - request_services: Queue           |
| + __init__(name)                 |            +-------------------------------------+
| + enter_town_hall(town_hall_name)|            | + __init__(name)                    |
| + exit_town_hall()               |            | + add_service(service_name)         |
| + current_town_hall()            |            | + remove_service(service_name)      |
+----------------------------------+            | + show_services()                   | 
                   ^        ^                   | + show_services_queue()             |
                   |        |                   | + add_request_service(client_name,  | 
                   |        --------+---------->|                      service_name)  |   
                   |                |           | + process_request_service()         |
                   |                |           +-------------------------------------+
                   |                |                   ^
           +-----------------+      |                   |
           |     Stack       |      |           +-----------------+
           +-----------------+      |           |     Queue       |
           | - stack: list   |      |           +-----------------+
           +-----------------+      |           | - queue: list   |
           | + __init__()    |      |           +-----------------+
           | + is_empty()    |      |           | + __init__()    |
           | + push(item)    |      |           | + is_empty()    |
           | + pop()         |      |           | + peek()        |
           | + peek()        |      |           | + enqueue(item) |
           +-----------------+      |           | + dequeue()     | 
                                    |           | + size()        |                   
                                    |           +-----------------+ 
                                    |
                                    |
                          +-----------------------------------------------+
                          | CitySimulation                                |
                          +-----------------------------------------------+
                          | - TIME_THRESHOLD: int                         |
                          +-----------------------------------------------+
                          | + __init__()                                  |
                          | + __filter_agents(*agents_types)              |
                          | + __get_agent_by_name(agent_name, agent_type) |
                          | + add_agent(agent_type, agent_name)           |
                          | + remove_agent(agent_name)                    |
                          | + list_agents(agent_type=None)                |
                          | + help_town_hall()                            |
                          | + help_client()                               |
                          | + help()                                      |
                          | + check_ready_services()                      |
                          | + is_time_to_serve(town_hall)                 |
                          | + command_loop()                              |
                          | + process_command(command)                    |
                          +-----------------------------------------------+
         
```

