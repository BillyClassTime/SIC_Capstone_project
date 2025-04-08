import unittest
from io import StringIO
import sys
from CitySimulation import CitySimulation
import time

class TestCitySimulation(unittest.TestCase):
    test_number = 0
    def setUp(self):
        self.simulation = CitySimulation()

    def run_command_and_assert(self,command, expected_output):
        try:
            output = StringIO()
            sys.stdout = output
            self.simulation.process_command(command)
            sys.stdout = sys.__stdout__
            result_output = output.getvalue()
            TestCitySimulation.test_number +=1
            print(f'# {TestCitySimulation.test_number}\n>{command}\n{result_output.strip()}',end='')
            self.assertIn(expected_output, result_output)
            print(' "Test passsed!"')
        except AssertionError:
            print()
            print("="*40)
            print(' "Test not passsed!"') 
            print("="*40)
            print(f'AssertionError: Expected output\n"{expected_output}"\nnot found in actual output:\n"{result_output.strip()}"')
            follow=input("q: quit, press other key continue...")
            if follow=='q':
                sys.exit(1)


    def test_commands(self):
        print('testing ...')

        # Cliente entra a un ayuntamiento
        self.run_command_and_assert('client add_client Billy', 'Client Billy added to the system.')
        self.run_command_and_assert('town_hall add_town_hall Pinto', 'TownHall Pinto added to the system.')
        self.run_command_and_assert('client enter_town_hall Billy Pinto', 
                                    'Billy entered Pinto.\nClient Billy entered the town hall.')

        # Cliente solicita un servicio
        self.run_command_and_assert('town_hall add_service Pinto Empadronar', 'Service Empadronar added to Pinto.')

        self.run_command_and_assert('client request_service Billy Pinto Empadronar', 
                                    'Client Billy requested service: Empadronar')

        #special case with timestamp
        timestamp = round(time.time(),0)
        self.run_command_and_assert('town_hall show_service_queue Pinto', 
                                    f"Services in queue for town hall 'Pinto':\nClient: Billy, Service: Empadronar, Timestamp: {timestamp}")
        
        # Cliente sale de un ayuntamiento
        self.run_command_and_assert('client exit_town_hall Billy Pinto', 
                                    'Billy exited Pinto.\nClient Billy exit the town hall Pinto.')


        # Cliente intenta salir de un ayuntamiento en el que no está
        self.run_command_and_assert('client exit_town_hall Billy Pinto', 
                                    'Client Billy can not exit of town hall Pinto, because not in it')

        # Mostrar servicios y eliminar servicio
        self.run_command_and_assert('town_hall show_services Pinto', 'Services offered by Pinto:\n- Empadronar')
        self.run_command_and_assert('town_hall remove_service Pinto Empadronar', 'Service Empadronar removed from Pinto.')

        # Eliminar cliente y ayuntamiento
        time.sleep(10) # Esperar 10 segundos para que el ayuntamiento se elimine
        self.simulation.agent_manager.check_ready_services()
        self.run_command_and_assert('client remove_client Billy', 'Agent Billy removed from the system.')
        self.run_command_and_assert('town_hall remove_town_hall Pinto', 'Agent Pinto removed from the system.')
        

    def test_remove_town_hall_with_restrictions(self):
        print('testing remove_town_hall with restrictions...')
    
        # Agregar un ayuntamiento
        self.run_command_and_assert('town_hall add_town_hall Pinto', 'TownHall Pinto added to the system.')
    
    
        # No se puede eliminar un ayuntamiento con procesos encolados
        self.run_command_and_assert('town_hall add_service Pinto Empadronar', 'Service Empadronar added to Pinto.')
        self.run_command_and_assert('client add_client Billy', 'Client Billy added to the system.')
        self.run_command_and_assert('client enter_town_hall Billy Pinto', 
                                    'Billy entered Pinto.\nClient Billy entered the town hall.')
        self.run_command_and_assert('client request_service Billy Pinto Empadronar', 
                                    'Client Billy requested service: Empadronar')
        self.run_command_and_assert('town_hall remove_town_hall Pinto', 
                                    "Cannot remove town hall 'Pinto' because it has queued processes.")
    
        # Procesar los servicios en cola
        time.sleep(10)  # Esperar el tiempo necesario para que se cumpla el umbral
        self.simulation.agent_manager.check_ready_services()
    
        # No se puede eliminar un ayuntamiento con servicios
        self.run_command_and_assert('town_hall remove_town_hall Pinto', 
                                    "Cannot remove town hall 'Pinto' because it still has services.")
        self.run_command_and_assert('town_hall remove_service Pinto Empadronar', "Service Empadronar removed from Pinto.")

        # No se puede eliminar un ayuntamiento con clientes
        self.run_command_and_assert('town_hall remove_town_hall Pinto',
                                    "Cannot remove town hall 'Pinto' because there are clients inside.")
        self.run_command_and_assert('client exit_town_hall Billy Pinto', 
                                    'Billy exited Pinto.\nClient Billy exit the town hall Pinto.')

        # Intentar eliminar el ayuntamiento nuevamente
        self.run_command_and_assert('town_hall remove_town_hall Pinto', 'Agent Pinto removed from the system.')
    
    def test_client_exit_town_hall(self):
        print('testing client exit town hall...')

        # Agregar un cliente y un ayuntamiento
        self.run_command_and_assert('client add_client Billy', 'Client Billy added to the system.')
        self.run_command_and_assert('town_hall add_town_hall Pinto', 'TownHall Pinto added to the system.')

        # Cliente entra al ayuntamiento
        self.run_command_and_assert('client enter_town_hall Billy Pinto', 
                                    'Billy entered Pinto.\nClient Billy entered the town hall.')

        # Cliente sale del ayuntamiento
        self.run_command_and_assert('client exit_town_hall Billy Pinto', 
                                    'Billy exited Pinto.\nClient Billy exit the town hall Pinto.') 

    def test_error_handling(self):
        print('testing error handling...')


        self.run_command_and_assert('client add_client Billy', 'Client Billy added to the system.')

        # Cliente intenta entrar a un ayuntamiento inexistente
        self.run_command_and_assert('client enter_town_hall Billy NonExistentTownHall', 
                                    "Town hall 'NonExistentTownHall' not found.")

        # Cliente intenta salir de un ayuntamiento inexistente
        self.run_command_and_assert('client exit_town_hall Billy NonExistentTownHall', 
                                    "Town hall 'NonExistentTownHall' not found.")

        # Cliente intenta solicitar un servicio inexistente
        self.run_command_and_assert('town_hall add_town_hall Pinto', 'TownHall Pinto added to the system.')
        self.run_command_and_assert('client enter_town_hall Billy Pinto', 
                                    'Billy entered Pinto.\nClient Billy entered the town hall.')
        self.run_command_and_assert('client request_service Billy Pinto NonExistentService', 
                                    "Service 'NonExistentService' not found in town hall 'Pinto'.")

        # Cliente intenta eliminar un cliente inexistente
        self.run_command_and_assert('client remove_client NonExistentClient', 
                                    "Agent NonExistentClient not found.")

        # Ayuntamiento intenta eliminar un servicio inexistente
        self.run_command_and_assert('town_hall remove_service Pinto NonExistentService', 
                                    "Service NonExistentService not found in Pinto.")
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCitySimulation)
    unittest.TextTestRunner(verbosity=2).run(suite)
