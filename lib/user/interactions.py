from abc import ABC, abstractmethod
from typing import Any
from speech_recognition import Microphone, Recognizer, AudioData


class AudioSource(ABC):
    """Represent abstract audio input."""

    @abstractmethod
    def __enter__(self) -> Any:
        """Enter audio manager."""
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit audio manager."""
        pass


class UserAudioSource(AudioSource):
    """Represent user audio input."""

    def __init__(self) -> None:
        self._micro = Microphone()

    def __enter__(self) -> Microphone:
        return self._micro.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self._micro.__exit__(exc_type, exc_val, exc_tb)


class RecognizerOfAudioSource(AudioSource):
    """Represent recogniser of audio source."""

    def __init__(self) -> None:
        self._recogniser = Recognizer()

    def __enter__(self) -> Recognizer:
        return self._recogniser.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self._recogniser.__exit__(exc_type, exc_val, exc_tb)

    @property
    def pause(self) -> int:
        """Return seconds of non-speaking audio before a phrase is considered complete"""
        return self._recogniser.pause_threshold

    @pause.setter
    def pause(self, seconds: int) -> None:
        if not isinstance(seconds, int):
            raise TypeError('Seconds should be <int> data type.')

    def configure_noise(self, source: Microphone, duration: int = 1) -> None:
        self._recogniser.adjust_for_ambient_noise(source, duration)

    def listen(
            self,
            source: Microphone,
            timeout: int = None,
            phrase_time_limit: int = None,
            config: str= None
    ) -> AudioData:
        return self._recogniser.listen(source, timeout, phrase_time_limit, config)

    def recognise_google(
            self,
            audio_data: AudioData,
            key: int = None,
            language: str = "en-US",
            show_all: bool = False
    ) -> str:
        return self._recogniser.recognize_google(audio_data, key, language, show_all).lower()
