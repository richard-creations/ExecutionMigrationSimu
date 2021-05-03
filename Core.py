
from Process import Process

class Core:

    def __init__(self, id, cacheSize_B = 32, processSize_nm = 180):
        self.id = id
        self.L1cacheSize_KB = cacheSize_B #cache size in bytes
        self.processSize_nm = processSize_nm
        self.L1cache = [0]*cacheSize_B    #cache data structure
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


    def displayProcesses(self):
        print(self.processList)
