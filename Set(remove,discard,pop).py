n = int(input())
s = set(map(int, input().split()))
number_of_commands = int(input())
for _ in range(number_of_commands):
    command,*val=input().split()
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(*val))
    elif command == "discard":
        s.discard(int(*val))
print(sum(s))
