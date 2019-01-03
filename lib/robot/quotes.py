from abc import ABC, abstractmethod
from random import choice
from typing import Tuple


class Quote(ABC):
    """Represent abstract quote."""

    @classmethod
    @abstractmethod
    def choose_random(cls) -> str:
        """Choose random quote."""
        pass


class CheerUpQuote(Quote):
    """Represent cheer up quote."""

    _cheer_up_quotes: Tuple[str] = (
        "Life is too short for us to dwell on sadness. Cheer up and live life to the fullest",
        "Keep believing, keep growing. Heaven will be cheering you on today, tomorrow, forever",
        "In the middle of difficulty lies opportunity",
        "It’s hard to beat a person who never gives up",
        "Sometimes you have to just pick yourself up and carry on",
        "Cheer up when the night comes, because mornings always give you another chance",
    )

    @classmethod
    def choose_random(cls) -> str:
        return choice(cls._cheer_up_quotes)


class JokeQuote(Quote):
    """Represent joke quote."""

    _jokes: Tuple[str] = (
        "I'm retired. I was tired yesterday and I'm tired again today",
        "I already want to take a nap tomorrow",
        "Do not judge me. I was born to be awesome, not perfect",
        "Stop worrying about the world ending today. It's already tomorrow in Australia",
        "Life is short, smile while you still have teeth",
        "Life is Short – Talk Fast!",
        "I know that I am intelligent, because I know that I know nothing",
        "I do not like morning people... or mornings, or people"
    )

    @classmethod
    def choose_random(cls) -> str:
        return choice(cls._jokes)


class Quotes:
    """Represent a bunch of quotes."""

    def __init__(self) -> None:
        self._cheer_up: Quote = CheerUpQuote
        self._joke: Quote = JokeQuote

    def cheer_up(self) -> Quote:
        """Return cheer up quotes."""
        return self._cheer_up

    def joke(self) -> Quote:
        """Return joke quotes."""
        return self._joke
