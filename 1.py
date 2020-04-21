flag = True
while flag:
 val_1 = int(input('input first number: '))
 val_2 = int(input('input second number: '))
 command = input('input operation: ')
 if command == '+':
     print(val_1 + val_2)
 elif command == '-':
     print(val_1 - val_2)
 elif command == '*':
     print(val_1 * val_2)
 elif command == '/':
     print(val_1 / val_2)
 else:
     print('wrong command!')
 for i in range(3):
    command = input('continue (y/n): ')
    if command == 'y':
        break
    elif command == 'n':
        flag = False
        break
    else:
        print('wrong command!')
    if i == 2:
        print ('too much errors!')
        flag = False
        break
