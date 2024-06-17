def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_choice = int(input("Enter your game choice: "))
    difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
    return game_choice, difficulty_level
