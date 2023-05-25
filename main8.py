m = int(input('Введите m долек шоколада:'))
n = int(input('Введите n долек шоколада:'))
k = int(input('Введите k долек шоколада:'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes')
else:
    print('No')