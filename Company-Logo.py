from collections import Counter


if __name__ == '__main__':
    s = input()

frequency = Counter(s).items()
sorted_freq = sorted(frequency,key=lambda x:(-x[1],x[0]))

for item in sorted_freq[:3]:
    print(item[0],item[1])
