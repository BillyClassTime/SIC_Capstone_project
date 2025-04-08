# Documentación del Proyecto

## Clases y sus Atributos/Métodos

### 1. Agent
- **Atributos**:
  - `name`: Nombre del agente.
- **Métodos**:
  - `__init__(name)`: Inicializa el agente con un nombre.
  - `__str__()`: Devuelve el nombre del agente.
  - `describe()`: Devuelve la representación en cadena del agente.

### 2. Client (hereda de `Agent`)
- **Atributos**:
  - `town_hall_stack`: **Pila** que almacena los ayuntamientos visitados.
- **Métodos**:
  - `__init__(name)`: Inicializa el cliente con un nombre y una pila de ayuntamientos.
  - `enter_town_hall(town_hall_name)`: Marca la entrada en un ayuntamiento.
  - `exit_town_hall()`: Marca la salida del último ayuntamiento visitado.
  - `current_town_hall()`: Devuelve el ayuntamiento actual.
  - `help()`: Muestra los comandos disponibles para los clientes.

### 3. TownHall (hereda de `Agent`)
- **Atributos**:
  - `services`: Lista de servicios ofrecidos.
  - `request_services`: Cola de solicitudes de servicios.
- **Métodos**:
  - `__init__(name)`: Inicializa el ayuntamiento con un nombre.
  - `add_service(service_name)`: Añade un nuevo servicio.
  - `remove_service(service_name)`: Elimina un servicio.
  - `show_services()`: Muestra los servicios disponibles.
  - `show_services_queue()`: Muestra la cola de servicios solicitados.
  - `add_request_service(client_name, service_name)`: Añade una solicitud de servicio a la cola.
  - `process_request_service()`: Atiende la primera solicitud en la cola.
  - `help()`: Muestra los comandos disponibles para los ayuntamientos.

### 4. AgentManager
- **Atributos**:
  - `agents`: Diccionario que almacena todos los agentes (clientes y ayuntamientos).
  - `TIME_THRESHOLD`: Umbral de tiempo (en segundos) para procesar solicitudes.
- **Métodos**:
  - `__init__()`: Inicializa el gestor de agentes.
  - `filter_agents(*agents_types)`: Filtra agentes según los tipos proporcionados.
  - `get_agent_by_name(agent_name, agent_type)`: Devuelve el agente con el nombre y tipo específico.
  - `add_agent(agent_type, agent_name)`: Añade un nuevo agente al sistema.
  - `remove_agent(agent_name)`: Elimina un agente del sistema.
  - `list_agents(agent_type=None)`: Muestra todos los agentes o filtra por tipo.
  - `check_ready_services()`: Verifica si hay servicios listos para ser atendidos.
  - `is_time_to_serve(town_hall)`: Verifica si es el momento de atender el siguiente servicio en la cola.
  - `validate_client_location(client, town_hall_name)`: Valida si un cliente está en un ayuntamiento específico.
  - `load_agents_from_file(file_path)`: Carga agentes desde un archivo JSON.

### 5. CitySimulation
- **Atributos**:
  - `agent_manager`: Instancia de `AgentManager` para gestionar los agentes.
  - `ERROR_MESSAGES`: Diccionario de mensajes de error centralizados.
- **Métodos**:
  - `__init__()`: Inicializa la simulación de la ciudad.
  - `help_town_hall()`: Muestra los comandos disponibles para ayuntamientos.
  - `help_client()`: Muestra los comandos disponibles para clientes.
  - `help()`: Muestra información general de ayuda.
  - `validate_command(parts, expected_length, error_key, expected_format)`: Valida el formato de un comando.
  - `validate_service_in_town_hall(town_hall, service_name)`: Valida si un servicio está disponible en un ayuntamiento.
  - `get_agent_or_error(agent_name, agent_type, error_key)`: Obtiene un agente o muestra un error si no existe.
  - `command_loop()`: Bucle principal para gestionar comandos del usuario.
  - `process_command(command)`: Procesa los comandos ingresados por el usuario.

### 6. Stack
- **Atributos**:
  - `stack`: Lista que representa la pila.
- **Métodos**:
  - `__init__()`: Inicializa la pila.
  - `is_empty()`: Verifica si la pila está vacía.
  - `push(item)`: Añade un elemento a la pila.
  - `pop()`: Elimina y devuelve el último elemento de la pila.
  - `peek()`: Devuelve el último elemento de la pila sin eliminarlo.

