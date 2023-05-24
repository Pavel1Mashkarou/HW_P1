TicketNumber = input('Введите номер билета:')
if len(TicketNumber)<6 or len(TicketNumber)>6:
    print('Билет не шестизначный.')
else:
   print('Good')
