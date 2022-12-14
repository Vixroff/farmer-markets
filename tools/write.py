def write(path, data):
    with open(path, 'w') as f:
        for row in data:
            f.write('|'.join(row))
            f.write('\n')
