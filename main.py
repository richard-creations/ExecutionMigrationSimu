from MasterCPU import MasterCPU
import random

def main():
    noOfCores = int(input("Enter number of cores: "))
    cacheSize = '32'
    #cacheSize = input("Enter L1 cache size for cores or press enter for default size: ")
    cpu = MasterCPU(noOfCores, cacheSize)


    print(f"\n{noOfCores} cores successfully created.\n")

    for _ in range(noOfCores * 4):
        cpu.fork()


 

    '''
    SIMULATION: The Execution Migration Machine
    This python project is an attempt to simulate a multi-core distributed memory architecture cpu.
    The total number of cores and processes can be simulated to any amount.

    The objective is to simulate the idea of execution migration and compare it to conventional remote access

    Given processes p1,p2,p3,p4,p5,p6...N

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
    
    getCost(): 
    '''
    print("preparing simulation memory accesses and cache data...")
    print()
    numCreations = 50
    created = list()
    numAccesses = 20
    accesses = [] * numAccesses
    testPID = 1
   

    for i in range(numCreations):
        pid = random.randint(0, (noOfCores * 4) - 1) #process that created it
        memAddr = "{:012b}".format(random.randint(1, 4096)) #RAM memory address to fetch
        created.append([pid, memAddr])
        cpu.fetchDataFromRAM( pid, memAddr)
    print("proccess and addresses in cache of home core:")
    print(created)
    print()

    for _ in range(numAccesses - 1):
        accesses.append(created[random.randint(0, numCreations -1)][1])
    print(f"P{testPID} accesses")
    print(accesses)
    print()


   
   #UNCOMMENT TO PRINT CACHE OF CORES 
    
    for core in cpu.cores:
        print(f"Core {core.id}: \n{core.status()}")
        i = 0
        '''
        for data in core.L1cache:
            print(f"Cache Index: {i}:: Memory Address::DATA:\n {data}")
            i += 1
        '''
    testAddr = created[3][1]
    print()
    print(f"Testing getCore(): Location of address {testAddr}")
    dest = cpu.getCore(testAddr)
    print(f"core: {dest}")

    print()
    print(f"Testing getMigrationCost() vs getAccessCost(): from proccess 1's home to core {dest}")
    start =cpu.getProccessHome(1)
    print(f"p1 location = {start}")
    print(f"Data location = {dest}")
    print(f"Migration Cost: {cpu.getMigrationCost(start, dest)}")
    print(f"Access Cost: {cpu.getAccessCost( start, dest)}")

if __name__ == "__main__":
    # execute only if run as a script
    main()