# 10 Coin Problem
import random  # to generate random stack


# function to flip the halve the stack and flip the first one.
def coin(l):
    l1 = l[0:len(l) // 2]
    new_l1 = []
    l2 = l[len(l) // 2:]
    print('first pile:', str(l1))
    print('second pile:', str(l2))
    if l1.count('H') == l2.count('H'):
        print("They contain same number of heads already,no need to flip")
        print("Number of heads in both:", str(l1.count('H')))
    else:
        for i in l1:
            if i == 'H':
                new_l1.append('T')
            else:
                new_l1.append('H')
        print('flipped fist pile:', str(new_l1))  # printing the flipped pile
        print("Number of Heads in flipped pile:",str(new_l1.count('H')))
        print("Number of Heads in second pile:", str(l2.count('H')))


# function to generate random stack of coins with exactly 5 heads & 5 tails
def random_stack(l):
    i = 0
    cH = 0
    cT = 0
    while i < 10:
        x = int(random.random() * 10)
        if x % 2 == 0:
            if cH < 5:
                l.append('H')
                cH = cH + 1
                i = i + 1
            else:
                pass
        elif x % 2 != 0:
            if cT <= 5:
                l.append('T')
                cT = cT + 1
                i = i + 1
            else:
                pass
        else:
            pass
    return l


l = []
l = random_stack(l)
print('Stack taken:', str(l))

coin(l)
