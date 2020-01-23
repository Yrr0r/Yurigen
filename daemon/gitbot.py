#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import configparser

from database import sql

"""
This gitbot script attempts to submit all changes to a directory.
"""

# CONFIG_FILE_NAME is defined on mutiple files
CONFIG_FILE_NAME = 'yurisora.ini'


def gitsubmit(path, commitmessage = 'Automated commit'):
    pathbefore = os.getcwd()
    os.chdir(path)
    returnmsg = os.popen("git add .").read()
    returnmsg = returnmsg + os.popen("git commit -m \'" + commitmessage + "\'").read()
    os.chdir(pathbefore)
    return returnmsg

def gitpush(path, giturl, username, token):
    passstring = username + ':' + token
    cmdstring = 'git push https://' + passstring + '@' + giturl 
    returnmsg = os.popen(cmdstring).read()
    return returnmsg

def autogit(path):
    pathbefore = os.getcwd()
    os.chdir(path)
    #first get userid and url
    config = configparser.ConfigParser()
    if (config.read(CONFIG_FILE_NAME)) == [] :
        return 'Config error'
    url = config['git']['repo']
    userid = config['git']['userid']
    authorname = config['info']['author_name']
    #then get token:
    token = sql.gettoken(authorname)
    if(token == ''): return "User does not exist!"
    #then do all the work
    result = gitsubmit(path) # 未来加入commit_message功能
    result = result + gitpush(path, url, userid, token)

    os.chdir(pathbefore)
    return result


path = sys.argv[1]
print(autogit(path))
