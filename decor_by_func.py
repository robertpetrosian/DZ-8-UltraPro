import time
import functools
import json

timer = time.perf_counter

def timer_decorator_file(func):
    '''
    декоратор с выводом в файл врмемни исполнения
    :param func: функция
    декоратор вычисляет время исполнения функции и записывает в журнал decor.json
    имя ф-ии , старт и длительность исполнения
    :return: ф-я декоратор
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_datetime = time.asctime()  # время начала
        start = timer()  # время начала процесса
        ret = func(*args, **kwargs)  # исполнение функции
        elapsed_ms = (timer() - start) * 10 ** 6  # длительность работы функции в мс

        with open('decor.json', 'w') as f:
            # запись в файл формата json
            f.write(json.dumps({'name': func.__name__,
                                'begin': start_datetime,
                                'elapsed': int(elapsed_ms)}))

        return ret  # результат ф-ии

    return wrapper  # результат декоратора


def timer_decorator_print(func):
    '''
    декоратор с печатью результата
    :param func: функция
    декоратор вычисляет время исполнения функции и печатает длительность исполнения
    :return: ф-я декоратор
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = timer()  # время начала процесса
        ret = func(*args, **kwargs)  # исполнение функции
        stop = timer()
        print(
            f"функция {func.__name__} длительность {(stop - start) * 10 ** 6 :6.0f} мс")  # печать результат декоратора
        return ret  # результат ф-ии

    return wrapper  # результат декоратора


@timer_decorator_print
@timer_decorator_file
def decor_fibo(n):
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[-1] + lst[-2])
        # lst.pop(0)
    return lst


if __name__ == "__main__":
    length = 20
    # использование функции-декортаторов для замера и записи времени исполнения
    print(decor_fibo)  # смотрим как сработал functools.wraps
    print(decor_fibo(length))  # вычисление Числа Фибоначчи и проверка как сработали оба декоратора

