from abc import ABC, abstractmethod
from lib.robot.engines import Engine
from lib.robot.quotes import Quotes
from lib.robot.speech import Sayable, Speech


class Robot(ABC):
    """Represent abstract robot."""

    @abstractmethod
    def cheer_up(self) -> None:
        """Cheer up the master."""
        pass

    @abstractmethod
    def say_joke(self) -> None:
        """Say a joke."""
        pass

    @abstractmethod
    def say_summary(self) -> None:
        """Compose a say_summary about a robot."""
        pass

    @abstractmethod
    def say_unknown(self) -> None:
        """Unknown word to say."""
        pass

    @abstractmethod
    def say_goodbye(self) -> None:
        """Say bye."""
        pass

    @abstractmethod
    def say_hello(self) -> None:
        """Say hello."""
        pass

    @abstractmethod
    def say_things_going(self) -> None:
        """Say how is going."""
        pass


class JackRobot(Robot):
    """Represent robot named `Jack`."""

    def __init__(self, speech_engine: Engine) -> None:
        self._say: Sayable = Speech(speech_engine, Quotes())

    def cheer_up(self) -> None:
        self._say.cheer_up()

    def say_joke(self) -> None:
        self._say.joke()

    def say_summary(self) -> None:
        self._say.summary(
            name=self.__class__.__name__,
            age='with immortal'
        )

    def say_unknown(self) -> None:
        self._say.unknown()

    def say_goodbye(self) -> None:
        self._say.goodbye()

    def say_hello(self) -> None:
        self._say.hello()

    def say_things_going(self) -> None:
        self._say.things_going()
