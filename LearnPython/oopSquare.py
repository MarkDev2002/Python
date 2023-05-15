class Shape:
    def __init__(self):
        pass
    @staticmethod
    def get_area(x):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length = length
    @staticmethod
    def get_area(x):
        return x*x
length = float(input("Nhap chieu dai : "))
hv = Square(length)
print("Dien tich Square :",hv.get_area(length))