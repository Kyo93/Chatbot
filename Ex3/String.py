a = "   Đây là một string   "
b = " Đây là string thứ 2"

print(a)
print("Một đoạn của string:", a[0:3])
print("Độ dài của string:", len(a))
print("Xóa khoảng trắng trước và sau string:", a.strip())
print("Đổi thành ko viết hoa:", a.lower())
print("Đổi thành viết hoa:", a.upper())
print("Thay đổi 1 thành phần trong string:", a.replace("l", "v"))
print("Cắt string khi gặp khoảng trắng:", a.split(" "))
print("Check string có trong string ko:", "Đây" in a)
print("Check string không tồn tại trong strin:", "Không" not in a)
print("Ghép 2 string:", a + b)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # Fomart thành kiểu string trước khi insert

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # insert theo thứ tụ

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  # Đánh số thứ tự để insert vào string một cách chính xác

print("Chúng tôi được gọi là \"Người Việt Nam\" ở phương Nam")  # Dùng dấu nháy trong string ==> tương tự các dấu khác
print("Hello\rWorld!")

