# converse các tuple thành dic

# tạo một list các tuple
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# tạo dic rỗng
d = {}
# chuyển tuple thành dic
for a, b in l:
    d.setdefault(a, []).append(b)
print(d)
