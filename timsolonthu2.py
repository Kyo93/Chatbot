# tìm số lớn thứ 2 cách 1
find_max2 = lambda a: max(filter(max(a).__ne__, a))
l = [10, 2, 3, 4, 5, -12, -9, 9]
print(find_max2(l))