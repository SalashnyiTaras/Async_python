"""
--------------------------------------------------------------------------------------------------------------
Often we see that generators yielding values. It is also possible to send values back to
generators. When this happens, after returning execution to the generator function,
the yield statement itself gives the value that was sent into the generator.
To do this, we need to replace next() with gen.send()
gen.send() executes the function from where it left off and will return any yielded values
from generator.

So coroutine is a generator-based function which can send value to generator
"""


def counter(start=0, limit=10):
    value = start
    while value < limit:
        x = yield value
        value += x
    yield value


def main():
    gen = counter()
    gen.send(None)
    while True:
        value = randint(1, 3)
        total = gen.send(value)
        print(f'sent {value}, got {total}')


main()
