
from Process import Process
import random

class Core:

    def __init__(self, id, cacheSize_B = 32, PCB_size = 128):
        self.id = id
        self.cacheSize_B = cacheSize_B #cache size in bytes
        self.PCB_size = PCB_size
        self.L1cache = [[0],['00000000' * 64]]*cacheSize_B    #cache data structure
        self.affinity = []
        self.procs = []
        self.currentExecution = -1


        #CREATES RANDOM DATA TO STORE IN THE CACHE


        '''
        for tag in range(cacheSize_B):
            randdata = random.randint(1,10000)
            randAddress = random.randint(10, 32000)
            self.L1cache[tag] = "{0:b}".format(randAddress)+":"+"{0:b}".format(randdata) * 64
        
        #set known target address for just core 1: (used in testing)
        if (id == 1):
            self.L1cache[int(cacheSize_B/2)] = "{0:b}".format(31) +":"+"{0:b}".format(random.randint(1,10000)) * 64
        '''
    def status(self):
        output = "CORE ID: " + str(self.id) + "\n"
        output += "Number of proccesses: " + str(len(self.affinity)) + "\n"
        '''
        if self.currentExecution == -1:
            output += "Current Proccess Execution: None"
        else:
            output += "Current Proccess Execution: " + str(self.currentExecution) + "\n"
            output += "-------------"
        '''
        return output


    def displayProcesses(self):
        print(f"Affinity proccesses for core {self.id}:")
        print(self.affinity)

