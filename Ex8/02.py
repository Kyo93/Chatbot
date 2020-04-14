def binary(decimal):
    otherBase = ""
    while decimal != 0:
        otherBase = str(decimal % 2) + otherBase
        decimal = int(decimal / 2)
    return otherBase


print(binary(-5454542))

binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)
