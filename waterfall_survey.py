names = ["Redhead 3", "Gadwall  1", "Smew 4", "Greater Scaup 10",
         "Redhead 3", "Gadwall 9", "Greater Scaup  15", "Common Eider 6"]

# ["COMEID", 6, "GADWAL", 10, "GRESCA", 25, "REDHEA", 6, "SMEW", 4]


def encode(name):
    code = ''
    if len(name) == 1:
        code = name[0][:6].upper()
    if len(name) == 2:
        code = name[0][:3].upper() + name[1][:3].upper()
    if len(name) == 3:
        code = name[0][:2].upper() + name[0][:2].upper() + name[0][:2].upper()
    if len(name) == 4:
        code = name[0][:1].upper() + name[1][:1].upper() + \
            name[2][:2].upper() + name[3][:2].upper()

    return(code)


def create_report(names):
    bird_dictionary = dict()
    for results in names:
        bird_name = results.split()[:-1]
        for birdie in range(len(bird_name)):
            if '-' in bird_name[birdie]:
                bird_name[birdie] = bird_name[birdie].replace('-', ' ')
        if 'Labrador' in bird_name:
            return ['Disqualified data']
        code = encode(bird_name)
        bird_count = ''.join(results.split()[-1:])
        count = int((bird_count))
        if code not in bird_dictionary.keys():
            bird_dictionary[code] = int(bird_count)
        else:
            bird_dictionary[code] += int(bird_count)
    survey = []
    for k in sorted(bird_dictionary):
        survey.append(k)
        survey.append(bird_dictionary[k])
    return survey


print(create_report(names))
