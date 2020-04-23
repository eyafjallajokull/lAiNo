flag = True
while flag:
    list_1 = []
    dict_1 = {}
    key = None
    print('parameters: ')
    with open('conf', 'r') as f:
        for line in f:
            if line[0] != '#' and line[0] != ';' and line[0] != '\n':
                list_1.append(line)
                print(line.split()[0])
    key = input('enter parameter: ').lower()
    for line in list_1:
        line = line.rsplit()
        list_1 = None
        if len(line)>1 and line[1] != ' ':
            list_1 = line[1:]
        dict_1[line[0]] = list_1
    if key in dict_1:
        print(f'parameter - {key} : value - {dict_1[key][0]}')
    else:
        print(f'parameter for {key} not found')
    for i in range(3):
        command = input('continue (y/n): ').lower()
        if command == 'y':
            break
        elif command == 'n':
            flag = False
            break
        else:
            print('wrong command')
        if i == 2:
            print ('too much errors')
            flag = False
