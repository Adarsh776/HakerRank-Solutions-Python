from collections import namedtuple
n=int(input())
Student=namedtuple("Student",input().split())
total=0
for _ in range(n):
    student=Student(*input().split())
    total+=int(student.MARKS)
print(total/n)
