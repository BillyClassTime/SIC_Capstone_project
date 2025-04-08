class Agent:
    """Clase base para todos los agentes en el sistema."""
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

    def describe(self):
        return self.__str__()

class Client(Agent):
    """Clase que representa a un cliente que interactúa con el ayuntamiento."""
    def __init__(self, name):
        super().__init__(name)
        self.town_hall_stack = Stack()  # En que ayuntamiento se encuentra

    def enter_town_hall(self, town_hall_name):
        """Método para marcar la entrada en un ayuntamiento."""
        self.town_hall_stack.push(town_hall_name)
        print(f'{self.name} entered {town_hall_name}.')

    def exit_town_hall(self):
        """Método para marcar la salida del último ayuntamiento visitado."""
        town_hall_name = self.town_hall_stack.pop()
        if town_hall_name:
            print(f'{self.name} exited {town_hall_name}.')
        else:
            print(f'{self.name} is not in any town hall.')

    def current_town_hall(self):
        """Método para obtener el ayuntamiento actual."""
        return self.town_hall_stack.peek()    
    
    HELP_MESSAGES = {
        "add_client": "client add_client <client_name>: Add a new client to the system.",
        "show_all": "client show_all: Show the list of all clients in the system.",
        "remove_client": "client remove_client <client_name>: Remove a client from the system.",
        "request_service": "client request_service <client_name> <town_hall_name> <service_name>: Request a specific service from the town hall.",
        "enter_town_hall": "client enter_town_hall <client_name> <town_hall_name>: Allow a client to enter the town hall.",
        "exit_town_hall": "client exit_town_hall <client_name> <town_hall_name>: Allow a client to exit the town hall.",
        "quit": "q: Exit the simulation."
    }

    @classmethod
    def help(cls):
        """Muestra los comandos disponibles para los clientes."""
        print("Available commands for client:")
        for command, description in cls.HELP_MESSAGES.items():
            print(f"- {description}")


class TownHall(Agent):
    """Clase que representa el ayuntamiento y sus servicios."""
    def __init__(self, name):
        super().__init__(name)
        self.services = []                              # Lista de servicios ofrecidos por el ayuntamiento
        self.request_services = Queue()                 # 

    def add_service(self, service_name):
        """Añade un nuevo servicio al ayuntamiento."""
        self.services.append(service_name)
        print(f'Service {service_name} added to {self.name}.')

    def remove_service(self, service_name):
        """Elimina un servicio del ayuntamiento."""
        if service_name in self.services:
            self.services.remove(service_name)
            print(f'Service {service_name} removed from {self.name}.')
        else:
            print(f'Service {service_name} not found in {self.name}.')

    def show_services(self):
        """Muestra la lista de servicios disponibles en el ayuntamiento."""
        print(f'Services offered by {self.name}:')
        for service in self.services:
            print(f'- {service}')

    def show_services_queue(self):
        if not self.request_services.is_empty():
            print(f"Services in queue for town hall '{self.name}':")
            for request in self.request_services.queue:
                print(f"Client: {request['client_name']}, Service: {request['service_name']}, Timestamp: {round(request['timestamp'],0)}")
        else:
            print(f"No services in queue for town hall '{self.name}'.")

    def add_request_service(self,client_name, service_name):
        """Añade una solicitud de servicio a la cola."""
        if service_name in self.services:
            timestamp = time.time()                       # Marca de tiempo de la solicitud
            request = {
                'client_name': client_name,
                'service_name': service_name,
                'timestamp': timestamp
            }
            self.request_services.enqueue(request)         # Encolar la solicitud            
        else:
            print(f"the service '{service_name}' is not available in the town hall '{self.name}'.")

    def process_request_service(self):
        """Atiende la primera solicitud en la cola si hay alguna."""
        if not self.request_services.is_empty():
            request = self.request_services.dequeue()      # Desencolar la solicitud
            client_name = request['client_name']
            service_name = request['service_name']
            timestamp = request['timestamp']
            print(f"Requested service was attended: {service_name} for client {client_name} from town hall {self.name}.")
        else:
            print(f"No requests in the queue for town hall '{self.name}'.")

    HELP_MESSAGES = {
        "add_town_hall": "town_hall add_town_hall <town_hall_name>: Add a new town hall to the system.",
        "show_all": "town_hall show_all: Show the list of all town halls in the system.",
        "add_service": "town_hall add_service <town_hall_name> <service_name>: Add a new service offered by a town hall.",
        "show_services": "town_hall show_services: Show the list of services available at all town halls in the system.",
        "show_services_specific": "town_hall show_services <town_hall_name>: Show the list of services available at a specific town hall.",
        "remove_service": "town_hall remove_service <town_hall_name> <service_name>: Remove a service from a town hall.",
        "show_service_queue": "town_hall show_service_queue <town_hall_name>: Show the list of services queued for a town hall.",
        "town_hall remove_town_hall": "town_hall remove_town_hall <town_hall_name>: Remove a town hall from the system.",
        "quit": "q: Exit the simulation."
    }

    @classmethod
    def help(cls):
        """Muestra los comandos disponibles para los ayuntamientos."""
        print("Available commands for town_hall:")
        for command, description in cls.HELP_MESSAGES.items():
            print(f"- {description}")

