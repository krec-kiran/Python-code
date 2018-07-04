def format_duration(time):
    hrs = 0
    min = 0
    if time == 0:
        print('now')
    while(time > 60):
        if time >= 3600:
            hrs = int(time / 3600)
            time = int(time % 3600)
        elif time > 60 and time < 3600:
            min = int(time / 60)
            time = int(time % 60)
    if (hrs and min == 0 and time == 0):
        print("Time is %d hour(s)" % hrs)
    if (hrs and min and time):
        print("Time is %d hour(s), %d minute(s) and %d second(s) " %
              (hrs, min, time))
    if (hrs and min != 0):
        print("Time is %d hour(s) and %d min(s)" % (hrs, min))
    if (hrs and time != 0):
        print("Time is %d hour(s) and %d sec(s)" % (hrs, time))
    elif(min and time != 0):
        print("Time is %d minute(s) and %d second(s) " %
              (min, time))
    elif(min and time == 0):
        print("Time is %d minute(s)" %
              min)
    elif(hrs == 0 and min == 0):
        print("Time is %d second(s) " %
              (time))


format_duration(7202)
