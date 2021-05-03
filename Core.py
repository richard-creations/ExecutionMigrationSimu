
from Process import Process

class Core:

    def __init__(self, id, cacheSize_B = 32, processSize_nm = 180):
        self.id = id
        self.cacheSize_KB = cacheSize_B #cache size in bytes
        self.processSize_nm = processSize_nm
        self.cache = [0]*cacheSize_B    #cache data structure
        self.processList = []
        self.currentExecution = -1
        self.CLOCK = 0
        
    def status(self):
    

        output = "CORE ID: " + str(self.id) + "\n"
        output += "Number of proccesses: " + str(len(self.processList)) + "\n"
        if self.currentExecution == -1:
            output += "Current Proccess Execution: None"
        else:
            output += "Current Proccess Execution: " + str(self.currentExecution) + "\n"
            output += "-------------"
        return output


    def createProcess(self):
        self.processList.append(Process(len(self.processList), "load 1"))
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