class AgentManager:
    """Clase base para gestionar la creación y eliminación de agentes."""
    def __init__(self):
        self.agents = {}                    # Diccionario para almacenar agentes
        self.TIME_THRESHOLD = 10            # Umbral de 10 segundos

    def filter_agents(self,*agents_types):
        """Filtra agentes según los tipos proporcionados."""
        filtered_agents = {
            name: agent for name, agent in agents.items()
            if isinstance(agent, tuple(agents_types))      # Filtrar según tipos
        }
        return filtered_agents
    
    def get_agent_by_name(self, agent_name, agent_type):
        """Devuelve el agente con el nombre dado y tipo específico, o None si no se encuentra."""
        return next((agent for agent in agents.values() 
                     if isinstance(agent, agent_type) and agent.name == agent_name), None)

    def add_agent(self, agent_type, agent_name):
        """Añade un nuevo agente al sistema."""
        if isinstance(agent_type, type) and agent_type == Client: 
            agents[agent_name] = Client(agent_name)
        elif isinstance(agent_type, type) and agent_type == TownHall:
            agents[agent_name] = TownHall(agent_name)
        else:
            print(f"Invalid agent type: {agent_type}. Please use valid agent.")
            return
            
        print(f'{agent_type.__name__} {agent_name} added to the system.')

    def remove_agent(self, agent_name):
        """Elimina un agente del sistema."""
        if agent_name in agents:
            del agents[agent_name]
            print(f'Agent {agent_name} removed from the system.')
        else:
            print(f'Agent {agent_name} not found.')

    def list_agents(self, agent_type=None):
        """Muestra todos los agentes o filtra por clientes o ayuntamientos en el sistema."""
        if agent_type:
            print(f"Current {agent_type.__name__}(s):")
            filtered_agents = self.filter_agents(agent_type)
            for agent in filtered_agents.values():               # Imprimir descripciones de los agentes filtrados
                print(agent.describe())
        else:
            print("Current agents:")
            for agent in agents.values():
                print(agent.describe())     

    def check_ready_services(self):
        """Verifica si hay servicios listos para ser atendidos por cada ayuntamiento."""
        filtered_agents = self.filter_agents(TownHall)  # Filtrar solo los ayuntamientos
        for town_hall in filtered_agents.values():
            while not town_hall.request_services.is_empty():  # Procesar todos los servicios en la cola
                if self.is_time_to_serve(town_hall):  # Verificar si es tiempo de atender el servicio
                    town_hall.process_request_service()  # Procesar el servicio
                else:
                    break  # Salir si no es tiempo de procesar el siguiente servicio

    def is_time_to_serve(self, town_hall):
        """Verifica si es el momento de atender el siguiente servicio en la cola."""
        if not town_hall.request_services.is_empty():
            last_request = town_hall.request_services.peek()  # Obtenemos la última solicitud
            current_time = time.time()                        # Método que deberías implementar para obtener el tiempo actual
            return (current_time - last_request['timestamp']) >= self.TIME_THRESHOLD  # Define el umbral

        return False        
    
    def validate_client_location(self, client, town_hall_name):
        if client.current_town_hall() is None:
            print(f'Client {client.name} cannot perform this action because not in it.')
            return False
        elif client.current_town_hall() != town_hall_name:
            print(f'Client {client.name} is in a different town hall: {client.current_town_hall()}.')
            return False
        return True

    def load_agents_from_file(self, file_path):
        """Carga agentes desde un fichero JSON."""

        import json
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Cargar town_halls
            for town_hall_name, town_hall_data in data.get("town_halls", {}).items():
                self.add_agent(TownHall, town_hall_name)
                town_hall = self.get_agent_by_name(town_hall_name, TownHall)
                if town_hall:
                    # Añadir servicios
                    for service in town_hall_data.get("services", []):
                        town_hall.add_service(service)
                    # Añadir solicitudes en cola
                    for request in town_hall_data.get("queue", []):
                        town_hall.add_request_service(request["client_name"], request["service_name"])

            # Cargar clients
            for client_name, client_data in data.get("clients", {}).items():
                self.add_agent(Client, client_name)
                client = self.get_agent_by_name(client_name, Client)
                if client and client_data.get("current_town_hall"):
                    client.enter_town_hall(client_data["current_town_hall"])

            print(f"--- Agents loaded successfully from {file_path}. --- ")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' is not a valid JSON file.")
        except Exception as e:
            print(f"An error occurred while loading agents: {e}")     


