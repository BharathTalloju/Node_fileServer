#!/usr/bin/python

import subprocess
from json_lib import *

commands_file = 'private/commands.json'

def getCommands():
    with open(commands_file) as f:
        buff = f.read()
        print "Read", buff
        commands_dict = validateAndCreateJson(buff)

    return commands_dict

commands = getCommands()
subprocess.Popen(commands["start_receiver"])

while True:
    cmd = raw_input('>').strip().split()
    if len(cmd) == 0:
        continue
    if len(cmd) == 1:
        subprocess.Popen(commands[cmd[0]])
        continue

    subprocess.Popen(commands[cmd[0]])