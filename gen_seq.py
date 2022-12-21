
def fun_lst_fibo(n=50):
    '''
    ф-я вычисляет ряд Фибоначчи
    :param n: количество членов ряда (по умолчанию 50)
    :return: список членов ряда
    '''
    n=50 if not isinstance(n, int) else n
    lst=[1,1]
    for i in range(2, n):
        lst.append(lst[-1]+lst[-2])
    return lst

def gen_lst_fibo(n=50):
    '''
    генератор ряда Фибоначчи
    :param n: число членов
    :return: след член ряда
    '''
    n=50 if not isinstance(n, int) else n
    lst=[]
    for i in range(n):
        lst.append(1) if i<2 else lst.append(lst[-1]+lst[-2])
        yield lst[-1]

if __name__ == "__main__" :
    length = 20
    lst = fun_lst_fibo(length)
    print(*lst)
    print(lst.__sizeof__())

    gen = gen_lst_fibo(length)
    print(gen)
    print(gen.__sizeof__())
    for i in range(length):
        print(next(gen), end=' ')