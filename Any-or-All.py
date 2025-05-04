nums_count = int(input())
nums=list(map(int,input().split()))

if all(map(lambda x:x>=0,nums)):
    if any(map(lambda x:str(x)==str(x)[::-1],nums)):
        print(True)
    else:
        print(False)
else:
    print(False)
