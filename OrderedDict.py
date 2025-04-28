from collections import OrderedDict
n=int(input())
dictionary=OrderedDict()
for _ in range(n):
    *name,price=input().split()
    if tuple(name) not in dictionary:
        dictionary[*name]=price
    elif tuple(name) in dictionary:
        dictionary[*name]=int(dictionary[*name])+int(price)

for i in dictionary:
    print(*i,dictionary[i])
