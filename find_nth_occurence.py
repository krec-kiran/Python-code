string = "TestTestTestTest"
word = 'TestTest'


def find_nth_occurrence(substring, string, occurrence=1):
    end = len(string)
    start = 0
    for i in range(occurrence):
        index = string.find(substring, start, end)
        start = index + 1
    return index


print(find_nth_occurrence(word, string, 1))
print(find_nth_occurrence(word, string, 2))
print(find_nth_occurrence(word, string, 3))
print(find_nth_occurrence(word, string, 4))
