import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        neos = []
        for row in reader:
            neo = NearEarthObject(
                designation=row.get('pdes', ''),
                name=row.get('name', ''),
                diameter=row.get('diameter', ''),
                hazardous=row.get('pha', 'N')
            )
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as file:
        data = json.load(file)
        approaches = []
        for entry in data['data']:
            approach = CloseApproach(
                designation=entry[0],
                time=entry[3],
                distance=entry[4],
                velocity=entry[7]
            )
            approaches.append(approach)
    return approaches
