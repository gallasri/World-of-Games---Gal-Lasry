from Live import load_game, welcome
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

def play_game(game_choice, difficulty):
    if game_choice == 1:
        game = MemoryGame(difficulty)
    elif game_choice == 2:
        game = GuessGame(difficulty)
    elif game_choice == 3:
        game = CurrencyRouletteGame(difficulty)
    else:
        print("Invalid game choice.")
        return
    print("You won!" if game.play() else "You lost!")

print(welcome("Player"))
game_choice, difficulty = load_game()
play_game(game_choice, difficulty)
