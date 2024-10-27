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

        self.run_command_and_assert('client add_client Billy', 'Client Billy added to the system.')
        self.run_command_and_assert('town_hall add_town_hall Pinto', 'TownHall Pinto added to the system.')
        self.run_command_and_assert('client enter_town_hall Billy Pinto ', 
                                    'Billy entered Pinto.\nClient Billy entered the town hall.')
        
        self.run_command_and_assert('town_hall show_all', 'Current TownHall(s):\nPinto')
        self.run_command_and_assert('town_hall add_service Pinto Empadronar', 'Service Empadronar added to Pinto.')
        self.run_command_and_assert('town_hall show_services', 'Services offered by Pinto:\n- Empadronar')
        self.run_command_and_assert('town_hall show_services Pinto', 'Services offered by Pinto:\n- Empadronar')

        self.run_command_and_assert('client request_service Billy Pinto Empadronar','Client Billy requested service: Empadronar')
        #special case with timestamp
        timestamp = time.time()  
        self.run_command_and_assert('town_hall show_service_queue Pinto', 
                                    f"Services in queue for town hall 'Pinto':\nClient: Billy, Service: Empadronar, Timestamp: {timestamp:.2f}")
        self.run_command_and_assert('town_hall remove_service Pinto Empadronar', "Service Empadronar removed from Pinto.")
        
        self.run_command_and_assert('client show_all', "Current Client(s):\nBilly")
        self.run_command_and_assert('client remove_client Billy','Agent Billy removed from the system.')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCitySimulation)
    unittest.TextTestRunner(verbosity=2).run(suite)
