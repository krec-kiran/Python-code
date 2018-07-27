def count_smileys(smiles):
    eyes = [':', ';']
    mouth = [')', 'D']
    nose = ['-', '~']

    count = 0
    for i in smiles:
        face = list(i)
        if len(face) > 2:
            if face[0] in eyes and face[1] in nose and face[2] in mouth:
                count += 1
        if len(face) <= 2:
            if face[0] in eyes and face[1] in mouth:
                count += 1
    return(count)


smiles = [':)', ':(', ':D', ':O', ':;']
print(count_smileys(smiles))
