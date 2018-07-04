# Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
# 8kyu


def findFreqLib(source, dest):
    return source.count(dest)


def findFreq(source, dest):
    count = 0
    start = 0
    leng = len(dest)
    end = leng
    for i in range(len(source)):
        if (source[start:end] == dest):
            count += 1
        start += 1
        end = start + leng
    return count


source = "Hello World Hello HelloHe He"
dest = "He"
print("The count is ", findFreq(source, dest))
print("The count from library is", findFreqLib(source, dest))
