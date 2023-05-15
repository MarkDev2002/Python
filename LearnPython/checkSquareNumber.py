
def find_square_number(n):

    flag = 0
    if any(i**2 == n for i in range(n+1)):
        flag = 1
    return flag


n = int(input("nhap mot so tu nhien : "))
check = find_square_number(n)

if check == 1:
    print(n, "la so chinh phuong")
else:
    print(n, "khong phai la so chinh phuong")
