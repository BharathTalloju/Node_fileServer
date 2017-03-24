import subprocess
from serverLog import *
commands_file = 'private/commands'

def getCommands():
    commands_dict = None
    with open(commands_file) as f:
        commands_dict = dict(f.read())

    return commands_dict

commands = getCommands()

while True:
    cmd = raw_input('>').strip().split()
    if len(cmd) == 0:
        continue
    if len(cmd) == 1:
        subprocess.Popen(commands[cmd])
    cmd, args = cmd[0], cmd[1:]
    writeToLog(serverLogFilename, __name__ + ": Spawning" + cmd[0])
    subprocess.Popen(cmd)