s = input(str("Nhap chuoi : "))
string = s.split()
new = set(string)
print(new)
for i in new:
    t = s.count(i)
    print('Frequency of', i, 'is :', t)
