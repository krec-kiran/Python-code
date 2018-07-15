def work_needed(projectMinutes, freelancers):
    total = 0
    for i in freelancers:
        hrs, min = i
        total += hrs * 60 + min

    projectMinutes -= total
    if projectMinutes < 0:
        return('Easy Money!')
    hrs = int(projectMinutes / 60)
    mins = projectMinutes % 60
    if hrs or mins:
        message = ("I need to work %d hour(s) and %d minute(s)" % (hrs, mins))
    else:
        message = "Easy Money!"
    return(message)


print(work_needed(141, [(1, 55), (0, 25)]))
