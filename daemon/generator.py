#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import configparser

"""
This generator applet calls the generator for a directory.
"""

# CONFIG_FILE_NAME is defined on mutiple files
CONFIG_FILE_NAME = 'yurisora.ini'

#chdir to the root and then run command.
def callgen(path, command):
    pathbefore = os.getcwd()
    os.chdir(path)
    try:
        result = os.popen(command).read()
    except:
        result = "Build Error"
    
    os.chdir(pathbefore)
    return result

def useconf(path):
    pathbefore = os.getcwd()
    os.chdir(path)
    if (os.path.isfile(CONFIG_FILE_NAME) == False):
        return 'Error: No Config'
    else:
        try:
            config = configparser.ConfigParser()
            config.read(CONFIG_FILE_NAME)
            command = config['generator']['generator']
        except:
            return 'Error: Bad Config'
        
        return(callgen(path, command))

    os.chdir(pathbefore)


path = sys.argv[1]
print(useconf(path))
