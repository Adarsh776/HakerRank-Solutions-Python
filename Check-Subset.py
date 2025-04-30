Test_Cases=int(input())

for _ in range(Test_Cases):
    Size_Of_Set_A = int(input())
    Set_A = set(map(int,input().split()))
    Size_Of_Set_B = int(input())
    Set_B = set(map(int,input().split()))
    print(bool(Set_A<Set_B))
