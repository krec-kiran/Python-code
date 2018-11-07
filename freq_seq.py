
def freq_seq(s, sep):
    result = ''
    for i in s:
        result += str(s.count(i)) + sep
    return(result.strip(sep))


print(freq_seq('hello world', '-'))
