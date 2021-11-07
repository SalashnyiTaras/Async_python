def subgen():
    """
    coroutines are  generators which can accept value using method send(). It is necessary to initialize a coroutine
    passin argument None in function send():
    g = gen()
    g.send(None)
    Interesting that yield can not only separately accept or return value, but both:
    yield will return smh during initializatoin(when passing None) and send smh after it, when using send(vmh)
    """
    x = 'Ready to get message'
    message = yield x
    print('Subgen recieved', message)


def coroutine(func):
    """
    you create function in order not to initialize coroutine each time (no need to do send(None))
    you use getgeneratorstate() from inspect module to check generator state
    """
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average():
    """
    you can to exception in coroutine using throw()
    you can also use return statement beside yield statement. To get return value you need to catch exception, and use
    its value:
    try:
        g.throw(StopIteration)
    except StopIteration as e:
        print('return value', e.value)
    """
    count = 0
    summa = 0
    average = 0

    while True:
        try:
            x = yield average
        except StopIteration:
            print('done')
        else:
            count += 1
            summa += x
            average = round(summa / count, 2)
    return average
