from abc import ABC, abstractmethod, abstractclassmethod
import random, json

class Papa(ABC):

    def ALPH(self):
        try:
            self._er = 0
            wa = input('\nВведите полный путь к файлу алфавита\n(файл должен быть в формате json и иметь расширение .alph,\nалфавит должен находится в ключе "alph"): ')
            with open(wa, 'r', encoding = "UTF-8") as alp:
                if wa[-5:] != ".alph":
                    raise OSError()
                else:
                    pass
                alph = json.load(alp)
            if "alph" in alph:
                if type(alph["alph"]) is list:
                    for letter in alph["alph"]:
                        if len(letter) == 1:
                            pass
                        else:
                            print(f'Длина символа "{letter}" не равна одного\n')
                            raise Exception()
                    alph = [let.lower() for let in alph["alph"]]
                    alph = set(alph)
                    self._alph = list(alph)
                else:
                    print("Неверный формат: значение ключа 'alph' не является списком\n")
                    self._er = 1
            else:
                print("Неверный формат: в данном словаре нет ключа 'alph'\n")
                self._er = 1
        except json.decoder.JSONDecodeError:
            print("Данный файл находится не в формате json\n")
            self._er = 1
        except FileNotFoundError:
            print("Такого файла не существует\n")
            self._er = 1
        except OSError:
            print('Расширение данного файла не ".alph"\n')
            self._er = 1
        except Exception:
            self._er = 1

    def KEY(self, x, enkey):
        self._er = 0
        if x == "r":
            try:
                wk = input("\nВведите полный путь к файлу ключа (файл должен иметь расширение .key): ")
                with open(wk, 'r', encoding = "UTF-8") as key:
                    if wk[-4:] != ".key":
                        raise OSError()
                    else:
                        pass
                    self._enlist = json.load(key)
            except FileNotFoundError:
                print("Такого файла не существует\n")
                self._er = 1
            except json.decoder.JSONDecodeError:
                print("Данный файл находится не в формате json")
                self._er = 1
            except OSError:
                print('Расширение данного файла не ".key"')
                self._er = 1
        else:
            flag = True
            while flag:
                try:
                    wk = input("\nВведите полный путь к месту создания файла ключа (файл должен иметь расширение .key): ")
                    if wk[-4:] != ".key":
                        raise OSError()
                    else:
                        pass
                    with open(wk, 'w', encoding = "UTF-8") as key:
                        json.dump(enkey, key, ensure_ascii=False)
                        print("Ключ успешно сгенерирован\n")
                        flag = False
                except OSError:
                    print('Расширение данного файла не ".key"\nВведите корректное название')

    def TXT(self, x, dtext):
        self._er = 0
        if x == "r":
            try:
                wt = input("\nВведите полный путь к файлу открытого текста (файл должен иметь расширение .txt): ")
                with open(wt, 'r', encoding = "UTF-8") as tx:
                    if wt[-4:] != ".txt":
                        raise OSError()
                    else:
                        pass
                    self._txt = tx.read()
            except FileNotFoundError:
                print("Такого файла не существует")
                self._er = 1
            except OSError:
                print('Расширение данного файла не ".txt"')
                self._er = 1
        else:
            flag = True
            while flag:
                try:
                    wd = input("\nВведите полный путь к месту создания файла расшифрованного текста (файл должен иметь расширение .txt): ")
                    if wd[-4:] != ".txt":
                        raise OSError()
                    else:
                        pass
                    with open(wd, 'w', encoding = "UTF-8") as dtx:
                        dtx.write(dtext)
                        print("Зашифрованный текст успешно расшифрован\n")
                        flag = False
                except OSError:
                    print('Расширение данного файла не ".txt"\nВведите корректное название')

    def ENCODE(self, x, defdict):
        self._er = 0
        if x == "r":
            try:
                we = input("\nВведите полный путь к файлу шифртекста (файл должен иметь расширение .encode): ")
                with open(we, 'r', encoding = "UTF-8") as etx:
                    if we[-7:] != ".encode":
                        raise OSError()
                    else:
                        pass
                    self._etxt = json.load(etx)
            except FileNotFoundError:
                print("Такого файла не существует\n")
                self._er = 1
            except OSError:
                print('Расширение данного файла не ".encode"')
                self._er = 1
            except json.decoder.JSONDecodeError:
                print("Данный файл находится не в формате json\n")
                self._er = 1
        else:
            flag = True
            while flag:
                try:
                    we = input("\nВведите полный путь к месту создания файла шифртекста (файл должен иметь расширение .encode): ")
                    if we[-7:] != ".encode":
                        raise OSError()
                    else:
                        pass
                    with open(we, 'w', encoding = "UTF-8") as etx:
                        json.dump(defdict, etx, ensure_ascii=False)
                        print("Открытый текст успешно зашифрован\n")
                        flag = False
                except OSError:
                    print('Расширение данного файла не ".encode"\nВведите корректное название')

