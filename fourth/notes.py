import os
import db
import security
import ast


class Notes:

    def __init__(self, log: str) -> None:
        self.log = log
        self.sec = security.Secur()
        with open("servdata.encode", "r", encoding="UTF-8") as sd:
            servd = dict(ast.literal_eval(sd.read()))
        self.mrkey = servd["Logins and Passwords"][self.log][1]

    def Creation(self) -> None:
        os.chdir(self.log)
        ersymlist = ["\\", "|", "/", "\"", "\'", "<", ">", ":", "*", ";"]
        for i in range(3):
            er = 0
            ntname = input("Введите название заметки: ")
            if ntname[-4:] != ".txt":
                ntname = ntname + ".txt"
            else:
                pass
            for let in ntname[:-4]:
                if let in ersymlist:
                    print("В названии не должны присутствовать символы:")
                    print("\\, |, /, \", \', <, >, ;, :, *")
                    er = 1
                    break
                else:
                    pass
            if er == 0:
                break
            else:
                pass
            if i == 2:
                print("Слишком много ошибок. Возврат в главное меню")
                er = 1
        if er == 0:
            try:
                with open(ntname, "x", encoding="UTF-8") as nt:
                    nt.write(str({"Ciphertext": ""}))
                    print("Вы успешно создали заметку")
            except FileExistsError:
                print("Заметка с таким именем уже существует")
        else:
            pass
        os.chdir("..")

    def Editing(self) -> None:
        os.chdir(self.log)
        er = 0
        miner = 0
        ntname = input("Введите название заметки: ")
        if ntname[-4:] != ".txt":
            ntname = ntname + ".txt"
        else:
            pass
        if os.path.exists(ntname) is True:
            with open(ntname, "r", encoding="UTF-8") as nt:
                try:
                    tx = dict(ast.literal_eval(nt.read()))
                    tx["Ciphertext"][0]
                except SyntaxError:
                    print("Этот файл не был создан в этой программе")
                    er = 1
                except IndexError:
                    miner = 1
            if er == 0:
                if miner == 1:
                    with open(ntname, "w", encoding="UTF-8"):
                        pass
                    os.system(ntname)
                else:
                    with open(ntname, "w", encoding="UTF-8") as nt:
                        dt = self.sec.Decrypt(tx["Ciphertext"], self.mrkey)
                        nt.write(dt.decode(encoding="UTF-8"))
                    os.system(ntname)
                with open(ntname, "r", encoding="UTF-8") as nt:
                    t = nt.read().encode(encoding="UTF-8")
                with open(ntname, "w", encoding="UTF-8") as nt:
                    tx.update({"Ciphertext": self.sec.Encrypt(t, self.mrkey)})
                    nt.write(str(tx))
            else:
                pass
        else:
            print("Такой заметки не существует")
        os.chdir("..")

    def Deletion(self) -> None:
        os.chdir(self.log)
        ntname = input("Введите название заметки: ")
        if ntname[-4:] != '.txt':
            ntname = ntname + '.txt'
        else:
            pass
        if os.path.exists(ntname) is True:
            os.remove(ntname)
            print("Заметка удалена")
        else:
            print("Заметки с таким именем не существует")
        os.chdir("..")

    def DelAll(self) -> None:
        os.chdir(self.log)
        self.n = 0
        for i in range(3):
            choice = input("Вы уверены?(Y/N): ").upper()
            if choice == 'N':
                self.n = 1
                break
            elif choice == 'Y':
                for j in os.listdir("."):
                    os.remove(j)
                print('Заметки удалены\n')
                break
            else:
                print("Неправильно введена команда")
            if i == 2:
                print("Допущено слишком много ошибок")
        os.chdir("..")

    def NotesList(self) -> None:
        os.chdir(self.log)
        print("Ваши заметки: ", os.listdir("."), "\n")
        os.chdir("..")

    def NoteReading(self) -> None:
        er = 0
        os.chdir(self.log)
        miner = 0
        ntname = input("Введите название заметки: ")
        if ntname[-4:] != '.txt':
            ntname = ntname + '.txt'
        else:
            pass
        if os.path.exists(ntname) is True:
            try:
                with open(ntname, "r", encoding="UTF-8") as nt:
                    tx = dict(ast.literal_eval(nt.read()))
                tx["Ciphertext"][0]
            except SyntaxError:
                print("Этот файл не был создан в этой программе")
                er = 1
            except IndexError:
                miner = 1
                td = ""
            if er == 0:
                if miner == 1:
                    pass
                else:
                    dt = self.sec.Decrypt(tx["Ciphertext"], self.mrkey)
                    td = dt.decode(encoding="UTF-8")
                for line in td.split('\n'):
                    print(line)
            else:
                pass
        else:
            print("Заметки с таким именем не существует")
        os.chdir("..")
