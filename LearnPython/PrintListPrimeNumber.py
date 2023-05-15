s = '1,2,3,4,5,6,7'


def ktsnt(n):
    if n < 2:
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n % i == 0):
            return False
    return True


L = s.split(',')
L = [int(i) for i in L if ktsnt(int(i))]
print("Cac so nguyen to :", L)
