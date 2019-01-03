from abc import ABC, abstractmethod
from lib.robot.robots import Robot
from lib.user.commands import Command, UserCommand
from lib.user.interactions import RecognizerOfAudioSource, UserAudioSource
from lib.user.processor import Processor, SpeechProcessor


class Recogniser(ABC):
    """Represent abstract recogniser."""

    @abstractmethod
    def run(self) -> None:
        """Run a recogniser."""
        pass


class SpeechRecogniser(Recogniser):
    """Concrete speech recogniser."""

    def __init__(self, robot: Robot) -> None:
        self._processor: Processor = SpeechProcessor(robot)
        self._command: Command = UserCommand(robot, RecognizerOfAudioSource(), UserAudioSource())

    def run(self) -> None:
        self._processor.recognise_command(self._command.process())
