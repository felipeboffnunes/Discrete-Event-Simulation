from .reader import read_n_parse
from .LCG import give_me_n_random

# Coupling Data
def preprocess(path):
    # Parsing
    data_dict = read_n_parse(path)
    # Data Dictionary Structure:
    # |  Number os Seeds  | Seeds | Arrivals | Queues | Network |
    # | rndnumbersPerSeed | seeds | arrivals | queues | network |
    # |        int        |  int  |   dict   |  dict  |  dict   |
    ###
    return get_queues(data_dict), get_arrivals(data_dict), get_networks(data_dict), get_randoms(data_dict)
##


def get_randoms(data_dict):
    # Acquiring pseudo-randoms with LCG
    return give_me_n_random(data_dict[0], data_dict[1])


# System Information
# Setup Queues
# Queue Structure:
# (With Arrival set)
# | Name | Num Machines | Capacity | Min Arrival | Max Arrival | Min Service | Max Service |
# | name | num_machines | capacity |    minA     |     maxA    |     minS    |     maxS    |
# (Without Arrival set)
# | Name | Num Machines | Min Service | Max Service |
def get_queues(data_dict):
    queues = []
    for queue in data_dict[3]:
        aux_queue = data_dict[3][queue]
        aux_queue["name"] = queue
        if len(aux_queue) > 5:
            queue_data = \
                name, num_machines, capacity, minA, maxA, minS, maxS = aux_queue
            queues.append(queue_data)
        else:
            queue_data = \
                name, num_machines, capacity, minS, maxS = aux_queue
            queues.append(queue_data)
    return queues

##
# Setup Arrival
# Question: Initial Arrival means number of entities which the system will simulate?
# Arrival Structure:
# |  Name   | Entities Amount |
# | arrival | entities_amount |
def get_arrivals(data_dict):
    arrivals = []
    for arrival in data_dict[2]:
        entities_amount = data_dict[2][arrival]
        arrival_data = arrival, entities_amount
        arrivals.append(arrival_data)
    return arrivals
##
# Setup Network
# Network Structure:
# | Source | Target | Probability |
# | source | target | probability |


def get_networks(data_dict):
    networks = []
    for network in data_dict[4]:
        aux_network = data_dict[4][network]
        network_data = \
            source, target, probability = aux_network
        networks.append(network_data)
    return networks
