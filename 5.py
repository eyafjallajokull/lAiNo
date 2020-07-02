import multiprocessing as mp
from time import time
from sys import argv
import typing
import os


def launch(lim: int) -> None:
    sqr_lim = int(lim ** 0.5)
    pool = mp.Pool(processes=3)
    calcproc1 = pool.apply_async(calc1, args=(lim, sqr_lim))
    calcproc2 = pool.apply_async(calc2, args=(lim, sqr_lim))
    calcproc3 = pool.apply_async(calc3, args=(lim, sqr_lim))
    calcproc1.wait()
    calcproc2.wait()
    calcproc3.wait()
    del calcproc1, calcproc2, calcproc3
    pool.close()
    pool.join()
    tim = time()
    with open("1.txt", "r") as f1:
        cll1 = f1.read().strip("[").strip("]").split(", ")
    os.remove("1.txt")
    with open("2.txt", "r") as f2:
        cll2 = f2.read().strip("[").strip("]").split(", ")
    os.remove("2.txt")
    is_prime = cll1
    for prel in range(len(is_prime)):
        if is_prime[prel] == cll2[prel] and cll2[prel] == "True":
            is_prime[prel] = "False"
        elif is_prime[prel] != cll2[prel] and cll2[prel] == "True":
            is_prime[prel] = "True"
        if time() - tim >= 5.0:
            print(f"Общий алгоритм №1.1: число: {prel}")
            tim = time()
    del cll2
    with open("3.txt", "r") as f3:
        cll3 = f3.read().strip("[").strip("]").split(", ")
    os.remove("3.txt")
    for prel in range(len(is_prime)):
        if is_prime[prel] == cll3[prel] and cll3[prel] == "True":
            is_prime[prel] = "False"
        elif is_prime[prel] != cll3[prel] and cll3[prel] == "True":
            is_prime[prel] = "True"
        if time() - tim >= 5.0:
            print(f"Общий алгоритм №1.2: число: {prel}")
            tim = time()
    del cll3
    is_prime[2] = "True"
    is_prime[3] = "True"
    for i in range(5, sqr_lim + 1):
        if is_prime[i] == "True":
            n = i * i
            for j in range(n, lim + 1, n):
                is_prime[j] = "False"
        if time() - tim >= 5.0:
            print(f"Проверка квадрата числа: {i}")
            tim = time()
    with open("common.txt", "w") as c:
        c.write("2\n3\n5")
        for i in range(6, lim + 1):
            if (is_prime[i] == "True") and (i % 3 != 0) and (i % 5 != 0):
                c.write(f"\n{i}")
            if time() - tim >= 5.0:
                print(f"Проверка делимости на 3 и на 5: {i}")
                tim = time()
    if os.path.exists("11.txt"):
        os.remove("11.txt")
    if os.path.exists("12.txt"):
        os.remove("12.txt")
    if os.path.exists("21.txt"):
        os.remove("21.txt")
    if os.path.exists("22.txt"):
        os.remove("22.txt")
    if os.path.exists("31.txt"):
        os.remove("31.txt")
    if os.path.exists("32.txt"):
        os.remove("32.txt")


def strtobool(x: str) -> bool:
    if x == "True":
        return True
    elif x == "False":
        return False


def calc1(lim: int, sqr_lim: int) -> typing.List[bool]:
    tim = time()
    it = 0
    x = 0
    i1 = 1
    j1 = 1
    if os.path.exists("11.txt"):
        with open("11.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    elif os.path.exists("12.txt"):
        with open("12.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    else:
        is_prime = [False for i in range(lim + 1)]
    try:
        y
        ck = 1
    except NameError:
        ck = 0
    for i in range(i1, sqr_lim + 1):
        x += 2 * i - 1
        if ck == 0:
            y = 0
        for j in range(j1, sqr_lim + 1):
            if it == 1000000:
                if os.path.exists("11.txt"):
                    with open("12.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    os.remove("11.txt")
                else:
                    with open("11.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    if os.path.exists("12.txt"):
                        os.remove("12.txt")
                it = 0
            y += 2 * j - 1
            n = 4 * x + y
            if (n <= lim) and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Первый процесс: x^2: {x}, y^2: {y}")
                tim = time()
            it += 1
            ck = 0
    writing(1, is_prime)
    del is_prime


def calc2(lim: int, sqr_lim: int) -> typing.List[bool]:
    tim = time()
    it = 0
    x = 0
    i1 = 1
    j1 = 1
    if os.path.exists("21.txt"):
        with open("21.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    elif os.path.exists("22.txt"):
        with open("22.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    else:
        is_prime = [False for i in range(lim + 1)]
    try:
        y
        ck = 1
    except NameError:
        ck = 0
    for i in range(i1, sqr_lim + 1):
        x += 2 * i - 1
        if ck == 0:
            y = 0
        for j in range(j1, sqr_lim + 1):
            if it == 1000000:
                if os.path.exists("21.txt"):
                    with open("22.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    os.remove("21.txt")
                else:
                    with open("21.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    if os.path.exists("22.txt"):
                        os.remove("22.txt")
                it = 0
            y += 2 * j - 1
            n = 3 * x + y
            if (n <= lim) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Второй процесс: x^2: {x}, y^2: {y}")
                tim = time()
            it += 1
            ck = 0
    writing(2, is_prime)
    del is_prime


def calc3(lim: int, sqr_lim: int) -> typing.List[bool]:
    tim = time()
    it = 0
    x = 0
    i1 = 1
    j1 = 1
    if os.path.exists("31.txt"):
        with open("31.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    elif os.path.exists("32.txt"):
        with open("32.txt", "r") as sl:
            ijxy = sl.readline().split(" ")
            i1 = int(ijxy[0])
            x = int(ijxy[1]) - (2 * i1 - 1)
            j1 = int(ijxy[2].strip("\n"))
            y = int(ijxy[3])
            is_prime = [strtobool(el) for el in sl.readline().strip("[").strip("]").split(", ")]
    else:
        is_prime = [False for i in range(lim + 1)]
    try:
        y
        ck = 1
    except NameError:
        ck = 0
    for i in range(i1, sqr_lim + 1):
        x += 2 * i - 1
        if ck == 0:
            y = 0
        for j in range(j1, sqr_lim + 1):
            if it == 1000000:
                if os.path.exists("31.txt"):
                    with open("32.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    os.remove("31.txt")
                else:
                    with open("31.txt", "w") as sl:
                        sl.write(f"{i} {x} {j} {y}\n")
                        sl.write(str(is_prime))
                    if os.path.exists("32.txt"):
                        os.remove("32.txt")
                it = 0
            y += 2 * j - 1
            n = 3 * x - y
            if (i > j) and (n <= lim) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Третий процесс: x^2: {x}, y^2: {y}")
                tim = time()
            it += 1
            ck = 0
    writing(3, is_prime)
    del is_prime


def writing(way: int, is_prime: list) -> None:
    way = str(way) + ".txt"
    with open(way, "w") as f:
        f.write(str(is_prime))


try:
    if __name__ == "__main__":
        if int(argv[1]) > 0:
            lim = int(argv[1])
        else:
            raise Exception
        start = time()
        launch(lim)
        print(f"Время выполение: {time() - start} сек.")
except MemoryError:
    print("Вам не хватает оперативной памяти")
except Exception:
    print("Неправильно задан аргумент")
except KeyboardInterrupt:
    print("*произошло нажатие CTRL + C")
