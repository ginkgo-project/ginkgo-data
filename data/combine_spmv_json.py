import json
import sys
from glob import glob

def combine_json(folder, output, properties):
    alljson = glob(folder + '/*/*.json')
    data=[]
    for name in alljson:
        with open(name, 'r') as f:
            temp = json.load(f)
        for item in temp:
            select = dict()
            for p in properties:
                select[p] = item[p]
            data.append(select)
    with open(output, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    if (len(sys.argv)) < 3:
        print("Usage:" + sys.argv[0] + "<FOLDER> <OUTPUT>")
        sys.exit(1)
    FOLDER=sys.argv[1]
    OUTPUT=sys.argv[2]
    PROPERTIES=['filename', 'problem', 'coo', 'csr', 'ell', 'sellp', 'hybrid']
    combine_json(FOLDER, OUTPUT, PROPERTIES)