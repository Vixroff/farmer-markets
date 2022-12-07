import csv 


def read(path):
    result = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            result.append(row)
    return result
 

def get_fields(path):
    with open(path, 'r') as f:
        fields = f.readline()
    return fields.split(',')