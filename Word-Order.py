from collections import OrderedDict
dic=OrderedDict()
n=int(input())
l=[]
for _ in range(n):
    s=input()
    if s not in dic:
        dic[s]=1
    else:
        dic[s]+=1
print(len(dic))
for key in dic:
    print(dic[key],end=" ")
