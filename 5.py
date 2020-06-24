import multiprocessing as mp
from time import time
from sys import argv
import typing


def launch(lim: int) -> None:
    sqr_lim = int(lim ** 0.5)
    is_prime = [False for i in range(lim + 1)]
    is_prime[2] = True
    is_prime[3] = True
    pool = mp.Pool(processes=3)
    calcproc1 = pool.apply_async(calc1, args=(is_prime, sqr_lim))
    calcproc2 = pool.apply_async(calc2, args=(is_prime, sqr_lim))
    calcproc3 = pool.apply_async(calc3, args=(is_prime, sqr_lim))
    calcproc1.wait()
    calcproc2.wait()
    calcproc3.wait()
    cll1 = calcproc1.get()
    del calcproc1
    cll2 = calcproc2.get()
    del calcproc2
    cll3 = calcproc3.get()
    del calcproc3
    tim = time()
    for prel in range(len(is_prime)):
        if is_prime[prel] != cll1[prel]:
            is_prime[prel] = cll1[prel]
        if is_prime[prel] == cll2[prel] and cll2[prel] is True:
            is_prime[prel] = False
        elif is_prime[prel] != cll2[prel] and cll2[prel] is True:
            is_prime[prel] = True
        if is_prime[prel] == cll3[prel] and cll3[prel] is True:
            is_prime[prel] = False
        elif is_prime[prel] != cll3[prel] and cll3[prel] is True:
            is_prime[prel] = True
        if time() - tim >= 5.0:
            print(f"Общий алгоритм №1: число: {prel}")
            tim = time()
    del cll1, cll2, cll3
    pool.close()
    pool.join()
    for i in range(5, sqr_lim + 1):
        if is_prime[i] is True:
            n = i * i
            for j in range(n, lim + 1, n):
                is_prime[j] = False
        if time() - tim >= 5.0:
            print(f"Проверка квадрата числа: {i}")
            tim = time()
    with open("common.txt", "w") as c:
        c.write("2\n3\n5")
        for i in range(6, lim + 1):
            if (is_prime[i] is True) and (i % 3 != 0) and (i % 5 != 0):
                c.write(f"\n{i}")
            if time() - tim >= 5.0:
                print(f"Проверка делимости на 3 и на 5: {i}")
                tim = time()


def calc1(primelist: typing.List[bool], sqr_lim: int) -> typing.List[bool]:
    is_prime = primelist.copy()
    lim = len(is_prime) - 1
    tim = time()
    x = 0
    for i in range(1, sqr_lim + 1):
        x += 2 * i - 1
        y = 0
        for j in range(1, sqr_lim + 1):
            y += 2 * j - 1
            n = 4 * x + y
            if (n <= lim) and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Первый процесс: x^2: {x}, y^2: {y}")
                tim = time()
    return is_prime


def calc2(primelist: typing.List[bool], sqr_lim: int) -> typing.List[bool]:
    is_prime = primelist.copy()
    lim = len(is_prime) - 1
    tim = time()
    x = 0
    for i in range(1, sqr_lim + 1):
        x += 2 * i - 1
        y = 0
        for j in range(1, sqr_lim + 1):
            y += 2 * j - 1
            n = 3 * x + y
            if (n <= lim) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Второй процесс: x^2: {x}, y^2: {y}")
                tim = time()
    return is_prime


def calc3(primelist: typing.List[bool], sqr_lim: int) -> typing.List[bool]:
    is_prime = primelist.copy()
    lim = len(is_prime) - 1
    tim = time()
    x = 0
    for i in range(1, sqr_lim + 1):
        x += 2 * i - 1
        y = 0
        for j in range(1, sqr_lim + 1):
            y += 2 * j - 1
            n = 3 * x - y
            if (i > j) and (n <= lim) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
            else:
                pass
            if time() - tim >= 5.0:
                print(f"Третий процесс: x^2: {x}, y^2: {y}")
                tim = time()
    return is_prime


if __name__ == "__main__":
    try:
        if int(argv[1]) > 0:
            lim = int(argv[1])
        else:
            raise Exception
        start = time()
        launch(lim)
        print(f"Время выполение: {time() - start} сек.")
    except Exception:
        print("Неправильно задан аргумент")
    except MemoryError:
        print("Вам не хватает оперативной памяти")
    except BaseException:
        print("*произошло нажатие CTRL + C")
