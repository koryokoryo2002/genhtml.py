# coding: UTF-8
import sys
import re

from LcovInfo import *

def readInfoFile(infoFile):
    for line in open(infoFile):
        if re.match("^TN:",line):
            print("TN")
        elif re.match("^[SK]F:",line):
            srcName = line.split(":")[1]
            if( (srcName in lcovInfos) == False):
                lcovInfos[srcName] = LcovInfo()            
        elif re.match("^DA:",line):
            da_data = line.split(":")[1]
            lcovInfos[srcName].addLineExeCount(da_data.split(",")[0], da_data.split(",")[1])
        elif re.match("^FNDA:",line):
            fnda_data =  line.split(":")[1]
            lcovInfos[srcName].addFunctionExeCount(fnda_data.split(",")[1], fnda_data.split(",")[0])
        elif re.match("^BRDA:",line):
            brda_data =  line.split(":")[1]
            lcovInfos[srcName].addBranchExe(brda_data.split(",")[0]+"_"+brda_data.split(",")[1]+"_"+brda_data.split(",")[2]
                                            , brda_data.split(",")[3])
        elif re.match("end_of_record",line):
            print("end_of_record")


argv = sys.argv
argc = len(sys.argv)

lcovInfos={}

if(argc != 2):
    print ("arg error")
    quit()

readInfoFile(argv[1])

