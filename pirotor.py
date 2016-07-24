from flight_controller import FlightController
import sys
import time

try:
    flight_controller = FlightController('test')
    flight_controller.armMotors()
    time.sleep(2)
    #flight_controller.simpleExample()
    #flight_controller.manualControl()
    flight_controller.autonomousControl()
    flight_controller.stopMotors()
except KeyboardInterrupt:
    flight_controller.stopMotors()
    sys.exit()
