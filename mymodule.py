import random

class Game:
    def __init__(self):
        self.choice = None
        self.rmdoor = None
        self.tresor = random.randint(0, 2)

        # Initialize doors list with placeholders
        self.doors = ["_" for _ in range(3)]

        # Mark the treasure door with $
        self.doors[self.tresor] = "$"

    def make_choice(self, choice):
        self.choice = choice

        # Mark the player's chosen door with *
        self.doors[self.choice] = "*"

    def check_result(self):
        # Return 1 if player wins, 0 if not
        return int(self.tresor == self.choice)

    def remove_door(self):
        # Select a door to remove that is neither the treasure door nor the player's choice
        available_doors = [i for i in range(3) if i != self.tresor and i != self.choice]
        self.rmdoor = random.choice(available_doors)

        # Mark the removed door with X
        self.doors[self.rmdoor] = "X"

    def switch_choice(self):
        # Select a door to switch to that is neither the original choice nor the removed door
        available_doors = [i for i in range(3) if i != self.choice and i != self.rmdoor]

        # Mark the original choice door as _
        self.doors[self.choice] = "_"

        # Randomly choose a new door and mark it with *
        self.choice = random.choice(available_doors)
        self.doors[self.choice] = "*"

    def __str__(self):
        # String representation of the doors
        return " ".join(self.doors)

def play_single_game():
    game = Game()

    print("New game:", game)

    chosen_door = random.randint(0, 2)
    game.make_choice(chosen_door)
    print("After choosing door:", game)

    game.remove_door()
    print("After removing a door:", game)

    game.switch_choice()
    print("After switching choice:", game)

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

        chosen_door = random.randint(0, 2)
        game.make_choice(chosen_door)
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

# Simulate multiple games without switching choice
print("If I never switch my choice:")
print("-------------------------------")
simulate_multiple_games(num_games=1000, switch_choice=False)

# Simulate multiple games with always switching choice
print("\nIf I always switch my choice:")
print("-------------------------------")
simulate_multiple_games(num_games=1000, switch_choice=True)
