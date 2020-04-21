flag = True
while flag:
    dictt = {}
    dataa = []
    key = []
    print('Parameters:')
    with open ('conf','r') as data: 
        for line in data:
            if line[0] != '#' and line[0] != ';' and line[0] != '\n':
                dataa.append(line)
                print(line.split()[0])
    key = input('Enter the required parameter: ')
    for line in dataa:
        line = line.rstrip().split()
        dataa = None
        if len(line) > 1:
            dataa = line[1:]
        dictt[line[0]] = dataa
    if key in dictt:
        print('Your parameter: "', key,'". Its value: "', str(dictt[key]))
    else:
        print("This file does not have this key.")
    for i in range(3):
        command = input('continue (y/n): ').lower()
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
 