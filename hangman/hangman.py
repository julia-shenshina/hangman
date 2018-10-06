import random
import re


class Hangman:
    MAX_MISTAKES_NUMBER = 5
    VOCABULARY = ["hello", "algorithm", "time", "name", "computer"]

    def __init__(self):
        self.word = None
        self.mistakes_count = None
        self.opened_letters = None
        self.closed_letters_count = None

    def print_opened_letters(self):
        print("The word:\t{}".format("".join(self.opened_letters)))

    def print_mistake_message(self):
        print("Missed, mistake {} out of {} \n".format(self.mistakes_count, self.MAX_MISTAKES_NUMBER))

    def create_game(self):
        self.word = random.choice(self.VOCABULARY)
        self.mistakes_count = 0
        self.closed_letters_count = len(self.word)
        self.opened_letters = ["*"] * self.closed_letters_count

    def guess(self, letter):
        assert self.has_attempts()
        if letter in self.opened_letters:
            return None
        if letter not in self.word:
            self.mistakes_count += 1
            return False
        else:
            indexes = [x.start(0) for x in re.finditer(letter, self.word)]
            for index in indexes:
                self.opened_letters[index] = letter
            self.closed_letters_count -= len(indexes)
            return True

    def word_opened(self):
        return self.closed_letters_count == 0

    def has_attempts(self):
        return self.mistakes_count < self.MAX_MISTAKES_NUMBER


def main():
    hangman = Hangman()
    hangman.create_game()
    while hangman.has_attempts() and not hangman.word_opened():
        hangman.print_opened_letters()
        print("Guess the letter")
        letter = input()
        if len(letter) > 1 or not letter.isalpha():
            print("Please, input single letter")
            continue
        decision = hangman.guess(letter)
        if decision is None:
            print("This letter was already opened")
        elif not decision:
            hangman.print_mistake_message()
    if hangman.word_opened():
        print("You win!")
    else:
        print("You lost.")


if __name__ == '__main__':
    main()
