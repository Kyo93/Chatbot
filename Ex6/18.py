# các cách reverse tuple

x = "thiệp đẹp trai"
y = reversed(x)
print(tuple(y))
x = (2, 4, 5.6, "thiep")
y = reversed(x)
print(tuple(y))
y = x[:: -1]
print(y)