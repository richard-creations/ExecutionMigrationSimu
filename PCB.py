

class PCB:
    def __init__(self,  pointer, processState, 
    processNo, priority):
        self.pointer = pointer
        self.processState = processState
        self.processNo = processNo
        self.priority = priority
        self.registers = []
        self.listOfOpenFiles = [] 
        self.listOfOpenDevices = [] 