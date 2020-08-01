# coding: UTF-8
import sys
from readInfoFile import *

argv = sys.argv
argc = len(sys.argv)

if(argc != 2):
    print ("arg error")
    quit()

readInfoFile = ReadInfoFile()
readInfoFile.readInfoFile(argv[1])

