import Core as Core
import Process as Process

class CPU:

    def __init__(self, noOfCores=4, L1CacheSize = '32', L2cacheSize = 32):
        self.noOfCores = noOfCores
        self.L1cacheSize = L1CacheSize
        self.L2cacheSize = L2cacheSize
        self.cores = []
        self.L2cache = [0] *  L2cacheSize
        self.processList = []
        self.currentExecution = -1
        self.RAM = open('ram.txt') #USING TEXT FILE AS RAM DATA
        self.registers = {'AH':0,'AL':0,'CH':0,'CL':0, 'DH':0,'DL':0,'BH':0,'BL':0,'SPL':0, 'BPL':0, 'SIL':0, 'DIL':0}

        if not L1CacheSize.isdigit():
            for coreID in range(noOfCores):
                self.cores.append(Core(coreID))

        elif L1CacheSize.isdigit():
            cSize = int(L1CacheSize)
            for coreID in range(noOfCores):
                self.cores.append(Core(coreID, cSize))

        
    def createProcess(self, parentID = 0):
        self.processList.append(Process(len(self.processList), "load 1", parentID))
        print(f"Process with PID {len(self.processList)} created at core {self.id}")
        self.CLOCK +=1

    def killProcess(self, pid):
        del self.processList[pid]
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
        of the CPU are needed to continue the operation. 
        This is performed by the instruction decoder
        '''
        self.CLOCK +=1
        return



    def execute(self, processID):
        '''
        Execute- is where the operation is performed.
        Each part of the CPU that is needed is activated to carry out the instructions.
        '''
        self.CLOCK +=1
        return

    def store(self):
        '''
        Store: The CPU must give feedback after executing an instruction, 
        and the output data is written to the memory.
        '''
        self.CLOCK +=1

    
    def displayProcesses(self):
        print(self.processList)

