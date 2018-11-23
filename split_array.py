def partition(k, classifier_method):
    x = list(filter((lambda x: classifier_method(x)), k))
    y = list(filter((lambda x: not classifier_method(x)), k))
    return(x, y)


print(partition(func, animals))
