number = int(input('Введите трёхзначное число:'))
if number>999 or number<100:
    print('Вы ввели не трёхзначное число!')
else:
    result1 = number // 100
    result2 = (number - 100*result1)//10
    result3 = number - 100*result1 - 10*result2
    result = result1+result2+result3
    print(f'{result1}+{result2}+{result3} = {result}')