# bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")

s = "_nnnnnnn_n__n______nn__nn_nnn"
bump = 0
for i in s:
    if i == 'n':
        bump += 1
    if bump > 15:
        print('Car dead')
if bump < 15:
    print('Wohoo...')
