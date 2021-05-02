

class PCB:
    def __init__(self,  pointer, processState, processNo, priority):
        self.pointer = pointer
        self.counter = 0
        self.processState = processState
        self.processNo = processNo
        self.priority = priority
        self.registers = {'AH':0,'AL':0,'CH':0,'CL':0, 'DH':0,'DL':0,'BH':0,'BL':0,'SPL':0, 'BPL':0, 'SIL':0, 'DIL':0}
        self.listOfOpenFiles = [] 
        self.listOfOpenDevices = [] 