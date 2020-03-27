# tìm số lớn thứ 2
# dùng hàm vô danh:
# lambda tham số: biểu thức
find_max2 = lambda a: max(filter(max(a).__ne__, a))
l = [10, 2, 3, 4, 5, -12, -9, 9]
print(find_max2(l))