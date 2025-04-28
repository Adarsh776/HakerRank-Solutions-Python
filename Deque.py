from collections import deque

d=deque()
n=int(input())

for _ in range(n):
    method,*value=input().split()
    if method=="append":
        d.append(int(*value))
    elif method=="appendleft":
        d.appendleft(int(*value))
    elif method=="pop":
        d.pop()
    elif method=="popleft":
        d.popleft()
print(*d)
