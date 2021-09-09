import random


############
# Example 3: birthday paradox
############
# In the birthday problem, everyone says its birthday date, and we check if there
#  is a collision between any pair of people in the room.
def random_birthday ():
    return random.randrange(0, 366)


def run_game_once ():
    all_birthdays = []
    numbers = 0
    while (1):
        curr = random_birthday()
        numbers = numbers + 1
        if (curr in all_birthdays):
            break
        all_birthdays.append(curr)
            
    #print("# after generating ", numbers, " birthdays we found a match ")
    #print(all_birthdays)
    return numbers

run_game_once ()


# run the above game for many times
# and compute the average number for matching
def run_game_many (n):
    tot = 0
    for i in range(n):
        tot = tot + run_game_once ()
    ave = tot / n
    print ("# after run the game for", n, "times, ave. num. = ", ave)


# theoretical value should be about 24.617
run_game_many (10000)

