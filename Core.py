
class Core:

    def __init__(self, id, clockSpeed, cacheSize_B = 32, processSize_nm = 180, noOfProccesses= 1):
        self.id = id
        self.clockSpeed = clockSpeed
        self.cacheSize_KB = cacheSize_B #cache size in bytes
        self.processSize_nm = processSize_nm
        self.cache = [0]*cacheSize_B  #cache data structure
        self.noOfProccesses = noOfProccesses
        



    def fetch(self, proccessID):
        '''
        Fetch- is the operation which receives instructions from program memory from a systems RAM.
        '''
        return

    def decode(self, proccessID):
        '''
        Decode- is where the instruction is converted to understand which other parts 
        of the CPU are needed to continue the operation. 
        This is performed by the instruction decoder
        '''
        return
    


    def execute(self, processID):
        '''
        Execute- is where the operation is performed.
        Each part of the CPU that is needed is activated to carry out the instructions.
        '''
        return

    def store(self):
        '''
        Store: The CPU must give feedback after executing an instruction, 
        and the output data is written to the memory.
        '''