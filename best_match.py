# "AL-AHLY" and "Zamalek" are the best teams in Egypt, but "AL-AHLY" always wins the matches between them. "Zamalek" managers want to know what is the best match they've played so far.
#
# The best match is the match they lost with the minimum goal difference. If there is more than one match with the same difference, choose the one "Zamalek" scored more goals in.
#
# Given the information about all matches they played, return the index of the best match (0-based). If more than one valid result, return the smallest index.
#
# Example
# For ALAHLYGoals = [6,4] and zamalekGoals = [1,2], the output should be 1.


def best_match(a, z):
    slots = []
    diff = [x - y for x, y in zip(a, z)]
    if diff.count(min(diff)) > 1:
        for i in range(len(diff)):
            if diff[i] == min(diff):
                slots.append(i)
        most = [z[x] for x in slots]
        match = list(zip(slots, most))
        goals = [x[1] for x in match]
        x = [item[0] for item in match if item[1] == max(goals)]
        return(x[0])
    else:
        return(diff.index(min(diff)))
