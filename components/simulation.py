# Imports
from .preprocess import preprocess
from .logger import logger
import simpy
###
global queues
global QUEUES_AUX
global LOST
global SERVED

LOST = 0
SERVED = 0
SIM_TIME = 200


env = simpy.Environment()
path = 'data/data.json'

data = preprocess(path)
MY_RANDOM_NUMBERS = data[3]


class Queue(object):
    def __init__(self, env, name, num_machines, minS, maxS, minA=0, maxA=1, capacity=1000, on_line=0, destiny=False):
        self.env = env
        self.name = name
        self.machine = simpy.Resource(env, num_machines)
        self.capacity = capacity
        self.on_line = on_line
        self.minS = minS
        self.maxS = maxS
        self.minA = minA
        self.maxA = maxA
        self.duration_task = 0
        self.destiny = destiny

    def do_task(self, aux_entity):
        global SERVED
        self.on_line -= 1
        self.duration_task = MY_RANDOM_NUMBERS.pop() * (self.maxS - self.minS) + self.minS
        # The simulation makes the self.duration_task change depending on env.now. So we call it only once and store it on aux to make things sturdy.
        aux_duration_task = self.duration_task
        print(logger("Serving", aux_entity, self.name, env.now, aux_duration_task))
        yield self.env.timeout(aux_duration_task)
        print(logger("Served", aux_entity, self.name, env.now, aux_duration_task))

        if self.destiny:
            env.process(self.to_destiny(aux_entity))
        else:
            SERVED += 1

    def to_destiny(self, aux_entity):
        global SERVED
        served = True
        # This yield is necessary, why? Don't really know.
        yield self.env.timeout(0)
        for network in data[2]:
            if network["source"] == self.name:
                if MY_RANDOM_NUMBERS.pop() <= network["probability"]:
                    for queue in QUEUES_AUX:
                        if queue.name == network["target"]:
                            env.process(redirect(env, aux_entity, queue))
                            served = False
                    break
        if served:
            SERVED += 1


def redirect(env, name, task):
    global LOST
    if task.on_line == task.capacity:
        print(logger("LostRedirect", name, task.name))
        LOST += 1
    else:
        print("{0} REDIRECTED TO {1}".format(name, task.name))
        task.on_line += 1
        with task.machine.request() as request:
            yield request
            yield env.process(task.do_task(name))


def entity(env, name, task):
    global LOST
    print(logger("Arrive", name, env.now))
    with task.machine.request() as request:
        yield request
        # Dealing with capacity
        if task.on_line == task.capacity:
            print(logger("Lost", name, task.name))
            LOST += 1
        else:
            task.on_line += 1
            print(logger("Enter", name, task.name, env.now))
            yield env.process(task.do_task(name))
            print(logger("Left", name, task.name, env.now))


def setup(env, data):
    global QUEUES_AUX
    global LOST
    # Queues
    QUEUES_AUX = []
    for i, queue in enumerate(data[0]):
        aux_queue = data[0][i]
        destiny = False
        for network in data[2]:
            if queue["name"] == network["source"]:
                destiny = True
        if len(aux_queue) > 5:
            q = Queue(env=env, name=aux_queue["name"], num_machines=aux_queue["servers"],
                      minS=aux_queue["minService"], maxS=aux_queue["maxService"],
                      minA=aux_queue["minArrival"], maxA=aux_queue["maxArrival"],
                      capacity=aux_queue["capacity"], destiny=destiny)
        else:
            q = Queue(env=env, name=aux_queue["name"], num_machines=aux_queue["servers"],
                      minS=aux_queue["minService"], maxS=aux_queue["maxService"],
                      capacity=aux_queue["capacity"], destiny=destiny)
        QUEUES_AUX.append(q)

    # Arrivals
    counter = 0
    LOST = 0
    for arrival in data[1]:
        for queue in QUEUES_AUX:
            if queue.name == arrival[0]:
                counter += 1
                env.process(entity(env, "ENTITY {}".format(counter), queue))

    # Simulation
    while True:
        for arrival in data[1]:
            for queue in QUEUES_AUX:
                if queue.name == arrival[0]:
                    if queue.on_line == queue.capacity:
                        counter += 1
                        LOST += 1
                        print(logger("Lost", counter, queue.name))
                    else:
                        yield env.timeout(MY_RANDOM_NUMBERS.pop() * (queue.maxA - queue.minA) + queue.minA)
                        counter += 1
                        env.process(
                            entity(env, "ENTITY {}".format(counter), queue))


def start():
    env.process(setup(env, data))
    # Execute the simulation!
    env.run(until=SIM_TIME)
    print("LOST: {}".format(LOST))
    print("SERVED: {}".format(SERVED))
