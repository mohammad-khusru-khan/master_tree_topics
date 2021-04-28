'''
def cc(l):
    count = 0
    for i in l:
        if l.count(i) > 1:
            count = count + 1
            l = [j for j in l if j != i]
            print(l)
    return count


l = ["the","higher","you","climb","the","further","you","fall"]
print(cc(l))
'''

'''
def sublist(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in range(len(l1)-1):
        if abs((l1[i]-l1[i+1])) > 1:
            return False
    return True


print(sublist([2,2,4],[2,2,3,4,5]))
'''
'''
def perfect(n):
    if n == 1:
        return True
    if n == 6:
        return True
    if n < 6:
        return False
    else:
        s = 0
        for i in range(1,n):
            if n % i == 0:
                s = s + i
        if s == n:
            return True
        else:
            return False


print(perfect(60))
'''