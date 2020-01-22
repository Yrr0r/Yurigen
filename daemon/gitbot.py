#!/usr/bin/env python3
# coding: utf-8

import os
import sys

def savebranch(path, commitmessage = 'No commit message'):
    pathbefore = os.getcwd()
    os.chdir(path)
    returnmsg = os.popen("git add .").read()
    returnmsg = returnmsg + os.popen("git commit -m \'" + commitmessage + "\'").read()
    os.chdir(pathbefore)
    return returnmsg


path = sys.argv[1]
commitmessage = sys.argv[2]
print(savebranch(path, commitmessage))
