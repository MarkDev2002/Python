import math

a = int(input('Nhap vao so a : '))
b = int(input('Nhap vao so b : '))

if a < 0 or b < 0:
    print('Vui long nhap lai!')
elif a > b:
    print('Số thứ nhất phải nhỏ hơn số thứ hai!')
else:
    for n in range(a, b + 1):
        if(n < 2):
            continue
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
