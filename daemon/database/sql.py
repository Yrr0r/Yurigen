#!/usr/bin/env python3
# coding: utf-8

import sqlite3
import atexit
import os,sys

DB_FILE = '/home/yrr0r_g/pass.db'

conn = sqlite3.connect(DB_FILE, uri=True)

# get token by github author's name:
def gettoken(username):
    c = conn.cursor()
    cmdstring = "SELECT github_token FROM gitcredentials WHERE name = \'" + username +"\'"
    dbout = c.execute(cmdstring).fetchall()
    if(not dbout): return ''
    if(not dbout[0]): return ''
    return dbout[0][0]
