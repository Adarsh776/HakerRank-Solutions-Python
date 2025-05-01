num_stud_Eng=int(input())
list_of_stud_Eng=set(map(int,input().split()))
num_stud_Fren=int(input())
list_of_stud_Fren=set(map(int,input().split()))

print(len(list_of_stud_Eng | list_of_stud_Fren))
