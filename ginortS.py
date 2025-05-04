s=input()
lower, upper, odd, even= [],[],[],[]
for char in s:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)
    elif char.isdigit():
        (even if int(char)%2==0 else odd).append(char)
print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))
