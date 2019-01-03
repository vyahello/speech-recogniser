from abc import ABC, abstractmethod
import sys
from lib.engines import Engine
from lib.quotes import Quote, CheerUpQuote, JokeQuote


class Robot(ABC):
    """Represent abstract robot."""

    @abstractmethod
    def say(self, speech: str) -> None:
        """Say some speech."""
        pass

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
    def say_bye(self) -> None:
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


class Jack(Robot):
    """Represent robot `Jack`."""

    def __init__(self, speech_engine: Engine) -> None:
        self._engine = speech_engine
        self._cheer_to_quote: Quote = CheerUpQuote
        self._joke_quote: Quote = JokeQuote

    def cheer_up(self) -> None:
        self.say(self._cheer_to_quote.choose_random())

    def say_joke(self) -> None:
        self.say(self._joke_quote.choose_random())

    def say_summary(self) -> None:
        self.say(f"My name is {self.__class__.__name__} and i have immortal age, I was born to help you.")

    def say_unknown(self) -> None:
        self.say("I do not understand what you are talking about. Please say it one more time!")

    def say_bye(self) -> None:
        self.say("Im glad i did my job, see you later my master!")
        sys.exit()

    def say_hello(self) -> None:
        self.say('Hello, my master! How the things are going')

    def say_things_going(self) -> None:
        self.say("I\'m doing just awesome, how the gorgeous day isn\'t it?")

    def say(self, speech: str) -> None:
        self._engine.translate_speech(speech)
