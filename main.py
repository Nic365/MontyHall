from mymodule import Game
import random

def play_single_game():
    game = Game()
    print("New game:", game.doors)
    game.make_choice(random.randint(0, 2))
    print("After choice:", game.doors)
    game.remove_door()
    print("After removing a door:", game.doors)
    game.switch_choice()
    print("After switching choice:", game.doors)
    result = game.check_result()
    print(result)

    if result:
        print("Congratulations! You won!")
    else:
        print("Sorry! You lost!")

def simulate_multiple_games(num_games, switch_choice):
    wins = 0
    losses = 0

    for _ in range(num_games):
        game = Game()
        game.make_choice(random.randint(0, 2))
        game.remove_door()

        if switch_choice:
            game.switch_choice()

        if game.check_result():
            wins += 1
        else:
            losses += 1

    print("Wins:", wins)
    print("Losses:", losses)
    win_percentage = round(100 * wins / (wins + losses), 2)
    print("Win percentage:", win_percentage, "%")

# Testing 

# Uncomment the line below to see the steps and result of a single game
# play_single_game()

print("If I never switch my choice:")
print("-------------------------------")
simulate_multiple_games(1000, switch_choice=False)

print("\nIf I always switch my choice:")
print("-------------------------------")
simulate_multiple_games(1000, switch_choice=True)
