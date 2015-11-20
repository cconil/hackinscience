S = 0
for i in range(0, 1000):
    if i % 3 == 0:
        S = S+i
    else:
        if i % 5 == 0:
            S= S+i
print(S)
