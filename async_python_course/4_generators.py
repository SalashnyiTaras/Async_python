from time import time

# interesting about generators - next() runs program up to next yield


def gen_filename():
    """example of simple generator"""
    while True:
        pattern = f'file-{str(int(time()*1000))}.jpeg'
        yield pattern
        print('code to be run after yield')


# round robin event loop
def gen1(s):
    for k in s:
        yield k


def gen2(n):
    for j in range(n):
        yield j


g1 = gen1('tarik')
g2 = gen2(5)


tasks = [g1, g2]


while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
