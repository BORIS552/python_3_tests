import json
import sys
from typing import Iterable
from typing import List
from typing import NamedTuple


class Interaction(NamedTuple):
    """ A single interaction with a business """
    interaction_type: str  # type of interaction with the business, one of the keys of WEIGHTS below
    business_id: int  # a business id, can be any int

# a weight for each interaction_type
WEIGHTS = {
    'review draft': 2.0,
    'photo': 1.0,
    'check-in': 0.8,
    'bookmark': 0.25,
}


def interactions_to_sorted_businesses(interactions: Iterable[Interaction]) -> List[int]:
    print(interactions)
    dict = {}
    for ini in interactions:
        dict[ini.business_id] = 0

    for it in interactions:
        dict[it.business_id] = dict[it.business_id]+WEIGHTS[it.interaction_type]
    
    new_dict = {}
    new_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return new_dict
    #print(sorted(dict.items(), key=lambda item: item[1]))


def main():
    """ Parses input from stdin and dumps output to stdout """
    f = open('data.json')
    input_json = json.load(f)
    interactions = [
        Interaction(
            interaction_type=interaction['interaction_type'],
            business_id=interaction['business_id'],
        )
        for interaction in input_json
    ]
    sorted_businesses = interactions_to_sorted_businesses(interactions)

    for business_id in sorted_businesses:
        print(business_id)


if __name__ == '__main__':
    main()