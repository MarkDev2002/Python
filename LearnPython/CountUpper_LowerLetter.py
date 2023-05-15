s = str(input("Nhap chuoi : "))
count_upper = 0
count_lower = 0
for i in s:
    if(i.islower()):
        count_lower += 1
    elif(i.isupper()):
        count_upper += 1

print("So luong chu cai viet hoa la =", count_upper)
print("So luong chu cai viet thuong la =", count_lower)
