# Cryptarithmetic puzzle solver
import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    leftmost = right[0]
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sum(get_value(word, sol) for word in left) == get_value(right, sol) and sol[leftmost] != 0:
            print("Solution:", str(sol), "\nCombination: " + ' + '.join(str(get_value(word, sol)) for word in left),
                  "=", str(get_value(right, sol)))
            break


s_inp = input("Enter the problem in the format of X + Y = Z \n-> ")
print(" ")
solve2(s_inp)
# SHOW + ME + THE = MONEY
# ME + ME = BEE
# SEND + MORE = MONEY
