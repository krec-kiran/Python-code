def string_parse(arr):
    print(arr)
    if type(arr) != str:
        return 'Please enter a valid string'
    result = []
    i = 0
    while i < len(arr):
        element = arr[i]
        if i < len(arr) - 2 and arr[i] == arr[i + 1] == arr[i + 2]:
            value = arr[i] + arr[i + 1]
            i = i + 2
            begin = i
            while i < len(arr) and arr[i] == element:
                i += 1
            text = value + '[' + arr[begin:i] + ']'
            result.append(text)
        else:
            result.append(arr[i])
            i += 1

    return(''.join(result))


print(string_parse("aaaabbcdefffffffg"))
