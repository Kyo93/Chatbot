A = [20, 1, 5, 5, 10, 12, 15, -2, -4, -5, -4]
Amax = A[0]
for x in A:
    if x > Amax:
        Amax = x
#print("Max là:",Amax)
A.remove(Amax)
Amax2 = A[0]
for y in A:
    if y > Amax2:
        Amax2 = y
print("Max là:", Amax)
print("Max2nd là:", Amax2)
