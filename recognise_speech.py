from lib.robot.engines import SpeechEngine
from lib.robot.robots import JackRobot
from lib.user.recogniser import Recogniser, SpeechRecogniser


def _recognise_speech() -> None:
    """Main speech recogniser program to run."""
    recogniser: Recogniser = SpeechRecogniser(
        JackRobot(
            SpeechEngine(
            )
        )
    )

    while True:
        recogniser.run()


if __name__ == '__main__':
    _recognise_speech()
