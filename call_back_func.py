# TODO: find a first number in fibo's sequence divided by 17

def fibonacci():
    """solution using simple function"""
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        if values[-1] % 17 == 0:
            return values[-1]

        if values[-1] > 10000:
            return


if __name__ == '__main__':
    res = fibonacci()
    if res is not None:
        print(res)


def fibonacci():
    """solution using generator """
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = (values[-1], values[-1] + values[-2])
        yield values[-1]


for f in fibonacci():
    if f % 17 == 0:
        print(f)
        break
    if f > 10000:
        break


def fibonacci(cb):
    """solution using call-back function"""
    values = []
    while True:
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        r = cb(values[-1])
        if r[0]:
            return r[1]


def check_17(v):
    if v % 17 == 0:
        return True, v

    if v > 10000:
        return True, None

    return False,


if __name__ == '__main__':
    res = fibonacci(check_17)
    if res is not None:
        print(res)


class Fibonacci:
    """solution using iterators"""

    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.values) < 2:
            self.values.append(1)
        else:
            self.values = [self.values[-1], self.values[-1] + self.values[-2]]
        return self.values[-1]


for f in Fibonacci():
    if f % 17 == 0:
        print(f)
        break
    if f > 10000:
        break


