from abc import ABC, abstractmethod, abstractclassmethod
from itertools import groupby
import random, json

class Papa(ABC):

    def ALPH(self):
        try:
            self.er = 0
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
                    self.alph = [el.lower() for el, _ in groupby(alph["alph"])]
                else:
                    print("Неверный формат: значение ключа 'alph' не является списком\n")
                    self.er = 1
            else:
                print("Неверный формат: в данном словаре нет ключа 'alph'\n")
                self.er = 1
        except json.decoder.JSONDecodeError:
            print("Данный файл находится не в формате json\n")
            self.er = 1
        except FileNotFoundError:
            print("Такого файла не существует\n")
            self.er = 1
        except OSError:
            print('Расширение данного файла не ".alph"\n')
            self.er = 1
        except Exception:
            self.er = 1

    def KEY(self, x, enkey):
        self.er = 0
        if x == "r":
            try:
                wk = input("\nВведите полный путь к файлу ключа (файл должен иметь расширение .key): ")
                with open(wk, 'r', encoding = "UTF-8") as key:
                    if wk[-4:] != ".key":
                        raise OSError()
                    else:
                        pass
                    self.enlist = json.load(key)
            except FileNotFoundError:
                print("Такого файла не существует\n")
                self.er = 1
            except json.decoder.JSONDecodeError:
                print("Данный файл находится не в формате json")
                self.er = 1
            except OSError:
                print('Расширение данного файла не ".key"')
                self.er = 1
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
        self.er = 0
        if x == "r":
            try:
                wt = input("\nВведите полный путь к файлу открытого текста (файл должен иметь расширение .txt): ")
                with open(wt, 'r', encoding = "UTF-8") as tx:
                    if wt[-4:] != ".txt":
                        raise OSError()
                    else:
                        pass
                    self.txt = tx.read()
            except FileNotFoundError:
                print("Такого файла не существует")
                self.er = 1
            except OSError:
                print('Расширение данного файла не ".txt"')
                self.er = 1
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
        self.er = 0
        if x == "r":
            try:
                we = input("\nВведите полный путь к файлу шифртекста (файл должен иметь расширение .encode): ")
                with open(we, 'r', encoding = "UTF-8") as etx:
                    if we[-7:] != ".encode":
                        raise OSError()
                    else:
                        pass
                    self.etxt = json.load(etx)
            except FileNotFoundError:
                print("Такого файла не существует\n")
                self.er = 1
            except OSError:
                print('Расширение данного файла не ".encode"')
                self.er = 1
            except json.decoder.JSONDecodeError:
                print("Данный файл находится не в формате json\n")
                self.er = 1
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
        if self.er == 0:
            enkey = self.alph.copy()
            random.shuffle(enkey)
            alphasc = [ord(letter) for letter in self.alph]
            kuyasc = [ord(letter) for letter in enkey]
            enkey = {"Cipher method" : "Replacement", "Alphabet ASCII": alphasc, "Key ASCII": kuyasc}
            self.KEY("", enkey)
        else:
            print("Возврат в Главное меню\n")

    def Encryption(self):
        self.TXT("r", "")
        if self.er == 0:
            self.KEY("r", "")
            if self.er == 0:
                if self.enlist["Cipher method"] == "Replacement":
                    self.txt = self.txt.lower()
                    alphlist = [chr(let) for let in self.enlist["Alphabet ASCII"]]
                    for letter in self.txt:
                        if letter in alphlist:
                            pass
                        else:
                            print("\nВ данном открытом тексте присутствуют символы, которых нет в данном алфавите\nШифрование может работать некорректно")
                            flag = True
                            while flag:
                                for i in range(3):
                                    command = input("Желаете продолжить?(Y/N) ").upper()
                                    if command == 'Y':
                                        flag = False
                                        break
                                    elif command == 'N':
                                        flag = False
                                        self.er = 1
                                        break
                                    else:
                                        print("Неправильно введена комманда\n")
                                    if i == 2:
                                        print("Слишком много ошибок. До свидания")
                                        flag = False
                                        self.er = 1
                    if self.er == 0:
                        kdict = {letter: enletter for letter, enletter in zip(self.enlist["Alphabet ASCII"], self.enlist["Key ASCII"])}
                        defdict = {"Cipher method" : "Replacement", "Ciphertext" : self.txt.translate(kdict)}
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
        if self.er == 0:
            if self.etxt["Cipher method"] == "Replacement":
                self.KEY("r", "")
                if self.er == 0:
                    if self.enlist["Cipher method"] == "Replacement":
                        dkdict = {enletter: letter for letter, enletter in zip(self.enlist["Alphabet ASCII"], self.enlist["Key ASCII"])}
                        dtext = self.etxt["Ciphertext"].translate(dkdict)
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
        if self.er == 0:
            self.KEY("r", "")
            if self.er == 0:
                if self.enlist["Cipher method"] == "Transposition":
                    if len(self.enlist["Key"]) > len(self.txt):
                        print("Длина данного блока перестановки больше длины текста\nСоздайте новый ключ или выберите корректный")
                        print("Возврат в Главное меню\n")
                    else:
                        if len(self.txt) % len(self.enlist["Key"]) != 0:
                            n = len(self.enlist["Key"]) - len(self.txt) % len(self.enlist["Key"]) + len(self.txt)
                            txt = self.txt.ljust(n, self.txt[random.randint(0, len(self.txt))])
                        else:
                            pass
                        text = list(txt)
                        for i in range(0, len(text), len(self.enlist["Key"])):
                            string = [text[i+j] for j in range(len(self.enlist["Key"]))]
                            for j in range(len(self.enlist["Key"])):
                                text[i + j] = string[self.enlist["Key"][j]]
                        defdict = {"Cipher method" : "Transposition", "Ciphertext" : "".join(text), "Difference": n - len(self.txt)}
                        self.ENCODE("", defdict)
                else:
                    print("Ключ не соотвествует данному методу шифрования\nВозврат в Главное меню\n")
            else:
                print("Возврат в Главное меню\n")
        else:
            print("Возврат в Главное меню\n")

    def Decryption(self):
        self.ENCODE("r", "")
        if self.er == 0:
            if self.etxt["Cipher method"] == "Transposition":
                self.KEY("r", "")
                if self.er == 0:
                    if self.enlist["Cipher method"] == "Transposition":
                        etxt = list(self.etxt["Ciphertext"])
                        for i in range(0, len(etxt), len(self.enlist["Key"])):
                            string = [etxt[i+j] for j in range(len(self.enlist["Key"]))]
                            for j in range(len(self.enlist["Key"])):
                                etxt[i + self.enlist["Key"][j]] = string[j]
                        dtext = "".join(etxt)
                        dtext = dtext[ : - self.etxt["Difference"]]
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
        if self.er == 0:    
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
            enkey = [random.randint(0, len(self.alph)) for i in range(siz)]
            hdict = {"Cipher method" : "Gamming", "Gamma": enkey, "Alphabet": self.alph}
            self.KEY("", hdict)
        else:
            print("Возврат в Главное меню\n")

    def Encryption(self):
        self.TXT("r", "")
        if self.er == 0:
            self.KEY("r", "")
            if self.er == 0:
                if self.enlist["Cipher method"] == "Gamming":
                    self.txt = self.txt.lower()
                    for letter in self.txt:
                        if letter in self.enlist["Alphabet"]:
                            pass
                        else:
                            print("\nВ данном открытом тексте присутствуют символы, которых нет в данном алфавите. Пожалуйста, создайте ключ с помощью более полного алфавита")
                            self.er = 1
                            break
                    if self.er == 0:
                        if len(self.enlist["Gamma"]) > len(self.txt):
                            print("Длина данной гаммы больше длины текста\nСоздайте новый ключ или выберите корректный")
                            print("Возврат в Главное меню\n")
                        else:
                            if len(self.txt) % len(self.enlist["Gamma"]) != 0:
                                n = len(self.enlist["Gamma"]) - len(self.txt) % len(self.enlist["Gamma"]) + len(self.txt)
                                txt = self.txt.ljust(n, random.choice(self.enlist["Alphabet"]))
                            else:
                                pass
                            text = list(txt)
                            kdict = {self.enlist["Alphabet"][i]: i for i in range(len(self.enlist["Alphabet"]))}
                            revkdict = {key: value for value, key in kdict.items()}
                            for i in range(0, len(text), len(self.enlist["Gamma"])):
                                string = [(kdict[text[i + j]] + self.enlist["Gamma"][j]) % len(self.enlist["Alphabet"]) for j in range(len(self.enlist["Gamma"]))]
                                for j in range(len(self.enlist["Gamma"])):
                                    text[i + j] = revkdict[string[j]]
                            defdict = {"Cipher method" : "Gamming", "Ciphertext" : "".join(text), "Difference": n - len(self.txt)}
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
        if self.er == 0:
            if self.etxt["Cipher method"] == "Gamming":
                self.KEY("r", "")
                if self.er == 0:
                    if self.enlist["Cipher method"] == "Gamming":
                        etxt = list(self.etxt["Ciphertext"])
                        kdict = {self.enlist["Alphabet"][i]: i for i in range(len(self.enlist["Alphabet"]))}
                        revkdict = {key: value  for value, key in kdict.items()}
                        for i in range(0, len(etxt), len(self.enlist["Gamma"])):
                            string = [(kdict[etxt[i + j]] - self.enlist["Gamma"][j]) % len(self.enlist["Alphabet"]) for j in range(len(self.enlist["Gamma"]))]
                            for j in range(len(self.enlist["Gamma"])):
                                etxt[i + j] = revkdict[string[j]]
                        dtext = "".join(etxt)
                        dtext = dtext[ : - self.etxt["Difference"] + 2]
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