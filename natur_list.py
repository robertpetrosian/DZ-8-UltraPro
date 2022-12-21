import time
import functools

SIZE = 0

def decor_size(func):
    '''
    декоратор замеряющий размер памяти ф-ии
    :param func: ф-я
    :return: размер памяти
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global SIZE
        ret=func(*args, **kwargs)
        SIZE = ret.__sizeof__()
        print(f'декорированная {func.__name__} занимает {SIZE}')
        return ret
    return wrapper

def lst_natur_list(n):
    '''
    ф-я возвращает список n натуральных чисел
    :param n: количество чисел
    :return: список
    '''
    return [x for x in range(n)]

# декорированная ф-я , не использовал @ чтобы иметь доступ к оригиналу
decorated_lst_natur_list = decor_size(lst_natur_list)

def gen_natur_list(n):
    '''
    ф-я генерирует до n натуральных чисел
    :param n: количество чисел
    :return: очередной элемент
    '''
    for i in range(n):
        yield i

# декорированный ген-р , не использовал @ чтобы иметь доступ к оригиналу
decorated_gen_natur_list = decor_size(gen_natur_list)

if __name__ == "__main__":
    length = 10**6
    start = time.perf_counter()
    lst = lst_natur_list(length)
    stop = time.perf_counter()
    elapsed = stop-start
    print(lst[-1], lst.__sizeof__() , f'elapsed {elapsed*10**6 :6.2f} ms')

    start = time.perf_counter()
    gen = gen_natur_list(length)
    stop = time.perf_counter()
    elapsed = stop-start
    lst=[next(gen) for i in range(length)]
    print(lst[-1], gen.__sizeof__(), f'elapsed {elapsed*10**6 :6.2f} ms')

    lst = decorated_lst_natur_list(length)
    size_of_lst = SIZE
    gen = decorated_gen_natur_list(length)
    size_of_gen = SIZE
    print(f'разница между размерами памяти список-генератор {size_of_lst-size_of_gen :,} ')

