import hashlib
import sys


def getInputFile():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            input_text = line.split(',')[0]
            x = line.split(',')[1]
    return input_text, x


def codify(iteration, code, reps, data_hash):
    position = iteration % 32
    if not code[reps].isalpha():
        index = int(code[reps])
        if data_hash[index] == '@':
            data_hash[index] = code[position]


def createHash(input_text, reps, data_hash, val):
    code = '0'
    iteration = 0

    while data_hash.count('@') > 0:
        while(code[:reps] != val):
            iteration += 1
            text = input_text + str(iteration)
            result = hashlib.md5(text.encode())
            code = result.hexdigest()
        codify(iteration, code, reps, data_hash)
        code = '0'
    data_hash_output = ''.join(data_hash)
    dumpOutput(data_hash_output)


def dumpOutput(output):
    f = open(str(sys.argv[1]) + '.answer', 'w')
    f.write(output)


def main():
    input_text, x = getInputFile()
    reps = int(x)
    val = str(''.join(['0'] * reps))
    data_hash = ['@'] * 10

    createHash(input_text, reps, data_hash, val)


if __name__ == "__main__":
    main()
