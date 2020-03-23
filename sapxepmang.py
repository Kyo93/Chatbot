import random as ra

A = list(range(25))
ra.shuffle(A)
print("Mang da tao: ", A)
for i in range(25):
    for j in range(25):
        if A[i] < A[j]:#???????
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
        j += 1
    i += 1
print("Done")
print("Mang da sap xep la: ", A)