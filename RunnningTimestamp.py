import time

def GetLogTimestamp():
    # Get current timestamp
    strTimestamp = time.time()
    print("Current Timestamp = ", strTimestamp)

    # Write timestamp to log file
    f = open("log/RunnningTimestamp.log", "w")
    f.write("Current Timestamp = %s\n" % (strTimestamp))
    f.close()