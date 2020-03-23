A = [20, 1, 5, 5, 10, 12, 15, -2, -4, -5, -4]
Amax2 = A[0]
Amax = A[0]

for x in A:
    if x > Amax:
        Amax2 = Amax
        Amax = x
print(Amax)
print(Amax2)