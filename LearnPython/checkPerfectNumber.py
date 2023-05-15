def kiemtraHoanHao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False


n = int(input('Nhap vao so nguyen n lon hon 0: '))
if kiemtraHoanHao(n):
    print(n, 'la so hoan hao')
else:
    print(n, 'khong la so hoan hao')
