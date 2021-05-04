    SIMULATION PROGRAM: Trying concepts from the paper "The Execution Migration Machine"

    This python project is an attempt to simulate a multi-core distributed memory architecture concepts
    of the execution migration machine.
    
    The total number of cores and processes can be simulated to any amount.

    The objective is to simulate the idea of execution migration and compare it to conventional remote access

    Given processes p1,p2,p3,p4,p5,p6...pN

    Assuming that in any given execution flow, p1 (or any chosen proccess) will need to access 
    remote data created by different proccesses at differnt cores for inter-proccess communication (IPC)

    E.G: P1 may need to use some data created by p3 and stored in the core of which p3 is running
    - p1 can either migrate excution or perform a remote access to fetch 64 bits of data from p3

    However, p1 might already have cache affinity at it's initial core.
    - Using Dynamic programming, the optimal solution for execution flow of the the 
    processes depends on how decisions are made to either migrate or perform a remote access.

    Advantage of execution migration:
        - It would eliminate the need for a round trip which occurs in remote access.
    Drawbacks of execution migration:
       -  Execution Migration comes with a setup cost which depends on the size of the PCB which is constant.
    
    Advantage of remote access:
        - If there are not too many subsequent remote accesses, it would be cheaper to fetch from another cores cache.

    if the thread context is small compared to the data that would otherwise be transferred it would be better to migrate
    thread.


    ASSUMPTIONS:
    - Fixed data access size in cache
    - Fixed context size or Process Control Block
    - Fine Grained Hardware execution
    - Ignoring Data-Bus and hardware congestions


    HOW TO RUN:

    run "python main.py" to start the program.

    The program will prompt for number of cores to simulate
    
    Simulation number is the number of tests you want to run.

    K is how many instructions to look agead for as in real life scenarios proccesses do not typically run out.

    
