import db
import notes

if __name__ == "__main__":
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
                    inter.Enter()
                    if inter.entrval == 1:
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
                                            ntwork.Creation()
                                        elif c == "2":
                                            ntwork.Editing()
                                        elif c == "3":
                                            ntwork.Deletion()
                                        elif c == "4":
                                            ntwork.DelAll()
                                        elif c == "5":
                                            ntwork.NotesList()
                                        elif c == "6":
                                            ntwork.NoteReading()
                                        elif c == "7":
                                            pass
                                        else:
                                            print("Неправильная команда.")
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
                                            inter.Exit()
                                            if inter.n == 1:
                                                pass
                                            else:
                                                Flag = False
                                        elif cm == "2":
                                            inter.Deletion()
                                            if inter.n == 1:
                                                Flag = False
                                            else:
                                                pass
                                        elif cm == "3":
                                            inter.ChCiphKey()
                                            if inter.success == 1:
                                                ntwork.mrkey = inter.nwckey
                                            else:
                                                pass
                                        elif cm == "4":
                                            pass
                                        else:
                                            print("Неправильная команда.")
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
                        pass
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
