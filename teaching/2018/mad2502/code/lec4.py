"""algorithms discussed on Lecture 4

"""

### Chap 3.3. approximating the square root or algorithm for solving x^2 = a

# simpler if a is a perfect square (a nonnegative)
inputstr = input('Enter an integer: ')
a = int(inputstr)
a = abs(a)
x = 0
# try all k such that x^2 < a
while (x**2 < abs(a)):
    x = x + 1
if (x**2 == a):
    if (a < 0):
        a = -a
        x = -x
    print ('square root of ', a, 'is', x)
else:
    print ('a is not a perfect square')    


# harder if a is a not perfect square (still try all approximated values)
inputstr = input('Enter an integer: ')
a = float(inputstr)
a = abs(a)
allowed_error = 0.01
increase = 0.0001
current_guess = 0
num_steps = 0
while abs(current_guess**2 - a) > allowed_error:
    current_guess = current_guess + increase
    #print(x)
    num_steps = num_steps + 1
print ('# after ', num_steps, " guesses we get square root of ", a, "is approximated", current_guess)

