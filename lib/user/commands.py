from abc import ABC, abstractmethod
from speech_recognition import UnknownValueError, AudioData
from lib.robot.robots import Robot
from lib.user.interactions import RecognizerOfAudioSource, UserAudioSource


class Command(ABC):
    """Represent abstract command."""

    @abstractmethod
    def process(self) -> str:
        """Process the input command."""
        pass


class UserCommand(Command):
    """Represent user input command."""

    def __init__(self, robot: Robot, recogniser: RecognizerOfAudioSource, source: UserAudioSource) -> None:
        self._robot = robot
        self._recogniser = recogniser
        self._source = source

    def process(self) -> str:
        with self._source as source:
            self._recogniser.pause: int = 1
            self._recogniser.configure_noise(source)
            audio_data: AudioData = self._recogniser.listen(source)
        try:
            return self._recogniser.recognise_google(audio_data)
        except UnknownValueError:
            self._robot.say_unknown()
        return ''
