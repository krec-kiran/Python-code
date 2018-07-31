dicts = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
]


def sentence(List):
    super_dict = dict()
    for d in List:
        for k, v in d.items():
            super_dict[int(k)] = v

    sorted_keys = sorted(super_dict)

    text = ''
    for k in sorted_keys:
        text += ' ' + super_dict[k]
    text = text.strip()
    return(text)


print(sentence(dicts))
