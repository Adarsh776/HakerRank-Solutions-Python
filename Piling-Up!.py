Test_Cases=int(input())
for _ in range(Test_Cases):
    n=int(input())
    blocks=list(map(int,input().split()))
    leftmost_element=blocks[0]
    rightmost_element=blocks[-1]
    if leftmost_element<=rightmost_element and rightmost_element==max(blocks):
        print("Yes")
    elif leftmost_element>=rightmost_element and leftmost_element==max(blocks):
        print("Yes")
    else:
        print("No")
