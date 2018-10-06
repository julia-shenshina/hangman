import pytest

from hangman import Hangman


@pytest.fixture
def patched_hangman():
    hangman = Hangman()
    hangman.VOCABULARY = ["test"]
    hangman.create_game()
    return hangman
