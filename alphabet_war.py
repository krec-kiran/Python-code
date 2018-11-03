def alphabet_war(fight):
    leftSide = ['1', 's', 'b', 'p', 'w']
    rightSide = ['1', 'z', 'd', 'q', 'm']
    leftCount = 0
    rightCount = 0
    for i in fight:
        if i in leftSide:
            leftCount += leftSide.index(i)
        if i in rightSide:
            rightCount += rightSide.index(i)
    if leftCount > rightCount:
        return('Left side wins!')
    elif rightCount > leftCount:
        return('Right side wins!')
    else:
        return('Let\'s fight again!')


print(alphabet_war('zdqmwpbs'))
print(alphabet_war('wwwwww'))
print(alphabet_war('zzzzs'))
