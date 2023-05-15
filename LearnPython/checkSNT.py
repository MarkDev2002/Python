
def check_prime_number(n):
    flag = 1
    if (n < 2):
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    else:
        flag = 1
    return flag


n = int(input("Nhap so tu nhien n : "))


check = check_prime_number(n)

if check == 1:
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")
