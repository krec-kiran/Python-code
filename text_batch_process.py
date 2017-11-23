def stream_docs(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            label, text = line[0:12], line[15:]
            yield text, label


doc_stream = stream_docs("music.txt")

# t, l = next(doc_stream)

# print("l:", l, "\nt", t)


def get_mini_batch(doc_stream, size):
    docs, y = [], []
    try:
        for _ in range(size):
            text, label = next(doc_stream)
            docs.append(text)
            y.append(label)
    except StopIteration:
        return None, None
    return docs, y

for _ in range(100):
    X_train, y_train = get_mini_batch(doc_stream, 3)
    if not X_train:
        break
    print('X_train,y_train=', X_train, y_train)
