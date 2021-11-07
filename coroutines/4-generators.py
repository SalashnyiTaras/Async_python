"""
---------------------------------------------------------------------------------------------------
I am able to yield multiple values overtime and able to start executing from where I left.
Great Generator
"""


def fib(count: int):
    a, b = 1, 0
    for _ in range(count):
        a, b = b, a + b
        yield b


def main():
    """
    Each time we call gen object, via next() generator gives us opportunity to start
    where we left off preserving the full state. If the function yields another value,
    we get that value as the result or return value of the call of next().
    If generator completes or return - StopIterationError is raised
    """
    gen = fib(5)
    print(gen)  # at this point code of gen() even did not started
    while True:
        print(next(gen))


main()
