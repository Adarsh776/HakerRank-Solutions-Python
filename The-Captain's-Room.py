from collections import Counter

k = int(input())
room_number_list = list(map(int,input().split()))
freq = sorted(Counter(room_number_list).items(),key = lambda x:(x[1],-x[0]))
print(freq[0][0])
