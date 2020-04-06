# Tính tổng trong 1 list

class A:
    def __init__(self,list):
        print("Đã khởi tạo xong list")
        self.list_item = list
        self.sum_item = 0
    def sum(self):
        print("Tính tổng nhé")
        for x in self.list_item:
            self.sum_item += x
list = [2,5,6,7,5,4,3,6,4,3,2]
p1 = A(list)
p1.sum()
print(p1.sum_item)