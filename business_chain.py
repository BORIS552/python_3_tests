import fileinput
from collections import defaultdict

class Business(object):

    def __init__(self, name, location, id):
        self.name = name
        self.location = location
        self.id = id

class Chain(object):

    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

def detect_and_order_chain_businesses(businesses, location):
    chainData = {}
    for item in businesses:
        name,location,id = item.name,item.location,item.id
        if location == targetLocation:
            if name+'-'+str(id) in chainData.keys():
                chainData[name+'-'+str(id)].freq+=1
            else:
                chainData[name+'-'+str(id)]=Chain(name,1)
    return [(v.name,v.freq) for v in sorted(chainData.values(),key = lambda x: (x.freq,x.name))]

def parse_stdin_and_get_input():
    lines = [line.strip() for line in list(fileinput.input())]
    businesses = []
    target_location = lines[-1]

    for line in lines[:-1]:
        name, location, id = line.split(' - ')
        businesses.append(Business(name, location, id))

    return businesses, target_location

if __name__ == '__main__':
    businesses, location = parse_stdin_and_get_input()

    chains = \
        detect_and_order_chain_businesses(businesses, location)

    for chain in chains:
        print('{} - {}'.format(chain.name, chain.frequency))