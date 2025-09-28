# еще один цикл while loop 
# i = 0 
# while i < 5: # когда возвращает правду - работает, пока не возвратит ложь 
#    print('hello')
#    i += 1
# else:
#    print('the end')

# while True: # постоянный цикл (прикольная постоянная программа, которая постоянно отслеживает ввод)
#    user_unput = input('''Сколько лет бокса у Димы? 
#                       для выхода - Выход''')
#    user_unput = user_unput.lower()
#    if user_unput == 'выход':
#       user_unput.ex
#    elif user_unput != int:
#       print('только целые числа')
#    elif(int(user_unput)) == 0:
#       print('Правильно, это всем известно')
#    else:
#       print('Ты че, не может быть столько, это же Дима')


while True: # постоянный цикл (прикольная постоянная программа, которая постоянно отслеживает ввод)
   user_input = input('Сколько лет бокса у Димы? ')
   user_input = user_input.lower()
   if user_input == 'выход':
      break
   elif(int(user_input)) == 0:
      print('Правильно, это всем известно')
   else:
      print('Ты че, не может быть столько, это же Дима')


