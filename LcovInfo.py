class LcovInfo:
    def __init__(self):
        self.hitLineCount = {}
        self.hitFunctionCount ={}
        self.hitBranch = {}
        self.totalFuncCount = 0
        self.hitFuncNum = 0
    def setTotalFuncCount(self, totalFuncCount):
        self.totalFuncCount = totalFuncCount
    def setHitFucCount(self, hitFuncCount):
        self.hitFuncCount = hitFuncCount
    def addhitLineCount(self, line, count):
        self.hitLineCount[line] = count
    def addHitFunctionCount(self, funcName, count):
        self.hitFunctionCount[funcName] = count
    def addHitBranche(self, line, isExe):
        self.hitBranch[line] = isExe
