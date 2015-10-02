
class LcovInfo:
    def __init__(self):
        self.lineExeCount = {}
        self.functionExeCount ={}
        self.branchExe = {}
    def addLineExeCount(self, line, count):
        self.lineExeCount[line] = count
    def addFunctionExeCount(self, funcName, count):
        self.functionExeCount[funcName] = count
    def addBranchExe(self, line, isExe):
        self.branchExe[line] = isExe
        print(line)
