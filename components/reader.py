import json


def read_json(path: str):
    with open(path) as f:
        d = json.load(f)
    return d


def parse_parameters(d: dict):
    all_data = d["parameters"]
    n_per_seed = all_data["rndnumbersPerSeed"]
    seeds = all_data["seeds"]
    arrivals = all_data["arrivals"]
    queues = all_data["queues"]
    network = all_data["network"]

    return [n_per_seed, seeds, arrivals, queues, network]


def read_n_parse(path: str):
    return parse_parameters(read_json(path))
