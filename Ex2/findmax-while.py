
A = [20, 1, 5, 5, 10, 12, 15, -2, -4, -5, -4, 30]
#lay max = phan tu dau tien
Amax = A[0]
i = 0
j = 1
# chay den cuoi cung cua list vuot thi dung
while j <= len(A):
    if Amax <= A[i]:
        Amax = A[i]
    j += 1
    i += 1
print(Amax)
