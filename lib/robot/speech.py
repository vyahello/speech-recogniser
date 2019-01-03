import sys
from abc import ABC, abstractmethod
from lib.robot.engines import Engine
from lib.robot.quotes import Quotes


class Sayable(ABC):
    """Certain sayable abstraction."""

    @abstractmethod
    def cheer_up(self) -> None:
        """Say to cheer up."""
        pass

    @abstractmethod
    def joke(self) -> None:
        """Say a joke."""
        pass

    @abstractmethod
    def summary(self, name: str, age: str) -> None:
        """Compose a summary about a robot."""
        pass

    @abstractmethod
    def unknown(self) -> None:
        """Unknown word to say."""
        pass

    @abstractmethod
    def goodbye(self) -> None:
        """Say bye."""
        pass

    @abstractmethod
    def hello(self) -> None:
        """Say hello."""
        pass

    @abstractmethod
    def things_going(self) -> None:
        """Say how is going."""
        pass


class Speech(Sayable):
    """Speech of particular robot."""

    def __init__(self, speech_engine: Engine, quotes: Quotes) -> None:
        self._engine = speech_engine
        self._quotes = quotes

    def cheer_up(self) -> None:
        self._translate(self._quotes.cheer_up().choose_random())

    def joke(self) -> None:
        self._translate(self._quotes.joke().choose_random())

    def summary(self, name: str, age: str) -> None:
        self._translate(f"My name is {name} and i'm {age} age, I was born to help you with your day to day things")

    def unknown(self) -> None:
        self._translate("I do not understand what you are talking about. Please say it one more time!")

    def goodbye(self) -> None:
        self._translate("I\'m glad I did my job, see you later my master!")
        sys.exit()

    def hello(self) -> None:
        self._translate('Hello, my master! How the things are going dude?')

    def things_going(self) -> None:
        self._translate("I\'m doing just awesome, how the gorgeous day isn\'t it?")

    def _translate(self, speech: str) -> None:
        self._engine.translate_speech(speech)
