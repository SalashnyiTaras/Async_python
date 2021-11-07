def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

#
# def sub_gen():
#     for i in 'tarik':
#         yield i
#
#
# def delegator(g):
#     """
#     example of simplest delegated generator
#     """
#     for j in g:
#         yield j


def sub_gen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('Done iteration')
        else:
            print('...........', message)


@coroutine
def delegator(g):
    """
    example of more complicated delegated generator

    interesting that:
        try:
            data = yield
            g.send(data)
        except StopIteration as e:
            g.throw(e)
    can be changed to:
        yield from <generator>

    So, when using yield from - we do not need to initialize sub generator,
    it also does loop for us, it send params and exceptions to sub gen. Another point of using
    delegating generator with 'yield from' is that we can still modify what return statement from
    sub generator returns

    'yield from' just gets value from iterable

    in other languages 'yield from' is called 'await'. Why 'await'? Because delegator has full control
    of sub generator and until sub generator is executed, delegator is blocked - it awaits))))
    """
    while True:
        yield from g
