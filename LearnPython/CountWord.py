s = str(input("Nhap chuoi : "))
counting = {}
for i in s:
    if i in counting:
        counting[i] += 1
    else:
        counting[i] = 1

for k in s:
    if k.isalpha():
        print(k, counting[k])
