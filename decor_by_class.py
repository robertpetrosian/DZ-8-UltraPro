import classes.fibo as cf
import gen_seq as gs



if __name__ == "__main__"  :
    length = 200
    t = cf.CounterOfTime()
    t.start()
    gg=gs.fun_lst_fibo(length)
    elapsed = t.stop()*10**6
    print(*gg)
    print(f"длительность функции {elapsed :6.3f} мс , память {gg.__sizeof__()}")

    # gg=[]
    t = cf.CounterOfTime()
    t.start()
    # for i in range(length):
    #     gg.append(next(gen))
    gen=gs.gen_lst_fibo(length)
    elapsed = t.stop()*10**6
    gg = [next(gen) for x in range(length) ]
    print(*gg)
    print(f"длительность генератора {elapsed :6.3f} мс, память {gen.__sizeof__()} ")

