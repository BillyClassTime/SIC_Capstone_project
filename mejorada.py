import time


# Base Classes
class Agent:
    """Clase base para todos los agentes en el sistema."""
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Agent: {self.name}"


class Client(Agent):
    """Clase que representa a un cliente que interactúa con el ayuntamiento."""
    def __init__(self, name):
        super().__init__(f"Cliente:{name}")
        self.town_hall_stack = Stack()

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


class TownHall(Agent):
    """Clase que representa el ayuntamiento y sus servicios."""
    def __init__(self, name):
        super().__init__(f"Town Hall:{name}")
        self.services = []
        self.request_queue = Queue()

    def add_service(self, service_name):
        """Añade un nuevo servicio al ayuntamiento."""
        if service_name not in self.services:
            self.services.append(service_name)
            print(f'Service {service_name} added to {self.name}.')
        else:
            print(f'Service {service_name} already exists in {self.name}.')

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

    def show_service_queue(self):
        """Muestra la cola de servicios pendientes."""
        if not self.request_queue.is_empty():
            print(f"Services in queue for town hall '{self.name}':")
            for request in self.request_queue.queue:
                print(f"Client: {request['client_name']}, Service: {request['service_name']}, Timestamp: {request['timestamp']:.2f}")
        else:
            print(f"No services in queue for town hall '{self.name}'.")

    def add_request(self, client_name, service_name):
        """Añade una solicitud de servicio a la cola."""
        if service_name in self.services:
            timestamp = time.time()
            self.request_queue.enqueue({
                'client_name': client_name,
                'service_name': service_name,
                'timestamp': timestamp
            })
            print(f"Request for service '{service_name}' by client '{client_name}' added to {self.name}.")
        else:
            print(f"Service '{service_name}' not available in {self.name}.")

    def process_request(self):
        """Procesa la primera solicitud en la cola."""
        if not self.request_queue.is_empty():
            request = self.request_queue.dequeue()
            print(f"Processed request: Client '{request['client_name']}', Service '{request['service_name']}'")
        else:
            print(f"No requests to process in {self.name}.")


# Utility Classes
class Stack:
    """Simple stack implementation."""
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None


class Queue:
    """Simple queue implementation."""
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0


# Agent Manager
class AgentManager:
    """Clase para gestionar todos los agentes en el sistema."""
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_type, name):
        if agent_type == 'client':
            self.agents[name] = Client(name)
        elif agent_type == 'town_hall':
            self.agents[name] = TownHall(name)
        else:
            print(f"Unknown agent type: {agent_type}")

    def get_agent(self, name, agent_type=None):
        agent = self.agents.get(name)
        if agent_type and not isinstance(agent, agent_type):
            return None
        return agent

    def list_agents(self, agent_type=None):
        if agent_type:
            return [agent for agent in self.agents.values() if isinstance(agent, agent_type)]
        return list(self.agents.values())


# City Simulation
class CitySimulation:
    """Clase principal para gestionar la simulación de la ciudad."""
    def __init__(self):
        self.agent_manager = AgentManager()

    def process_command(self, command):
        """Procesa los comandos ingresados por el usuario."""
        parts = command.split()
        if not parts:
            return
        cmd = parts[0]
        args = parts[1:]

        if cmd == 'town_hall':
            self.handle_town_hall_command(args)
        elif cmd == 'client':
            self.handle_client_command(args)
        else:
            print("Unknown command.")

    def handle_town_hall_command(self, args):
        """Procesa comandos relacionados con los ayuntamientos."""
        if args[0] == 'add':
            self.agent_manager.add_agent('town_hall', args[1])
        elif args[0] == 'show_all':
            town_halls = self.agent_manager.list_agents(TownHall)
            for town_hall in town_halls:
                print(town_hall.describe())
        elif args[0] == 'add_service':
            town_hall = self.agent_manager.get_agent(args[1], TownHall)
            if town_hall:
                town_hall.add_service(args[2])
        elif args[0] == 'show_services':
            town_hall = self.agent_manager.get_agent(args[1], TownHall)
            if town_hall:
                town_hall.show_services()
        elif args[0] == 'remove_service':
            town_hall = self.agent_manager.get_agent(args[1], TownHall)
            if town_hall:
                town_hall.remove_service(args[2])
        elif args[0] == 'show_service_queue':
            town_hall = self.agent_manager.get_agent(args[1], TownHall)
            if town_hall:
                town_hall.show_service_queue()

    def handle_client_command(self, args):
        """Procesa comandos relacionados con los clientes."""
        if args[0] == 'add':
            self.agent_manager.add_agent('client', args[1])

    def command_loop(self):
        """Bucle principal para gestionar comandos del usuario."""
        print("Starting city simulation... Type 'q' to exit.")
        while True:
            command = input("> ")
            if command == 'q':
                break
            self.process_command(command)


# Main Program
if __name__ == "__main__":
    simulation = CitySimulation()
    simulation.command_loop()