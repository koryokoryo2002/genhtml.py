# coding: UTF-8
import re

from LcovInfo import *

class ReadInfoFile:
    def __init__(self):
        self.lcovInfos={}

    def readInfoFile(self, infoFile):
        for line in open(infoFile):
            if re.match("^TN:",line):
                print("TN")
            elif re.match("^[SK]F:",line):		#source name
                srcName = line.split(":")[1]
                if( (srcName in self.lcovInfos) == False):
                    self.lcovInfos[srcName] = LcovInfo()            
            elif re.match("^FNF:",line):		#Func count
                self.lcovInfos[srcName].setTotalFuncCount(line.split(":")[1])
            elif re.match("^FNH:",line):		#Hit Func count
                self.lcovInfos[srcName].setHitFucCount(line.split(":")[1])
            elif re.match("^DA:",line):		#Hit line and count
                tmp = line.split(":")[1]
                self.lcovInfos[srcName].addhitLineCount(tmp.split(",")[0], tmp.split(",")[1])
            elif re.match("^FNDA:",line):		#Hit function
                tmp =  line.split(":")[1]
                self.lcovInfos[srcName].addHitFunctionCount(tmp.split(",")[1], tmp.split(",")[0])
            elif re.match("^BRDA:",line):		#Hit Branch
                tmp =  line.split(":")[1]
                self.lcovInfos[srcName].addHitBranch(tmp.split(",")[0]+"_"+tmp.split(",")[1]+"_"+tmp.split(",")[2], brda_data.split(",")[3])
            elif re.match("end_of_record",line):
                print("end_of_record")
