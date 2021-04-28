import sys
# NOTE: THIS ONLY WORKS WHEN THERE IS NO LEFT RECURSION OR LEFT FACTORING IN THE GRAMMAR
sys.setrecursionlimit(60)


def first(string):
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ | first_2

    elif string in terminals:
        first_ = {string}

    elif string == '' or string == '@':
        first_ = {'@'}

    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                # print("inside while")

                first_ = first_ | (first_2 - {'@'})
                # print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2
    return first_


def follow(nT):
    follow_ = set()
    prods = productions_dict.items()
    if nT == starting_symbol:
        follow_ = follow_ | {'$'}
    for nt, rhs in prods:
        for alt in rhs:
            for char in alt:
                if char == nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str == '':
                        if nt == nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2 - {'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    return follow_


def production_seperator(productions):
    new_prd = []
    for production in productions:
        x = production[0]
        production_ = production.split('->')[1]
        if '|' in production_:
            temp_l = list(production_.split('|'))
            for i in temp_l:
                new_prd.append(x + "->" + i)
        else:
            new_prd.append(production)
    return new_prd


def generate_table(terminals, nonterminals, productions, first, follow):
    table = {}
    terminals.append('$')
    for row in nonterminals:
        table[row] = {}
        for coloumn in terminals:
            table[row][coloumn] = {}
    productions_ = production_seperator(productions)
    for production in productions_:
        row = production.split('->')[0]
        if '@' in production:
            plot = list(follow[row])
        else:
            plot = list(first[row])
        if '@' in plot:
            plot.remove('@')
        for coloumn in plot:
            table[row][coloumn] = production

    print_table(table)


def print_table(table):
    print('{: ^10}'.format(' '), end='')
    for i in terminals:
        print('{: ^10}'.format(i), end='')
    print()
    for row in table.keys():
        print('{: ^10}'.format(row), end='')
        for column in table[row].keys():
            print('{: ^10}'.format(str(table[row][column])), end='')
        print()


terminals = list(input('Enter the terminals : ').split())
non_terminals = list(input('Enter the non terminals : ').split())
starting_symbol = input("Enter the starting symbol: ")
no_of_productions = int(input("Enter no of productions: "))
productions = []
print('Enter the productions:')
for _ in range(no_of_productions):
    productions.append(input())
productions_dict = {}
for nT in non_terminals:
    productions_dict[nT] = []
for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()
for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)
    if FOLLOW[non_terminal] == set():
        FOLLOW[non_terminal] = None

print('{: ^20}{: ^20}{: ^20}'.format('Non Terminals', 'First', 'Follow'))
for non_terminal in non_terminals:
    print('{: ^20}{: ^20}{: ^20}'.format(non_terminal, str(FIRST[non_terminal]), str(FOLLOW[non_terminal])))
for i in range(100):
    print('=', end='')
print()
print('{: ^100}'.format('LL1 Parsing table'))
for i in range(100):
    print('=', end='')
print()
generate_table(terminals, non_terminals, productions, FIRST, FOLLOW)


'''

Enter the terminals : a b e r = ( ) + ;
Enter the non terminals : A E F P R S T
Enter the starting symbol: S
Enter no of productions: 7
Enter the productions:
S->AR
P->bSe
R->AR|@
A->a=E;
E->FT
T->+FT|@
F->(E)|a|r
   Non Terminals           First               Follow       
         A                 {'a'}          {'$', 'e', 'a'}   
         E            {'(', 'r', 'a'}        {')', ';'}     
         F            {'(', 'r', 'a'}     {')', '+', ';'}   
         P                 {'b'}                None        
         R               {'@', 'a'}          {'$', 'e'}     
         S                 {'a'}             {'$', 'e'}     
         T               {'+', '@'}          {')', ';'}     
====================================================================================================
                                         LL1 Parsing table                                          
====================================================================================================
              a         b         e         r         =         (         )         +         ;         $     
    A      A->a=E;      {}        {}        {}        {}        {}        {}        {}        {}        {}    
    E       E->FT       {}        {}      E->FT       {}      E->FT       {}        {}        {}        {}    
    F        F->r       {}        {}       F->r       {}       F->r       {}        {}        {}        {}    
    P         {}      P->bSe      {}        {}        {}        {}        {}        {}        {}        {}    
    R       R->AR       {}       R->@       {}        {}        {}        {}        {}        {}       R->@   
    S       S->AR       {}        {}        {}        {}        {}        {}        {}        {}        {}    
    T         {}        {}        {}        {}        {}        {}       T->@     T->+FT     T->@       {} 

'''
