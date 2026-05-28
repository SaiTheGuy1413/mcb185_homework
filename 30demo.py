import itertools

#for nts in itertools.product('AGTC', repeat = 2):
    #print(nts)

'''d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])'''

def read_catalog(filepath):
    catalog = []
    with open(filepath) as fp:
        for line in fp:
            if line.startswith('#'): continue
            name, length, seq, desc = line.rstrip().split(',')
            record = {
                'Name': name,
                'Length': length,
                'Sequence': seq,
                'Description': desc
            }
            catalog.append(record)
    return catalog


catalog = read_catalog('primers.csv')
for primer in catalog:
    print(primer['Name'], primer['Description'])