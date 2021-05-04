from Core import Core
from Process import Process
import random
import math

class MasterCPU:

    def __init__(self, noOfCores=4, L1CacheSize = '32', L2cacheSize = 32):
        self.CLOCK = 0
        self.noOfCores = noOfCores
        self.L1CacheSize = L1CacheSize
        self.L2CacheSize = L2cacheSize
        self.L2cache = [0] *  L2cacheSize
        self.cores = list()
        self.processList = []
        self.affinity = {}
        self.currentExecution = -1
        self.RAM = open('ram.txt') #USING TEXT FILE AS RAM DATA
        self.registers = {'AH':0,'AL':0,'CH':0,'CL':0, 'DH':0,'DL':0,'BH':0,'BL':0,'SPL':0, 'BPL':0, 'SIL':0, 'DIL':0}
        self.programCounter = 0

        if not L1CacheSize.isdigit():    
            for coreID in range(int(self.noOfCores)):
                self.cores.append( Core(coreID) )
                self.affinity[coreID] = set()

        elif L1CacheSize.isdigit():
            cSize = int(self.L1CacheSize)
            for coreID in range(noOfCores):
                self.cores.append(Core(coreID, cSize))
                self.affinity[coreID] = set()
        
    def fork(self, parentID = 0, exe = "load 1001", verbose=False):
        pid = len(self.processList)
        self.processList.append(Process(pid, exe, parentID, self.CLOCK))
        if verbose is True:
            print(f"Process with PID {pid} created.")
        nextNode = self.nextAvailableNode()
        self.affinity[nextNode].add(pid)
        self.assignProc(pid, nextNode)
        if verbose is True:
            print(f"Process with PID {pid} assigned to core {nextNode}.")
        self.CLOCK +=1

    def assignProc(self, pid, coreID):
        self.cores[coreID].affinity.add(pid)
        self.cores[coreID].procs.add(self.processList[pid])

    #EXECUTION MIGRATION IMPLEMENTATION HERE---------
    def fetchDataFromRAM(self, pid, addr):
        randdata = random.randint(1,256)
        coreID = self.getProccessHome(pid)
        #SIMULATESTHE DATA HAS BEEN SAVED IN appropriate L1_CACHE of affinity core
        tag = int(addr[0:5], 2)
        set = addr[4:6]
        offset = addr[6:12]
        self.cores[coreID].L1cache[tag] = [addr, "{:08b}".format(randdata) * 64]
        

    def getProccessHome(self, pid):
         for coreID in range(self.noOfCores):
            if pid in self.affinity[coreID]:
                return coreID

    def executionMigration(self, startCore, destCore, pid):
        self.affinity[startCore].remove(pid)
        self.cores[startCore].affinity.remove(pid)
        self.affinity[destCore].add(pid)
        self.cores[destCore].affinity.add(pid)
        

    #This will return the core which the address is stored in the L1 cache
    def getCore(self, addr):
        tag = int(addr[0:5], 2)
        for core in self.cores:
            if core.L1cache[tag][0] == addr:
                return core.id
        return -1


    #This is the cost of execution migration, moving from the process from the
    #start node to destination node to use the data
    #PCBsize is a fixed processblocksize
    def getMigrationCost(self, start, dest):
        PCBsize = self.cores[start].PCB_size #128
        migrCost = abs(dest - start) * PCBsize
        return migrCost

    #This is the access cost of fetching the data from another core and doing a round trip back
    #access is usually 32 bit or 64 bit so it is constant
    def getAccessCost(self, start, dest):
        accessCost = abs(dest - start) * 64 * 2 #because of round trip it is twice as long
        return accessCost


    def kill(self, pid):
        del self.processList[pid]
        coreID = self.getProccessHome(pid) 
        self.cores[coreID].affinity.remove(pid)
        self.affinity.remove(pid)
        print(f"pid {pid} killed.")
        self.CLOCK +=1

    def fetch(self, proccessID):
        '''
        Fetch- is the operation which receives instructions from program memory from a systems RAM.
        '''
        self.CLOCK +=1
        return

    def decode(self, proccessID):
        '''
        Decode- is where the instruction is converted to understand which other parts 
        of the MasterCPU are needed to continue the operation. 
        This is performed by the instruction decoder
        '''
        self.CLOCK +=1
        return


    def nextAvailableNode(self):
        min = 0
        for coreID in range(self.noOfCores):
            if len(self.affinity[coreID]) < len(self.affinity[min]):
                min = coreID
        return min
            


    def execute(self, processID):
        '''
        Execute- is where the operation is performed.
        Each part of the MasterCPU that is needed is activated to carry out the instructions.
        '''
        self.CLOCK +=1
        return

    def store(self):
        '''
        Store: The MasterCPU must give feedback after executing an instruction, 
        and the output data is written to the memory.
        '''
        self.CLOCK +=1

    
    def displayProcesses(self):
        print(self.processList)

