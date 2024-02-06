# from bigread import Reader

# stream = Reader(file='large.txt', block_size=10)


with open('variables.txt') as file:
    data = file.readlines()
    entities = []
    for record in data:
        di = {}
        record = record.strip()
        if '----' in record:
            continue
        each = record.split(":")
        each[0] = each[0].strip()
        each[1] = each[1].strip()
        if each[0] in ['Entity', 'Attributes', 'Values', 'Datatype']:
            di[each[0]] = [each for each in each[1].split(",")]
            entities.append(di)
    print(entities)
