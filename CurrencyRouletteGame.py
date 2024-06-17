import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self):
        usd_to_ils_rate = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()['rates']['ILS']
        random_usd = random.randint(1, 100)
        ils_value = random_usd * usd_to_ils_rate
        return (ils_value - (5 - self.difficulty), ils_value + (5 - self.difficulty), random_usd)

    def get_guess_from_user(self):
        return float(input("Guess the value in ILS: "))

    def play(self):
        interval, random_usd = self.get_money_interval()
        print("How much is " + str(random_usd) + " USD in ILS?")
        user_guess = self.get_guess_from_user()
        return interval[0] <= user_guess <= interval[1]
