"""
Coroutine - functions which enables concurrency via cooperative multitasking
Simple function - a sequence of instructions that takes inputs and returns outputs
---------------------------------------------------------------------------------------------------
"""
from dis import dis


def square(x: int) -> int:
    return x * x


def main() -> None:
    """
    looks easy because many things are taken for granted:

    CPython uses virtual machine(VM) to execute a program. We can check cpython bytecode
    using dis.dis module. This bytecode is exact instruction which uses virtual machine
    to execute python code.

    CPython uses a 'stack based' virtual machine. There are no registers comparing with
    assembly programming. If an instruction needs to operate on some piece of data, this
    data must be first onto the stack.

    Stack - linear block of memory that contains data or references to data.
    VM uses 'stack pointer' to keep track of stack's state.

    When executing instruction it is only possible to push data on top of the stack.
    'Load fast instruction' has only one job - to push single value onto the stack.
    Each time this happens, stack pointer is incremented to point at the new top of the
    stack. Other instructions can then consume or pop instructions from stack and also can
    add items onto stack.

    Not everything lives solely on the stack - data that outlasts the function creating
    has to be stored somewhere else, so data does not go away when function returns.
    So python uses the heap to store objects in long-term memory.
    The heap is unordered space where objects can be allocated and deallocated at any time
    during execution.
    Often items on the stack are just references to real objects in heap.

    When executing a code runtime needs to keep track of its position in the set of
    instructions. Each instruction has predetermine fixed size in memory ans therefore has
    its own memory address. So the runtime can keep track of the next instruction it has to
    execute. Each time runtime execute an instruction, instruction pointer is incremented.
    Special instructions can them modify the instruction pointer allowing runtime jump
    between different sections of code. (It is bases for all flow control)
    """
    x = square(5)
    print(x)


print("square:")
dis(square)
print("main:")
dis(main)
