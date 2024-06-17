import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = self.generate_number()

    def generate_number(self):
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return int(input("Guess a number between 1 and " + str(self.difficulty) + ": "))

    def compare_results(self, user_guess):
        return user_guess == self.secret_number

    def play(self):
        user_guess = self.get_guess_from_user()
        return self.compare_results(user_guess)
