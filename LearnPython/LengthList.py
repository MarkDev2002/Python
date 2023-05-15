def chieudaiChuoi(str1):
    count = 0
    for char in str1:
        count += 1
    return count


s = input(str("Nhap chuoi : "))
print("Chieu dai chuoi : {} ".format(chieudaiChuoi(s)))
print("Check len() function : ", len(s))
