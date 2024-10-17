# Diccionario global para almacenar agentes
agents = {}

class Agent:
    """Clase base para todos los agentes en el sistema."""
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Agent: {self.name}"

class Client(Agent):
    """Clase que representa a un cliente que interactúa con el ayuntamiento."""
    def __init__(self, name):
        super().__init__(name)
        self.in_town_hall = False  # Estado de entrada en el ayuntamiento

class TownHall(Agent):
    """Clase que representa el ayuntamiento y sus servicios."""
    def __init__(self, name):
        super().__init__(name)
        self.services = []  # Lista de servicios ofrecidos por el ayuntamiento

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

class CitySimulation:
    """Clase principal para gestionar la simulación de la ciudad."""
    def add_agent(self, agent_type, agent_name):
        """Añade un nuevo agente al sistema."""
        if agent_type == 'client':
            agents[agent_name] = Client(agent_name)
        elif agent_type == 'town_hall':
            agents[agent_name] = TownHall(agent_name)
        print(f'{agent_type.capitalize()} {agent_name} added to the system.')

    def remove_agent(self, agent_name):
        """Elimina un agente del sistema."""
        if agent_name in agents:
            del agents[agent_name]
            print(f'Agent {agent_name} removed from the system.')
        else:
            print(f'Agent {agent_name} not found.')

    def list_agents(self):
        """Muestra todos los agentes en el sistema."""
        print("Current agents:")
        for agent in agents.values():
            print(agent.describe())

    def help(self):
        """Muestra la lista de comandos disponibles."""
        print("""
            Available commands:
            - town_hall add_service <service_name>: Add a new service offered by the town hall.
            - town_hall add_town_hall <town_hall_name>: Add a new town hall to the system.
            - client add_client <client_name>: Add a new client to the system.
            - client remove_client <client_name>: Remove a client from the system.
            - town_hall remove_service <service_name>: Remove a service from the town hall.
            - client enter_town_hall <client_name>: Allow a client to enter the town hall.
            - client request_service <client_name> <service_name>: Request a specific service from the town hall.
            - town_hall show_services: Show the list of services available at the town hall.
            - q: Exit the simulation.
            """)            

    def command_loop(self):
        """Bucle principal para gestionar comandos del usuario."""
        print("Starting city simulation... Type 'q' to exit")
        while True:
            command = input('> ')
            if command == 'q':
                break
            self.process_command(command)

    def process_command(self, command):
        """Procesa los comandos ingresados por el usuario."""
        parts = command.split()
        if not parts:
            return
        
        cmd = parts[0]
        
        if cmd == '?':
            self.help()  # Llama al método de ayuda
            return
        
        elif cmd == 'town_hall':
            if parts[1] == 'add_service':
                try:
                    _, _, service_name = parts
                    town_hall_name = next((name for name in agents if isinstance(agents[name], TownHall)), None)
                    if town_hall_name:
                        agents[town_hall_name].add_service(service_name)
                    else:
                        print("No town hall found.")
                except ValueError:
                    print("Error: Invalid add_service command format. Use 'town_hall add_service <service_name>'")
            
            elif parts[1] == 'remove_service':
                try:
                    _, _, service_name = parts
                    town_hall_name = next((name for name in agents if isinstance(agents[name], TownHall)), None)
                    if town_hall_name:
                        agents[town_hall_name].remove_service(service_name)
                    else:
                        print("No town hall found.")
                except ValueError:
                    print("Error: Invalid remove_service command format. Use 'town_hall remove_service <service_name>'")
            
            elif parts[1] == 'show_services':
                town_hall_name = next((name for name in agents if isinstance(agents[name], TownHall)), None)
                if town_hall_name:
                    agents[town_hall_name].show_services()
                else:
                    print("No town hall found.")
            elif parts[1] == 'add_town_hall':
                try:
                    _, _, town_hall_name = parts
                    self.add_agent('town_hall', town_hall_name)
                except ValueError:
                    print("Error: Invalid add_town_hall command format. Use 'town_hall add_town_hall <town_hall_name>'")

        elif cmd == 'client':
            if parts[1] == 'add_client':
                try:
                    _, _, client_name = parts
                    self.add_agent('client', client_name)
                except ValueError:
                    print("Error: Invalid add_client command format. Use 'client add_client <client_name>'")

            elif parts[1] == 'remove_client':
                try:
                    _, _, client_name = parts
                    self.remove_agent(client_name)
                except ValueError:
                    print("Error: Invalid remove_client command format. Use 'client remove_client <client_name>'")

            elif parts[1] == 'enter_town_hall':
                try:
                    _, _, client_name = parts
                    if client_name in agents and isinstance(agents[client_name], Client):
                        agents[client_name].in_town_hall = True
                        print(f'Client {client_name} entered the town hall.')
                    else:
                        print(f'Client {client_name} not found.')
                except ValueError:
                    print("Error: Invalid enter_town_hall command format. Use 'client enter_town_hall <client_name>'")

            elif parts[1] == 'request_service':
                try:
                    _, _, client_name, service_name = parts
                    if client_name in agents and isinstance(agents[client_name], Client):
                        town_hall_name = next((name for name in agents if isinstance(agents[name], TownHall)), None)
                        if town_hall_name and service_name in agents[town_hall_name].services:
                            print(f'Client {client_name} requested service: {service_name}')
                        else:
                            print(f'Service {service_name} not available.')
                    else:
                        print(f'Client {client_name} not found.')
                except ValueError:
                    print("Error: Invalid request_service command format. Use 'client request_service <client_name> <service_name>'")

        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    simulation = CitySimulation()
    simulation.command_loop()