import random


############
# Example 4: 
############
"""
https://en.wikipedia.org/wiki/Monty_Hall_problem

Suppose you're on a game show, and you're given the choice of three doors:

1) Behind one door is a car; behind the others, goats. 

2) You pick a door, say No. 1 (but not opening it) and the host, who knows what are
behind the doors, opens another door, say No. 3, which has a goat. He then says to you,
"Do you want to pick door No. 2?" Is it to your advantage to switch your choice?


Note: the host must always open a door to reveal a goat and never the car.

Under the standard assumptions, contestants who switch have a 2/3
chance of winning the car, while contestants who stick to their initial
choice have only a 1/3 chance.
"""


def pick_a_door():
    return random.randrange(1, 4)
 

# host open a random door (contain goat) other than the car door
def host_open_a_door(car_door, user_door):

    open_door = pick_a_door()
    # if the open door is the car door or the user's door, re-pick until it is not.
    while (open_door == car_door or open_door == user_door):
        open_door = pick_a_door()
    
    return open_door

def run_game_once(switch):

    # Step 1: setup the car in a random door
    car_door = pick_a_door()


    # Step 2: User select a random door
    user_door = pick_a_door()


    # Step 3: user select a random goat door (out of 2)
    host_door = host_open_a_door(car_door, user_door)
    

    # Step 4: user switch door
    if (switch):
        a = [1, 2, 3]
        a.remove(host_door)
        a.remove(user_door)        
        user_door = a[0]
    
    # now check if user wins
    if (user_door == car_door):
        return True
    else:
        return False



def run_game_many (n, switch):
    num_wins = 0
    for i in range(n):
        result = run_game_once(switch)
        if (result):
            num_wins = num_wins + 1

    print ("# Run", n, "Monty Hall games with switching =", switch)
    print ("#  user won =", num_wins, "games")
    print ("#  user lose =", n-num_wins, "games")
    print ("#  prob. win. =", num_wins / n)
    

# switch door
run_game_many (100000, True)

# do not switch door
run_game_many (100000, False)    
