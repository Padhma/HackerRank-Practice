def split_and_join(line):
    splitString = line.split(' ')
    return '-'.join(splitString)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)