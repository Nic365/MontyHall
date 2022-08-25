from mymodule import Game
import random

# test 1 game
def just_one_game(): 
    g1 = Game()
    print("new game:", g1.doors)
    g1.make_choice(random.randint(0,2))
    print("after choice:",g1.doors)
    g1.remove_door()
    print("after remove:",g1.doors)
    g1.switch_choice()
    print("after switch:",g1.doors)
    print(g1.check_result())

    if g1.check_result():
        print("youhoo")
    else:
        print("boohoo")

def bunch_of_games(howmany, switch):
    win, lost = 0, 0
    for i in range(1, howmany):
        g1 = Game()
        # choisit une porte au hasard
        g1.make_choice(random.randint(0,2))
        # retirer une porte
        g1.remove_door()
        # on veux-tu changer ? 
        if switch:
            g1.switch_choice()
        # retenir le resultat
        if g1.check_result():
            win+=1
        else:
            lost+=1
    
    # stats
    print("Win:", win)
    print("lost:", lost)
    print(round(100 * win/(win+lost),2),"%")


# Testing 

# print("Just to see one game")
#just_one_game()

print("let's see a thousand games with no change")
bunch_of_games(1000, 0)

print("let's see a thousand games with F**** change")
bunch_of_games(1000, 1)
