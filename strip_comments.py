import io

text = "apples, pears # and bananas\ngrapes\nbananas !apples"
buf = io.StringIO(text)
line = buf.readline()
while(line):
    line = line.split()
    print(line)
    markers = ["#", "!"]

    for pos in range(len(line)):
        if line[pos] in markers:
            print("Pos:", pos)
            subtext = line[:pos]
            print("subtext", subtext)
    line = buf.readline()

s = 'Hello word Kiran'

k = list(s)
print(k)
p = ''.join(k)
print(p)
