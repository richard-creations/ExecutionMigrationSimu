from PCB import PCB

class Process:
    
    def __init__(self, pid, exe):
        self.pid = pid
        self.context = PCB()
        self.code = exe
        self.globVars = []
        self.heap = []
        self.stack = []

