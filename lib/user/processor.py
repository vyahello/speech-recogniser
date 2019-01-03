from abc import ABC, abstractmethod
from lib.robot.robots import Robot


class Processor(ABC):
    """Represent abstract processor."""

    @abstractmethod
    def recognise_command(self, command: str) -> str:
        """Recognise the input command."""
        pass


class SpeechProcessor(Processor):
    """Represent speech processor."""
    
    def __init__(self, robot: Robot) -> None:
        self._robot = robot
    
    def recognise_command(self, command: str) -> None:
        if 'hello' in command:
            self._robot.say_hello()
        elif 'how are you' in command:
            self._robot.say_things_going()
        elif 'joke' in command:
            self._robot.say_joke()
        elif 'cheer me up' in command:
            self._robot.cheer_up()
        elif 'who are you' in command:
            self._robot.say_summary()
        elif 'goodbye' in command:
            self._robot.say_goodbye()
        else:
            self._robot.say_unknown()