class Replacement(Papa):

    def GenKey(self):
        self.ALPH()
        if self._er == 0:
            enkey = self._alph.copy()
            random.shuffle(enkey)
            alphasc = [ord(letter) for letter in self._alph]
            kuyasc = [ord(letter) for letter in enkey]
            enkey = {"Cipher method" : "Replacement", "Alphabet ASCII": alphasc, "Key ASCII": kuyasc}
            self.KEY("", enkey)
        else:
            print("Возврат в Главное меню\n")

    def Encryption(self):
        self.TXT("r", "")
        if self._er == 0:
            self.KEY("r", "")
            if self._er == 0:
                if self._enlist["Cipher method"] == "Replacement":
                    self._txt = self._txt.lower()
                    alphlist = [chr(let) for let in self._enlist["Alphabet ASCII"]]
                    alphlist.append("\n")
                    minier = 0
                    for letter in self._txt:
                        if letter in alphlist:
                            pass
                        else:
                            print(f'\nСимвол "{letter}" данного открытого текста отсутствует в данном алфавите\nШифрование может работать некорректно')
                            minier = 1
                    if minier == 1:
                        flag = True
                        while flag:
                            for i in range(3):
                                command = input("Желаете продолжить?(Y/N) ").upper()
                                if command == 'Y':
                                    flag = False
                                    break
                                elif command == 'N':
                                    flag = False
                                    self._er = 1
                                    break
                                else:
                                    print("Неправильно введена комманда\n")
                                if i == 2:
                                    print("Слишком много ошибок. До свидания")
                                    flag = False
                                    self._er = 1
                    else:
                        pass
                    if self._er == 0:
                        kdict = {letter: enletter for letter, enletter in zip(self._enlist["Alphabet ASCII"], self._enlist["Key ASCII"])}
                        defdict = {"Cipher method" : "Replacement", "Ciphertext" : self._txt.translate(kdict)}
                        self.ENCODE("", defdict)
                    else:
                        print("Возврат в Главное меню\n")
                else:
                    print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
            else:
                print("Возврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

    def Decryption(self):
        self.ENCODE("r", "")
        if self._er == 0:
            if self._etxt["Cipher method"] == "Replacement":
                self.KEY("r", "")
                if self._er == 0:
                    if self._enlist["Cipher method"] == "Replacement":
                        dkdict = {enletter: letter for letter, enletter in zip(self._enlist["Alphabet ASCII"], self._enlist["Key ASCII"])}
                        dtext = self._etxt["Ciphertext"].translate(dkdict)
                        self.TXT("", dtext)
                    else:
                        print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
                else:
                    print("Возврат в Главное меню\n")
            else:
                print("Данный шифртекст зашифрован не методом замены\nВозврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

class Transposition(Papa):

    def GenKey(self):
        flag = True
        while flag:
            try:    
                siz = int(input("Введите размер блока перестановки: "))
                if siz <= 0:
                    print("\nВы ввели не положительное число")
                elif siz == 1:
                    print("\nРазмер блока перестановки не может быть равен 1-му")
                else:
                    flag = False
            except ValueError:
                print("\nВы ввели не целое число")
        enkey = [i for i in range(siz)]
        random.shuffle(enkey)
        enkey = {"Cipher method" : "Transposition", "Key": enkey}
        self.KEY("", enkey)

    def Encryption(self):
        self.TXT("r", "")
        if self._er == 0:
            self.KEY("r", "")
            if self._er == 0:
                if self._enlist["Cipher method"] == "Transposition":
                    if len(self._enlist["Key"]) > len(self._txt):
                        txt = self._txt.ljust(len(self._enlist["Key"]), self._txt[random.randint(0, len(self._txt))])
                        n = len(self._enlist["Key"])
                    elif len(self._txt) % len(self._enlist["Key"]) != 0:
                        n = len(self._enlist["Key"]) - len(self._txt) % len(self._enlist["Key"]) + len(self._txt)
                        txt = self._txt.ljust(n, self._txt[random.randint(0, len(self._txt))])
                    else:
                        txt = self._txt
                        n = len(txt)
                    text = list(txt)
                    for i in range(0, len(text), len(self._enlist["Key"])):
                        string = [text[i+j] for j in range(len(self._enlist["Key"]))]
                        for j in range(len(self._enlist["Key"])):
                            text[i + j] = string[self._enlist["Key"][j]]
                    defdict = {"Cipher method" : "Transposition", "Ciphertext" : "".join(text), "Difference": n - len(self._txt)}
                    self.ENCODE("", defdict)
                else:
                    print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
            else:
                print("Возврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

    def Decryption(self):
        self.ENCODE("r", "")
        if self._er == 0:
            if self._etxt["Cipher method"] == "Transposition":
                self.KEY("r", "")
                if self._er == 0:
                    if self._enlist["Cipher method"] == "Transposition":
                        etxt = list(self._etxt["Ciphertext"])
                        for i in range(0, len(etxt), len(self._enlist["Key"])):
                            string = [etxt[i+j] for j in range(len(self._enlist["Key"]))]
                            for j in range(len(self._enlist["Key"])):
                                etxt[i + self._enlist["Key"][j]] = string[j]
                        dtext = "".join(etxt)
                        if self._etxt["Difference"] <= 0:
                            pass
                        else:
                            dtext = dtext[ : - self._etxt["Difference"]]
                        self.TXT("", dtext)
                    else:
                        print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
                else:
                    print("Возврат в Главное меню\n")
            else:
                print("Данный шифртекст зашифрован не методом перестановки\nВозврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

class Gamming(Papa):

    def GenKey(self):
        self.ALPH()
        if self._er == 0:    
            flag = True
            while flag:
                try:    
                    siz = int(input("Введите размер гаммы: "))
                    if siz <= 0:
                        print("\nВы ввели не положительное число")
                    else:
                        flag = False
                except ValueError:
                    print("\nВы ввели не целое число")
            enkey = [random.randint(0, len(self._alph)) for i in range(siz)]
            if "\n" in self._alph:
                pass
            else:
                self._alph.append("\n")
            hdict = {"Cipher method" : "Gamming", "Gamma": enkey, "Alphabet": self._alph}
            self.KEY("", hdict)
        else:
            print("Возврат в Главное меню\n")

    def Encryption(self):
        self.TXT("r", "")
        if self._er == 0:
            self.KEY("r", "")
            if self._er == 0:
                if self._enlist["Cipher method"] == "Gamming":
                    txt = self._txt.lower()
                    for letter in txt:
                        if letter in self._enlist["Alphabet"]:
                            pass
                        else:
                            print(f'\nСимвол "{letter}" данного открытого текста отсутствует в данном алфавите')
                            self._er = 1
                    if self._er == 0:
                        if len(self._enlist["Gamma"]) > len(self._txt):
                            txt = txt.ljust(len(self._enlist["Gamma"]), random.choice(self._enlist["Alphabet"]))
                            n = len(self._enlist["Gamma"])
                        elif len(self._txt) % len(self._enlist["Gamma"]) != 0:
                            n = len(self._enlist["Gamma"]) - len(self._txt) % len(self._enlist["Gamma"]) + len(self._txt)
                            txt = txt.ljust(n, random.choice(self._enlist["Alphabet"]))
                        else:
                            n = len(txt)
                        text = list(txt)
                        kdict = {self._enlist["Alphabet"][i]: i for i in range(len(self._enlist["Alphabet"]))}
                        revkdict = {key: value for value, key in kdict.items()}
                        for i in range(0, len(text), len(self._enlist["Gamma"])):
                            string = [(kdict[text[i + j]] + self._enlist["Gamma"][j]) % len(self._enlist["Alphabet"]) for j in range(len(self._enlist["Gamma"]))]
                            for j in range(len(self._enlist["Gamma"])):
                                text[i + j] = revkdict[string[j]]
                        defdict = {"Cipher method" : "Gamming", "Ciphertext" : "".join(text), "Difference": n - len(self._txt)}
                        print(defdict)
                        self.ENCODE("", defdict)
                    else:
                        print("Пожалуйста, создайте ключ с помощью более полного алфавита")
                        print("Возврат в Главное меню\n")
                else:
                    print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
            else:
                print("Возврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

    def Decryption(self):
        self.ENCODE("r", "")
        if self._er == 0:
            if self._etxt["Cipher method"] == "Gamming":
                self.KEY("r", "")
                if self._er == 0:
                    if self._enlist["Cipher method"] == "Gamming":
                        etxt = list(self._etxt["Ciphertext"])
                        kdict = {self._enlist["Alphabet"][i]: i for i in range(len(self._enlist["Alphabet"]))}
                        revkdict = {key: value  for value, key in kdict.items()}
                        for i in range(0, len(etxt), len(self._enlist["Gamma"])):
                            string = [(kdict[etxt[i + j]] - self._enlist["Gamma"][j]) % len(self._enlist["Alphabet"]) for j in range(len(self._enlist["Gamma"]))]
                            for j in range(len(self._enlist["Gamma"])):
                                etxt[i + j] = revkdict[string[j]]
                        dtext = "".join(etxt)
                        if self._etxt["Difference"] <= 0:
                            pass
                        else:
                            dtext = dtext[ : - self._etxt["Difference"]]
                        self.TXT("", dtext)
                    else:
                        print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
                else:
                    print("Возврат в Главное меню\n")
            else:
                print("Данный шифртекст зашифрован не методом перестановки\nВозврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

flag = True
while flag:
    try:
        for i in range(3):
            try:
                r = Replacement()
                t = Transposition()
                g = Gamming()
                print("->Главное меню:\n->\t1) Зашифровать\n->\t2) Расшифровать\n->\t3) Сгенерировать ключ\n->\t4) Выход из программы\n")
                choice = input("Введите 1, 2, 3 или 4: ")
                choice = choice[0]
                if choice == "1":
                    print("->Выберите метод шифрования:\n->\t1) Замена\n->\t2) Перестановка\n->\t3) Гаммирование\n->\t4) Вернуться в главное меню\n")
                    n = input("Введите 1, 2, 3 или 4: ")
                    n = n[0]
                    if n == "1":
                        r.Encryption()
                    elif n == "2":
                        t.Encryption()
                    elif n == "3":
                        g.Encryption()
                    elif n == "4":
                        break
                elif choice == "2":
                    print("->Выберите метод расшифрования:\n->\t1) Замена\n->\t2) Перестановка\n->\t3) Гаммирование\n->\t4) Вернуться в главное меню\n")
                    n = input("Введите 1, 2, 3 или 4: ")
                    n = n[0]
                    if n == "1":
                        r.Decryption()
                    elif n == "2":
                        t.Decryption()
                    elif n == "3":
                        g.Decryption()
                    elif n == "4":
                        break
                elif choice == "3":
                    print("->Выберите метод шифрования, для которого нужно создать ключ:\n->\t1) Замена\n->\t2) Перестановка\n->\t3) Гаммирование\n->\t4) Вернуться в главное меню\n")
                    n = input("Введите 1, 2, 3 или 4: ")
                    n = n[0]
                    if n == "1":
                        r.GenKey()
                    elif n == "2":
                        t.GenKey()
                    elif n == "3":
                        g.GenKey()
                    elif n == "4":
                        break
                elif choice == "4":
                    flag = False
                    break
                elif i == 2:
                    print("Слишком много ошибок. До свидания")
                    flag = False
                else:
                    print("Неправильно введена комманда\n")
            except IndexError:
                print("Неправильно введена комманда\n")
    except BaseException:
        print("Произошла ошибка")
