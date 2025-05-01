set_A = set(map(int,input().split()))
number_of_sets = int(input())

for _ in range(number_of_sets):
    other_set = set(map(int,input().split()))
    if not(set_A > other_set):
        output = False
        break
else:
    output = True
print(output)
