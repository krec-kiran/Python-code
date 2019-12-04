def extractInput(file):
    with open(file, 'r') as f:
        coords = []
        for line in f:
            k = line.split(',')
            for i in k:
                if i != '\n':
                    coords.append(i)
    return (','.join(coords)).strip('\n')
