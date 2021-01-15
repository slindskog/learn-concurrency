
# Python Concurrency 


Notes and code following along the educative course: 
[Python Concurrency for Senior Engineering Interviews](https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews).

Linux or Mac is recommended as some scripts cannot run on Windows. 

### Basics 
* Program:
    * A set of instructions and associated data that resides on the disk and is loaded by the operating system to 
    perform a task.
    * E.g., an executable file or a Python script.
    * In order to run a program, the operating system's kernel is first asked to create a new process, which is 
    an environment in which a program is executed. 
* Process:
    * A process is a program in execution.  
* Thread:
    * The smallest unit of execution in a process which simply executes instructions serially. 
    * A process can have multiple threads running as part of it.
    * Threads usually have some state associated with the process that is shared among threads and each
    thread would have some state private to itself.
    * The globally shared state amongst the threads of a process is visible and accessible to all the threads, and 
    special attention needs to be paid when any thread tries to read or write to this global shared state.
    * Note: processes don't share any resources amongst themselves whereas threads of a process can share the resources
    allocated to that particular process, including memory address space.
* Global Interpreter Lock (GIL):
    * Python's Achilles' heel. Is a mutex (or a lock) that allows only one thread to hold the control of the 
    Python interpreter. 
    * This prevents two threads from executing simultaneously in the same program. 
* Concurrency
    * A program that can be decomposed into constituent parts and each part can be executed out of order or in
    partial order without affecting the final outcome.
    * A system capable of running several distinct programs or more than one independent unit of the same
    program in overlapping time intervals is called a *concurrent system*. 
        * E.g., an operating system running on a single core machine is concurrent but not parallel. It can only 
        process one task at any given point, but all the tasks being managed by the operating system appear to make
        progress because the operating system is designed for concurrency. 
* Parallelism
    * A parallel system is one which necessarily has the ability to execute multiple programs as the same time. 
    * E.g., multicore processors on individual machines or a computing cluster where several machines solve independent
    pieces of a problem simultaneously. 
    * An individual problem has to be concurrent in nature. Portions of it can be worked on independently without
    affecting the final outcome before it can be executed in parallel. 
    * A system can be both concurrent and parallel, e.g., a multitasking operating system running on a multicore machine.
    * Parallelism is about doing a lot of things at once. Concurrency is about dealing with lots of things at once.
   
   
### Async.io
* asynchronous input output. The programming paradigm which achieves high concurrency using a single
thread or event loop. 