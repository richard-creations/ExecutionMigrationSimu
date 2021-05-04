'''
AUTHOR: RICHARD MADUKA
TITLE: SIMULATION OF EXECUTION MIGRATION IN DISTRUBUTED MULTICORE IPC
'''
from MasterCPU import MasterCPU
import random

try:
    noOfCores = int(input("Enter number of cores (4 and above): "))
except:
    noOfCores = 16
cacheSize = '32'
#cacheSize = input("Enter L1 cache size for cores or press enter for default size: ")
cpu = MasterCPU(noOfCores, cacheSize)


print(f"\n{noOfCores} cores successfully created.\n")

for _ in range(noOfCores * 4):
    cpu.fork()

def main():
    '''
    SIMULATION: The Execution Migration Machine
    This python project is an attempt to simulate a multi-core distributed memory architecture concept
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

    


    '''

    simulate()

def simulate(verbose = False):
    try:
        simTotal = int(input("Enter number of simulations (50 is default) : "))
    except:
        simTotal = 50
    try:
        k = int(input("Enter how many accesses K to look ahead (20 is default): "))
    except:
        k = 20

    total_OPT = 0
    total_noMigr = 0
    total_noAccess = 0

    print(f"SimNo\tOPT\tnoMigr\t noAccess")
    for sim_num in range(simTotal):
        if verbose is True:
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

        if verbose is True:
            print("Simulated addresses fetched from main memory into L1cache:")
            print(created)
            print()
        
        for _ in range(numAccesses - 1):
            accesses.append(created[random.randint(0, numCreations -1)][1])
        if verbose is True:
            print(f"P{testPID} accesses")
            print(accesses)
            print()
      
        currOPT = OPT(k, 0, cpu.getProccessHome(1), accesses)
        currOPT_noMigr = OPT_noMigration(k, 0, cpu.getProccessHome(1), accesses)
        currOPT_noAccess = OPT_noAccess(k, 0, cpu.getProccessHome(1), accesses)
        total_OPT+=currOPT
        total_noMigr+=currOPT_noMigr
        total_noAccess+=currOPT_noMigr

        print(f"{sim_num}:\t{currOPT}\t"+
        f"{currOPT_noMigr}\t" +
        f"{currOPT_noAccess}")
    print(f"Average cost with Execution Migration and Remote Access: {total_OPT/simTotal}")
    print(f"Average cost without Execution Migration: {total_noMigr/simTotal}")
    print(f"Average cost without Remote Access: {total_noAccess/simTotal}")


#-------------------------------------------------------------------------------------
#DYNAMIC PROGRAMMING OPTIMIZATION when there is execution migration and remote access
#Time Complexity: O(NQ^2) Where Q is number of processors.
#-------------------------------------------------------------------------------------
'''
base case: if i == last access to look ahead: break

SUBPROBLEM: Every next acccess is a sub problem

recursive case:  return min(OPT(k, i + 1, core, access) + cpu.getAccessCost(core, destCore), 
                OPT(k, i + 1, destCore, access) + cpu.getMigrationCost(core, destCore)), if cache miss
'''
def OPT(k, i, core, access):
    if i > k or i > len(access) -2:
        return 0
    destCore = cpu.getCore(access[i+1])

    if destCore == -1:
        #not in any L1 cache Ignore for this simulation
        return OPT(k, i + 1, core, access)
    elif core == destCore: 
        #cache hit
        return OPT(k, i + 1, core, access) + cpu.getAccessCost(core, destCore)
    else:                   
        #cache miss
        return min(OPT(k, i + 1, core, access) + cpu.getAccessCost(core, destCore), 
                OPT(k, i + 1, destCore, access) + cpu.getMigrationCost(core, destCore))
    
'''
OPT solution when there is no execution migration
'''
def OPT_noMigration(k, i, core, access):
    if i > k or i > len(access) -2 :
        return 0
    destCore = cpu.getCore(access[i+1])
    if destCore == -1:
        return OPT_noMigration(k, i + 1, core, access)
    elif core == destCore:
        return OPT_noMigration(k, i + 1, core, access) + cpu.getAccessCost(core, destCore)
    else:
        return OPT_noMigration(k, i + 1, core, access) + cpu.getAccessCost(core, destCore)


'''
OPT solution when there is ONLY execution migration
'''
def OPT_noAccess(k, i , core, access):
    if i > k or i > len(access) - 2:
        return 0
    destCore = cpu.getCore(access[i+1])
    if destCore == -1:
        return OPT_noAccess(k, i + 1, core, access)
    elif core == destCore:
        return OPT_noAccess(k, i + 1, core, access) + cpu.getAccessCost(core, destCore)
    else:
        return OPT_noAccess(k, i + 1, destCore, access) + cpu.getMigrationCost(core, destCore) 


if __name__ == "__main__":
    # execute only if run as a script
    main()