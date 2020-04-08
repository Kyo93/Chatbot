# tạo tuple
tuple01 = (2, 3, 4, 5, 6, 7)
print(tuple01)
# tuple không thể sửa xóa trực tiếp các phần tử
# dùng phép cộng để thêm phần tử vào tuple
tuple02 = tuple01 + (8, 9,)
print(tuple02)
# thêm phần tử vào một vị trí xác định
tuple03 = tuple01[:5] + (15, 20, 25) + tuple01[:5]
print(tuple03)
# convert tuple sang list
list = list(tuple01)
list.append(30)
tuple04 = tuple(list)
print(tuple04)