### 7. Queue
- **Atributos**:
  - `queue`: Lista que representa la cola.
- **Métodos**:
  - `__init__()`: Inicializa la cola.
  - `is_empty()`: Verifica si la cola está vacía.
  - `peek()`: Devuelve el primer elemento de la cola sin eliminarlo.
  - `enqueue(item)`: Añade un elemento a la cola.
  - `dequeue()`: Elimina y devuelve el primer elemento de la cola.
  - `size()`: Devuelve el tamaño de la cola.

---

## Relación entre Clases

- **`Client`** y **`TownHall`** heredan de **`Agent`**.
- **`AgentManager`** gestiona la creación, eliminación y filtrado de agentes.
- **`Client`** utiliza **`Stack`** para gestionar los ayuntamientos visitados.
- **`TownHall`** utiliza **`Queue`** para gestionar las solicitudes de servicios.
- **`CitySimulation`** utiliza **`AgentManager`** para coordinar la interacción entre **`Client`** y **`TownHall`**, y proporciona una interfaz de comandos para el usuario.

---

## Ejemplos de Uso

### Crear un Cliente y Registrar Ayuntamientos Visitados
```python
# Crear un cliente
client = Client("John Doe")

# Registrar ayuntamientos visitados
client.enter_town_hall("TownHall A")
client.enter_town_hall("TownHall B")

# Ver el ayuntamiento actual
print(client.current_town_hall())  # Output: TownHall B

# Salir del último ayuntamiento
client.exit_town_hall()
print(client.current_town_hall())  # Output: TownHall A
```
### Crear un Ayuntamiento y Gestionar Servicios
```python
# Crear un ayuntamiento
town_hall = TownHall("Central TownHall")

# Añadir un nuevo servicio
town_hall.add_service("Service A")

# Mostrar servicios disponibles
town_hall.show_services()  # Output: ['Service A']

# Añadir una solicitud de servicio
town_hall.add_request_service("John Doe", "Service A")

# Procesar la primera solicitud
town_hall.process_request_service()
```
### Simulación de Ciudad
```python
# Crear una simulación
simulation = CitySimulation()

# Añadir agentes
simulation.agent_manager.add_agent(Client, "John Doe")
simulation.agent_manager.add_agent(TownHall, "Central TownHall")

# Listar agentes
simulation.agent_manager.list_agents()  # Muestra todos los agentes

# Procesar comandos
simulation.process_command("town_hall add_service Central TownHall Service A")
simulation.process_command("client request_service John Doe Central TownHall Service A")
```
## Diagrama de Clases
```bash
+-----------------+
|     Agent       |
+-----------------+
| - name: str     |
+-----------------+
| + __init__(name)|
| + __str__()     |
| + describe()    |
+-----------------+
          ^
          |
+-------------------------+
|       Client (Agent)    |
+-------------------------+
| - town_hall_stack: Stack|
+-------------------------+
| + __init__(name)        |
| + enter_town_hall()     |
| + exit_town_hall()      |
| + current_town_hall()   |
| + help()                |
+-------------------------+
          ^
          |
+-----------------------------+
|       TownHall (Agent)      |
+-----------------------------+
| - services: list            |
| - request_services: Queue   |
+-----------------------------+
| + __init__(name)            |
| + add_service()             |
| + remove_service()          |
| + show_services()           |
| + show_services_queue()     |
| + add_request_service()     |
| + process_request_service() |
| + help()                    |
+-----------------------------+
          ^
          |
+---------------------------+
|      AgentManager         |
+---------------------------+
| - agents: dict            |
| - TIME_THRESHOLD: int     |
+---------------------------+
| + add_agent()             |
| + remove_agent()          |
| + list_agents()           |
| + check_ready_services()  |
| + load_agents_from_file() |
+---------------------------+
          ^
          |
+-------------------------------+
|     CitySimulation            |
+-------------------------------+
| - agent_manager: AgentManager |
| - ERROR_MESSAGES: dict        |
+-------------------------------+
| + help_town_hall()            |
| + help_client()               |
| + help()                      |
| + command_loop()              |
| + process_command()           |
+-------------------------------+
```