from Colors import Colors
from RobotStates import RobotStates
from State import State
from maze import LIGHT_CONTROL, ENGINE


class WinState(State):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        ENGINE.stop()

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        LIGHT_CONTROL.setColor(Colors.BLUE, 50)
        LIGHT_CONTROL.setColor(Colors.GREEN, 50)
        LIGHT_CONTROL.setColor(Colors.YELLOW, 50)
        LIGHT_CONTROL.setColor(Colors.ORANGE, 50)
        LIGHT_CONTROL.setColor(Colors.RED, 50)
        
        return RobotStates.WIN