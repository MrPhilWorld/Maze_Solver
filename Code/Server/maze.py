from Engine import Engine
from LightControl import LightControl
from Memory import Memory
from ObstacleDetection import ObstacleDetection
from RobotStates import RobotStates
from StateMachine import *

from Ultrasonic import Ultrasonic
from Infrared import Infrared

MEMORY=Memory()
ENGINE=Engine()
ULTRASONIC=Ultrasonic()
LIGHT_CONTROL=LightControl()
INFRARED=Infrared()
OBSTACLE_DETECTION=ObstacleDetection()

def run(): 
    state_machine = StateMachine(RobotStates.FORWARD)
    
    try:
        while True:
            state_machine.run()

    except KeyboardInterrupt:
        state_machine.reset()
        print ("\nEnd of program")

# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    run()