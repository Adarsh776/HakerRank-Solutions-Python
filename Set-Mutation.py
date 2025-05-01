size_set_A = int(input())
set_A = set(map(int, input().split()))
num_other_sets = int(input())

for _ in range(num_other_sets):
    operation_line = input().split()
    operation = operation_line[0]
    other_set = set(map(int, input().split()))
    
    getattr(set_A, operation)(other_set)

print(sum(set_A))
