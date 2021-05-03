from PCB import PCB

class Process:
    
    def __init__(self, pid, exe, parentID=0):
        self.pid = pid
        self.programCount = 0
        self.context = PCB(pid)
        self.code = exe
        self.globVars = []
        self.heap = []
        self.stack = []
        self.children = []
        self.parentID = parentID

