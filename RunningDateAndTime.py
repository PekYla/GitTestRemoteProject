import datetime

def GetLogDataTime():
    # Get current date and time
    strDateTime = datetime.datetime.now()
    print("Current date and time = ", strDateTime)

    # Write date and time to log file
    f = open("log/RunningDateAndTime.log", "w")
    f.write("Current date and time = %s\n" % (strDateTime))
    f.close()