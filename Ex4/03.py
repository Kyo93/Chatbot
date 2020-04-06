# Tìm số lớn nhất

class Bai03:
    def __init__(self, list):
        print("Đã khởi tạo xong list")
        print(list)
        self.max = list[0]
        self.list_items = list

    def max_in_list(self):
        for x in self.list_items:
            if x > self.max:
                self.max = x


list = [0, 2, 34, 5656, 778888, 9]
p1 = Bai03(list)
p1.max_in_list()
print("Max của list", p1.max)
