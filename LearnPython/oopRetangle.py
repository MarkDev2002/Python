class Retangle:
    def __init__(self, dai=0, rong=0):
        self.dai = dai
        self.rong = rong

    def get_area(self):
        return self.dai * self.rong


a = float(input("Nhap chieu dai : "))
b = float(input("Nhap chieu rong : "))
hcn = Retangle(a, b)
print("Dien tich hinh chu nhat :", hcn.get_area())
