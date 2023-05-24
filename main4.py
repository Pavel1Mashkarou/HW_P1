import math
summ = int(input('Введите общее количество журавликов:'))
if summ < 0:
    print('Значение журавликов не может быть меньше нуля')
else:
    if summ == 0:
        print('Ребята не сделали ни одного журавлика. Делить нечего:(')
    else:
        summP = math.trunc(summ / 6)
        summS = math.trunc(summP)
        summK = math.trunc(summ - (summP+summS))
        print(f'Петя собрал {summP} журавликов, Серёжа - {summS}, а Катя - {summK}.')