class CitySimulation:
    """Clase principal para gestionar la simulación de la ciudad."""
    def __init__(self):
        

        self.agent_manager = AgentManager()               # Instancia de la clase AgentManager
        self.agent_manager.agents = agents                # Asignar el diccionario global de agentes a la instancia

         
        self.ERROR_MESSAGES = {                           # Mensajes de error centralizados
            "invalid_command": "Error: Invalid command.",
            "town_hall_not_found": "Error: Town hall '{name}' not found.",
            "client_not_found": "Error: Client '{name}' not found.",
            "service_not_found": "Error: Service '{service}' not found in town hall '{town_hall}'.",
            "invalid_format": "Error: Invalid command format. Use '{expected_format}'."
        }
        
    def help_town_hall(self):
        """Displays the list of available commands."""
        TownHall.help()

    def help_client(self):
        """Muestra los comandos disponibles para los clientes."""
        Client.help()
        
    def help(self):
        """Displays general help information."""
        print("""
            Available help commands:
            - ? town_hall: Show available commands for town halls.
            - ? client: Show available commands for clients.
            - load_agents <file_path>: Load agents from a JSON file.
            - q: Exit the simulation.              
            """)

    def validate_command(self, parts, expected_length, error_key, expected_format):
        if len(parts) != expected_length:
            print(self.ERROR_MESSAGES[error_key].format(expected_format=expected_format))
            return False
        return True
    
    def validate_service_in_town_hall(self, town_hall, service_name):
        if service_name not in town_hall.services:
            print(self.ERROR_MESSAGES["service_not_found"].format(service=service_name, town_hall=town_hall.name))
            return False
        return True
    
    def get_agent_or_error(self, agent_name, agent_type, error_key):
        agent = self.agent_manager.get_agent_by_name(agent_name, agent_type)
        if not agent:
            print(self.ERROR_MESSAGES[error_key].format(name=agent_name))
        return agent

    def command_loop(self):
        """Bucle principal para gestionar comandos del usuario."""
        print("Starting city simulation... Type 'q' to exit")
        while True:
            command = input('> ')
            if command == 'q':
                break
            self.process_command(command)
            self.agent_manager.check_ready_services()        #verifica servicios de los ayuntamientos encolados 

    def process_command(self, command):
        """Procesa los comandos ingresados por el usuario."""
        parts = command.split()
        if not parts:
            return
        cmd = parts[0]
        if cmd == '?':
            if len(parts)==2:
                if parts[1]== 'town_hall':
                    self.help_town_hall()
                elif parts[1]== 'client':
                    self.help_client()
                else:
                    self.help()
            else:
                self.help()            # Llama al método de ayuda
            return
        elif cmd == 'load_agents':
            if self.validate_command(parts, 2, "invalid_format", "load_agents <file_path>"):
                _, file_path = parts
                self.agent_manager.load_agents_from_file(file_path)
        elif cmd == 'town_hall':
            if   parts[1] == 'add_town_hall':
                if self.validate_command(parts, 3, "invalid_format", "town_hall add_town_hall <town_hall_name>"):
                    _, _, town_hall_name = parts
                    self.agent_manager.add_agent(TownHall, town_hall_name)
            elif parts[1] == 'show_all':   
                if self.validate_command(parts, 2, "invalid_format", "town_hall show_all"):
                    self.agent_manager.list_agents(TownHall)
            elif parts[1] == 'add_service':                 
                if self.validate_command(parts, 4, "invalid_format", "town_hall add_service <town_hall_name> <service_name>"):
                    _, _, town_hall_name, service_name = parts
                    town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                    if town_hall:
                        if service_name not in town_hall.services:
                            town_hall.add_service(service_name)
                        else:
                            print(f"Service '{service_name}' already exists in town hall '{town_hall_name}'.")                
            elif parts[1] == 'show_services':
                if len(parts)==2:                           #town_hall show_services 
                    town_halls = self.agent_manager.filter_agents(TownHall)
                    if town_halls:
                        for town_hall in town_halls.values():
                            town_hall.show_services()
                    else:
                        print(self.ERROR_MESSAGES["town_hall_not_found"].format(name=town_hall_name))
                elif len(parts)==3:                         #town_hall show_services <town_hall_name>
                    _, _, town_hall_name = parts
                    town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                    if town_hall:
                        town_hall.show_services()
                else:
                    print(self.ERROR_MESSAGES["invalid_format"].format(expected_format="town_hall show_services <town_hall_name>"))
                    self.help_town_hall()
            elif parts[1] == 'show_service_queue':
                if self.validate_command(parts, 3, "invalid_format", "town_hall show_service_queue <town_hall_name>"):
                    _,_,town_hall_name = parts
                    town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                    if town_hall:
                        town_hall.show_services_queue()
            elif parts[1] == 'remove_service':             
                if self.validate_command(parts, 4, "invalid_format", "town_hall remove_service <town_hall_name> <service_name>"):
                    _, _, town_hall_name, service_name = parts
                    town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                    if self.validate_service_in_town_hall(town_hall, service_name):
                        town_hall.remove_service(service_name)
            elif parts[1] == 'remove_town_hall':  # town_hall remove_town_hall <town_hall_name>
                if self.validate_command(parts, 3, "invalid_format", "town_hall remove_town_hall <town_hall_name>"):
                    _, _, town_hall_name = parts
                    town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                    if town_hall:

                        # Verificar si hay procesos encolados
                        if not town_hall.request_services.is_empty():
                            print(f"Cannot remove town hall '{town_hall_name}' because it has queued processes.")
                            return
                        
                        # Verificar si el ayuntamiento tiene servicios
                        if town_hall.services:
                            print(f"Cannot remove town hall '{town_hall_name}' because it still has services.")
                            return
                        
                        # Verificar si hay clientes en el ayuntamiento
                        clients_in_town_hall = [
                            client for client in agents.values()
                            if isinstance(client, Client) and client.current_town_hall() == town_hall_name
                        ]
                        if clients_in_town_hall:
                            print(f"Cannot remove town hall '{town_hall_name}' because there are clients inside.")
                            return
                        
                        # Si pasa todas las verificaciones, eliminar el ayuntamiento
                        self.agent_manager.remove_agent(town_hall_name)                        
            else:
                print(self.ERROR_MESSAGES["invalid_command"])
                self.help_town_hall()
        elif cmd == 'client':
            if   parts[1] == 'add_client':                  #client add_client <client_name>
                if self.validate_command(parts, 3, "invalid_format", "client add_client <client_name>"):
                    _, _, client_name = parts
                    self.agent_manager.add_agent(Client, client_name)
            elif parts[1] == 'show_all':   
                if self.validate_command(parts, 2, "invalid_format", "client show_all"):
                    self.agent_manager.list_agents(Client)
            elif parts[1] == 'remove_client':
                if self.validate_command(parts, 3, "invalid_format", "client remove_client <client_name>"):
                    _, _, client_name = parts
                    self.agent_manager.remove_agent(client_name)
            elif parts[1] == 'request_service':  # client request_service <client_name> <town_hall_name> <service_name>
                if self.validate_command(parts, 5, "invalid_format", "client request_service <client_name> <town_hall_name> <service_name>"):
                    _, _, client_name, town_hall_name, service_name = parts
                    client = self.get_agent_or_error(client_name, Client, "client_not_found")
                    if client:
                        town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                        if town_hall:
                            if self.agent_manager.validate_client_location(client, town_hall_name):
                                if self.validate_service_in_town_hall(town_hall, service_name):
                                    town_hall.add_request_service(client_name, service_name)
                                    print(f"Client {client_name} requested service: {service_name}")
            elif parts[1] == 'enter_town_hall':             #client enter_town_hall <client_name> <town_hall_name>
                if self.validate_command(parts, 4, "invalid_format", "client enter_town_hall <client_name> <town_hall_name>"):
                    _, _, client_name, town_hall_name = parts
                    client =  self.get_agent_or_error(client_name, Client, "client_not_found")
                    if client:
                        town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                        if town_hall:
                            if client.current_town_hall() is None:
                                client.enter_town_hall(town_hall_name)
                                print(f'Client {client_name} entered the town hall.')
                            elif self.agent_manager.validate_client_location(client, town_hall_name):
                                print(f'Client {client_name} already in town hall {town_hall_name}.')
            elif parts[1] == 'exit_town_hall':              #client exit_town_hall <client_name> <town_hall_name>
                if self.validate_command(parts, 4, "invalid_format", "client exit_town_hall <client_name> <town_hall_name>"):
                    _, _, client_name, town_hall_name = parts
                    client =  self.get_agent_or_error(client_name, Client, "client_not_found")
                    if client:
                        town_hall = self.get_agent_or_error(town_hall_name, TownHall, "town_hall_not_found")
                        if town_hall:
                            if self.agent_manager.validate_client_location(client, town_hall_name):
                                client.exit_town_hall()
                                print(f'Client {client_name} exit the town hall {town_hall_name}.')
            else:
                print(self.ERROR_MESSAGES["invalid_format"])
                self.help_client()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return True if len(self.stack) == 0 else False
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return None if self.is_empty() else self.stack.pop()
    
    def peek(self):
        return None if self.is_empty () else self.stack[-1]

class Queue:
    
    def __init__(self):
        self.queue = []
    
    def is_empty (self):
        return True if len(self.queue) == 0 else False
    
    def peek(self):
        return None if self.is_empty () else self.queue[0]
    
    def enqueue (self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)
    
    def size(self):
        return len(self.queue)


# Diccionario global para almacenar agentes
agents = {}

import time
if __name__ == "__main__":
    simulation = CitySimulation()
    simulation.command_loop()


