#!/usr/bin/python2

from time import gmtime, strftime

serverLogFilename = "server_debug.log"

def writeToLog(fileName, data):
    """
    function to maintain log for debugging
    :param fileName: name of the log file
    :param data: data to be written in string format
    :return: None
    """
    with open(fileName,'a') as logFile:
        logFile.write( "\n" + strftime("%Y-%m-%d %H:%M:%S ", gmtime()) + ":\t" + data)
        return

#No other file to place it
def writeToFile(filename, data):
    """Writes data to file"""

    try:
        with open(filename, "w") as f:
            f.write(data)
    except Exception as err:
        writeToLog(serverLogFilename, "Error writing to " + filename)
