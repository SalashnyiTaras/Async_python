"""
core of every async app - event loop. It is responsible for switching between task(like manager)

asyncio is intended to be used for efficient writing of event loops

every async app uses data structure to keep tasks. In previous project we used lists and dicts.
in asyncio Task(Future) is used instead and it hold coroutines. So instances of module
Task should be applied async.

class Future  - заглушка: кожна функція передасть контроль виконання тільки коли закінчить своє
виконання. Щоб не чекати поки виконається функція - достатньо передати мітку про те що ф-ція має
закінчитися. Що й робить class Future.
Наприклад ми запитуємо дані з дб. Замість того, шоб код простоював чекаючи результату запиту,
ми отримаємо заглушку 'памятаю про ф-цію, поки можеш зробити щось інше. коли буде готово прийдеш
за результатами'

Algo:
write coroutines - logic
оборочиваем корутини в екземпляры класа Task
стаивим курутини в очередь на выполнения и запускаем ивент луп
дожидаемся результатаэ выполнения
закрываем событийный цикл
to do this asyncio gives high-level abstraction
"""
import asyncio


@asyncio.coroutine
def print_nums():
    """
    @coroutine does not initialize generator, but it makes a coroutine from function based
    on generator
    """
    pass


def print_time():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
