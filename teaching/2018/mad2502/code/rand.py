"""
some examples of random number generator in python
"""
import random


# basic use of random flp/integer generator


# generate a uniform flp in [0, 1)
random.random()


# generate a uniform flp in [-10, 10)
random.uniform(-10, 10)


# uniform integers in [-2, 2]
random.randint(-2, 2)


# randrange fix the end point convention [-2, 2)
random.randrange(-2, 2)


# try set random seed
# "None or no argument seeds from current time or from an operating
#   system specific randomness source if available."
#random.seed()
#random.seed(2)

# sequence of random integers
for i in range(50):
    tmp = random.randrange(0, 100)
    print(tmp, end=", ")
print()



############
# Example 1
############
# first example, simulating coin flipping
def flip_coin ():
    return random.randrange(0, 2)

print (flip_coin ())


# now flip coin for n times. 0 denotes head
def stat_flip_coin (n):
    head_count = 0
    for i in range(n):
        result = flip_coin()
        if (result == 0):
            head_count = head_count + 1

    print("# after tossing coin for ", n, " times. ")
    print("# num. head = ", head_count)
    print("# num. tail = ", n-head_count)        


stat_flip_coin (1000)
print()

# the same as before, except adding the gambling.
def stat_flip_coin_gambling (n):
    head_count = 0
    num_wins = 0
    for i in range(n):
        my_guess = flip_coin()
        result = flip_coin()
        if (result == 0):
            head_count = head_count + 1
        if (result == my_guess):
            num_wins = num_wins + 1

    print("# after tossing coin for ", n, " times. ")
    print("# num. head = ", head_count)
    print("# num. tail = ", n-head_count)
    print("# num. win. from random guess = ", num_wins)            


stat_flip_coin_gambling (1000)
print()


############
# Example 2
############
# similarly, we can simulating a simple version of Powerball
# generate 5 balls out of 50
def generate_5balls ():
    l = set()
    for i in range(5):
        l.add(random.randrange(1, 50))
    return l


print(generate_5balls ())

# simulating Powerball
def simul_powerball ():
    num_trials = 0
    while (1):
        num_trials = num_trials + 1
        
        # guessed 5-balls
        my_guess = generate_5balls()
        
        # true result
        result = generate_5balls()
        if (result == my_guess):
            print("# after buy powerballs for ", num_trials, " times we win")
            print(my_guess)
            print(result)
            break


simul_powerball ()


