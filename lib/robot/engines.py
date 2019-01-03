import os
from abc import ABC, abstractmethod


class Engine(ABC):
    """Represent abstract engine."""

    @abstractmethod
    def translate_speech(self, speech: str) -> int:
        """Translate speech from human representation to machine one."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Traverse string representation of an object."""
        pass


class SpeechEngine(Engine):
    """Represent robot speech engine."""

    def __init__(self, engine_name: str = 'Default engine') -> None:
        self._name: str = engine_name

    def translate_speech(self, speech: str) -> int:
        return os.system(f"say {speech}")

    def __str__(self) -> str:
        return f"{self._name} engine is working on translation..."
