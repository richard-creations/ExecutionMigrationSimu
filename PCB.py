'''
PCB Block contains information about the context of a proccess. When the scheduler switches to run another process
the conexte of the last running context is aved here to resume execution effectively later
'''

class PCB:
    def __init__(self,  processNo, priority=1, pointer =0, processState = 'r'):
        self.pointer = pointer
        self.counter = 0
        self.processState = processState
        self.processNo = processNo
        self.priority = priority
        self.registers = {'AH':0,'AL':0,'CH':0,'CL':0, 'DH':0,'DL':0,'BH':0,'BL':0,'SPL':0, 'BPL':0, 'SIL':0, 'DIL':0}
        self.listOfOpenFiles = [] 
        self.listOfOpenDevices = [] 