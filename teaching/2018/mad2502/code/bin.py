import random

# this is the previous lecture for birthday paradox
def random_birthday ():
    return random.randrange(0, 366)


def run_game_once ():
    all_birthdays = []
    numbers = 0
    comparisons = 0
    while (1):
        curr = random_birthday()
        numbers = numbers + 1
        for i in range(len(all_birthdays)):
            comparisons = comparisons + 1
            if (curr==all_birthdays[i]):
                #print("# found match after generating ", numbers, "; number of comparison ", comparisons)
                return numbers, comparisons
        all_birthdays.append(curr)
            
run_game_once ()


# run the above game for many times
# and compute the average number for matching
def run_game_many (n):
    tot_num = 0
    tot_comp = 0
    for i in range(n):
        num, comp = run_game_once ()
        tot_num = tot_num + num
        tot_comp = tot_comp + comp
    ave_num = tot_num / n
    ave_comp = tot_comp / n
    print ("# after run the game for", n, "times; ave. num. = ", ave_num, "ave. comp. = ", ave_comp)


# theoretical value should be about 24.617
#run_game_many (40000)



def random_list (n):
    L = []
    for i in range(n):
        L.append(random.randrange(0, 366))
    return L

L = random_list (20)
print("# before sort", L)
L.sort()
print("# after sort", L)


# assume the list is sorted, then one can use the binary search
def bin_search (L, x):
    l = 0
    r = len(L) - 1
    num = 0
    while (True):
        num = num + 1
        if r < l:
            return -1, num
        m = (l + r) // 2
        if L[m] < x:
            l = m + 1
        elif L[m] > x:
            r = m - 1
        else:
            return m, num


x = L[10]
print(bin_search(L, x))

x = L[0]
print(bin_search(L, x))

x = 1
print(bin_search(L, x))







        
