"""
---------------------------------------------------------------------------------------------------

Ways of achieving concurrency:

    - Multiprocessing, where each worker is its own process: each worker has its own CPython
      runtime, its own stack, heap and its own set of compiled bytecode.
      Cons:
        - duplicated memory use for each runtime
        - any communication between processes has to happen by serializing and deserializing
          data, adding extra work for each task
        - each process is still idle while tasks are waiting on resources
      Pros:
        - each worker can process task in parallel giving higher potential utilization of
          multiple cores (is called parallelism)

    - Threading, idea is to use threads for each worker: when we add new workers, we need to
      add a new call stack for each thread - reducing duplication of heap and bytecode
      Cons:
        - because of GIL we can not run multiple threads of python code at the same time:
          all other threads have to sit and wait idle when current thread is executed.
        - runtime is in charge of scheduling threads with no insight into what threads are
          doing. Everytime new thread is selected we have to wait for a costly switch
          which involves saving execution stack of the previous thread and restoring
          stack for the new thread(preemptive multitasking)
        - difficult to switch task at appropriate time
        - more threads more switching between them, chance of failure when switching increases
      Pros:
        - reducing duplication of heap and bytecode
        - no need for serialization
        - it does utilize fully CPU

    - Cooperative multitasking - switch between task should be daone only when a task waits for
      external resources. Each task need to be completed or yield control before next task
      Pros:
        - simple and inexpensive form of concurrency
        - better use of resources running one process with one thread
        - one heap and stack

      Cons: each task must be well mannered and cooperate with other tasks to share CPU
        and stack
---------------------------------------------------------------------------------------------------
"""