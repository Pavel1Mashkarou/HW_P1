TicketNumber = input('Введите номер билета:')
if len(TicketNumber)<6 or len(TicketNumber)>6:
    print('Билет не шестизначный.')
else:
   i = 0
   NumberSumm1 = 0
   while i<=2:
       NumberSumm1 += int(TicketNumber[i])
       i=i+1
   print(f'Сумма первых трёх цифр - {NumberSumm1}')
   i = 3
   NumberSumm2 = 0
   while i<=len(TicketNumber)-1:
       NumberSumm2 += int(TicketNumber[i])
       i=i+1
   print(f'Сумма последних трёх цифр - {NumberSumm2}')
   if NumberSumm1 == NumberSumm2:
       print(f'{NumberSumm1}={NumberSumm2}')
       print('Ваш билет счастливый!')
   else:
       print(f'{NumberSumm1}!={NumberSumm2}')
       print('Ваш билет не оказался счастливым:(')