import math


def isPrimeNumber(n):
    if (n < 2):
        return False

    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True


n = int(input("Nhập số nguyên dương n = "))
dem = 0
i = 2
sb = ""
while (dem < n):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " "
        dem = dem + 1
    i = i + 1
print(n, "Số nguyên tố đầu tiên là : ", sb)
