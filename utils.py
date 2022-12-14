def get_fields(path):
    with open(path, 'r') as f:
        fields = f.readline().strip().split(',')
    return fields
