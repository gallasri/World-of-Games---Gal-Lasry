import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        return list(map(int, input("Enter the sequence of numbers: ").split()))

    def is_list_equal(self, seq, user_seq):
        return seq == user_seq

    def play(self):
        seq = self.generate_sequence()
        print("Remember this sequence: " + ' '.join(map(str, seq)))
        time.sleep(0.7)
        print("\r" + " " * 50 + "\r", end="")
        user_seq = self.get_list_from_user()
        return self.is_list_equal(seq, user_seq)
