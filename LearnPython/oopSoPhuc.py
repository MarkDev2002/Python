
class MyComplexNumber():
    def __init__(self, thuc=0, ao=0):
        self.thuc = thuc
        self.ao = ao

    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"

    def input(self):
        self.thuc = int(input("Nhap so thuc : "))
        self.ao = int(input("Nhap so ao : "))

    def addition(self, other):
        self.thuc += other.thuc
        self.ao += other.ao

    def subtract(self, other):
        self.thuc -= other.thuc
        self.ao -= other.ao

    def multiply(self, other):
        self.thuc = (self.thuc * other.thuc - self.ao * other.ao)
        self.ao = (self.thuc * other.ao + self.ao * other.thuc)

    def division(self, other):
        self.thuc = (self.thuc * other.thuc + self.ao *
                     other.ao) / (other.thuc ** 2 + other.ao ** 2)
        self.thuc = (self.thuc * other.thuc - self.ao *
                     other.ao) / (other.thuc ** 2 + other.ao ** 2)

    def __add__(self, other):
        self.addition(other)

    def __sub__(self, other):
        self.subtract(other)

    def __mul__(self, other):
        self.multiply(other)

    def __div__(self, other):
        self.division(other)

    def getDoLon(self):
        return (self.thuc ** 2 + self.ao ** 2) ** 0.5

    def compare(self, other):
        if self.getDoLon() == other.getDoLon():
            return 0
        elif self.getDoLon() > other.getDoLon():
            return 1
        else:
            return -1

    def __eq__(self, other):
        return self.getDoLon() == other.getDoLon

    def __gt__(self, other):
        return self.getDoLon() > other.getDoLon

    def __lt__(self, other):
        return self.getDoLon() < other.getDoLon


i = MyComplexNumber()
j = MyComplexNumber()
i.input()
j.input()
print("So thuc thu nhat : ", i)
print("So thuc thu hai : ", j)
i.addition(j)
print("Cong 2 so thuc = ", i)


