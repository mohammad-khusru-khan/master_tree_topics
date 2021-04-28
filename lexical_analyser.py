import re

keywords = []
operators = []
delimiters = []
identifiers = []


def Delimiter(ch):
    if ch == ' ' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ',' or ch == ';' or ch == '>' or ch == '<' or ch == '=' or ch == '(' or ch == ')' or ch == '[' or ch == ']' or ch == '{' or ch == '}':
        return True
    return False


def Operator(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '>' or ch == '<' or ch == '=' or ch == '&&' or ch == '||':
        return True
    return False


def validIdentifier(stry):
    if stry[0] == '0' or stry[0] == '1' or stry[0] == '2' or stry[0] == '3' or stry[0] == '4' or stry[0] == '5' or stry[
        0] == '6' or stry[0] == '7' or stry[0] == '8' or stry[0] == '9' or Delimiter(stry[0]) == True:
        return False
    return True


def Keyword(stry):
    if stry == "if" or stry == "main" or stry == "printf" or stry == "stdio.h" or stry == "#include" or stry == "else" or stry == "while" or stry == "do" or stry == "break" or stry == "continue" or stry == "int" or stry == "double" or stry == "float" or stry == "return" or stry == "char" or stry == "case" or stry == "char" or stry == "sizeof" or stry == "long" or stry == "short" or stry == "typedef" or stry == "switch" or stry == "unsigned" or stry == "void" or stry == "static" or stry == "struct" or stry == "goto":
        return True
    return False


def subString(stry, left, right):
    subStr = []
    for i in range(left, right):
        subStr.append(stry[i])
    return subStr


def parse(stry):
    left = 0
    right = 0
    leny = len(stry)
    while leny > right >= left:
        if not Delimiter(stry[right]):
            right += 1

        if Delimiter(stry[right]) and left == right:
            if Operator(stry[right]):
                operators.append(stry[right])
            else:
                delimiters.append(stry[right])
            right += 1
            left = right

        elif Delimiter(stry[right]) and left != right or (right == leny and left != right):
            subStr = subString(stry, left, right)
            subStr = ''.join(subStr)

            if Keyword(subStr):
                keywords.append(subStr)

            elif validIdentifier(subStr) and not Delimiter(stry[right - 1]):
                identifiers.append(subStr)
            left = right;
    return


f = open('input.c', 'r')

i = f.read()

count = 0
program = i.split('\n')

for j in program:
    parse(j)
print("Keywords: {}".format(len(keywords)))
for i in keywords:
    print(i)
print("---------------------------")
print("Operators: {}".format(len(operators)))
for i in operators:
    print(i)
print("---------------------------")
while " " in delimiters:
    delimiters.remove(" ")
print("Delimiters: {}".format(len(delimiters)))
for i in delimiters:
    print(i)
print("---------------------------")
print("Identifiers: {}".format(len(identifiers)))
for i in identifiers:
    print(i)
print("---------------------------")
