import os
import db
import notes


if __name__ == "__main__":
    if os.name == "nt":
        hl = "Неправильная команда"
        hp = "Слишком много ошибок"
        flag = True
        inter = db.Data()
        while flag:
            for i in range(3):
                try:
                    print("->Главное меню:\n->\t1) Войти в аккаунт")
                    print("->\t2) Создать аккаунт")
                    print("->\t3) Выход из программы")
                    choice = input("Введите 1, 2 или 3: ")
                    choice = choice[0]
                    if choice == "1":
                        log = input("Введите логин: ")
                        pas = input("Введите пароль: ")
                        if inter.Enter(log, pas) is True:
                            print("Вы вошли в систему")
                            Flag = True
                            ntwork = notes.Notes(inter.log)
                            while Flag:
                                try:
                                    print("->Выберите действие:")
                                    print("->\t1) Работа с заметками")
                                    print("->\t2) Управление аккаунтом")
                                    print("->\t3) Выход из программы")
                                    com = input("Введите 1, 2 или 3: ")
                                    com = com[0]
                                    if com == "1":
                                        try:
                                            print("->Выберете действие:")
                                            print("->\t1) Создать заметку")
                                            print("->\t2) Изменить заметку")
                                            print("->\t3) Удалить заметку")
                                            print("->\t4) Удалить все заметки")
                                            print("->\t5) Список заметок")
                                            print("->\t6) Прочитать заметку")
                                            print("->\t7) Назад")
                                            c = input("Выберете действие: ")
                                            c = c[0]
                                            if c == "1":
                                                print("Название заметки:")
                                                ntname = input()
                                                pep81 = ntwork.Creation(ntname)
                                                if pep81 is True:
                                                    print("Заметка создана")
                                                else:
                                                    pass
                                            elif c == "2":
                                                print("Название заметки:")
                                                ntname1 = input()
                                                ntwork.Editing(ntname1)
                                            elif c == "3":
                                                print("Название заметки:")
                                                ntname2 = input()
                                                ntwork.Deletion(ntname2)
                                            elif c == "4":
                                                for i in range(3):
                                                    c = input("Уверены?(Y/N):")
                                                    choice = c.upper()
                                                    if choice == 'N':
                                                        break
                                                    elif choice == 'Y':
                                                        ntwork.DelAll()
                                                        print('Удалено\n')
                                                        break
                                                    else:
                                                        print(hl)
                                                    if i == 2:
                                                        print(hp)
                                            elif c == "5":
                                                pep82 = ntwork.NotesList()
                                                print("Заметки:", pep82, "\n")
                                            elif c == "6":
                                                print("Название заметки:")
                                                ntname3 = input()
                                                ntwork.NoteReading(ntname3)
                                            elif c == "7":
                                                pass
                                            else:
                                                print("Неправильная команда")
                                                print("Возврат в главное меню")
                                        except IndexError:
                                            print("Неправильная команда\n")
                                    elif com == "2":
                                        try:
                                            print("->Выберите действие:")
                                            print("->\t1) Выйти из аккаунта")
                                            print("->\t2) Удалить аккаунт")
                                            print("->\t3) Изменить шифр-ключ")
                                            print("->\t4) Назад")
                                            cm = input("Введите 1,2,3 или 4: ")
                                            cm = cm[0]
                                            if cm == "1":
                                                for i in range(3):
                                                    c = input("Уверены?(Y/N):")
                                                    cce = c.upper()
                                                    if cce == 'N':
                                                        break
                                                    elif cce == 'Y':
                                                        inter.Exit()
                                                        print("Вход выполнен")
                                                        Flag = False
                                                        break
                                                    else:
                                                        print(hl)
                                                    if i == 2:
                                                        print(hp)
                                            elif cm == "2":
                                                pas1 = input("Введите пароль:")
                                                pep83 = inter.Deletion(pas1)
                                                if pep83 is True:
                                                    Flag = False
                                                else:
                                                    print('Неверный пароль')
                                                    print('Возврат в меню')
                                            elif cm == "3":
                                                for i in range(3):
                                                    c = input("Уверены?(Y/N) ")
                                                    ce = c.upper()
                                                    if ce == 'N':
                                                        break
                                                    elif ce == 'Y':
                                                        inter.ChCiphKey()
                                                        print("Ключ изменён")
                                                        pep84 = inter.nwckey
                                                        ntwork.mrkey = pep84
                                                        break
                                                    else:
                                                        print(hl)
                                                    if i == 2:
                                                        print(hp)
                                            elif cm == "4":
                                                pass
                                            else:
                                                print("Неправильная команда")
                                                print("Возврат в главное меню")
                                        except IndexError:
                                            print("Неправильная команда\n")
                                    elif com == "3":
                                        flag = False
                                        Flag = False
                                    else:
                                        print("Неправильно введена команда")
                                except IndexError:
                                    print("Неправильно введена команда\n")
                        else:
                            print("Неправильно введен логин и/или пароль")
                            print("Возврат в главное меню")
                        break
                    elif choice == "2":
                        inter.Creation()
                        break
                    elif choice == "3":
                        flag = False
                        break
                    elif i == 2:
                        print("Слишком много ошибок. До свидания")
                        flag = False
                    else:
                        print("Неправильно введена команда\n")
                except IndexError:
                    print("Неправильно введена команда\n")
    else:
        print("Данная программа работает только на Windows")
        print("сори нот сори")
