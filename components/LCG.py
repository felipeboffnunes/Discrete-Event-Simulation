import numpy as np

def congruent_linear_generator(a : int, m : int, c : int, x0 : int):
    """
    :def: Linear Congruent Generator Technique
    : Method to generate pseudo-randoms
    :
    :param a:  Random Parameter
    :type a:   int
    :param c:  Constant used to create bigger variation of generated numbers
    :type c:   int
    :param m:  Parameter which determines the biggest value generated 
    :type m:   int
    :param x0: Determines initial seed and stop trigger
    :type x0:  int
    :return:   Pseudo-random list of numbers 
    :rtype:    list[int]
    """
    return (a*x0 + c)%m


def give_me_n_random(RANGE:int, SEED:int, a:int=44, m:int=95784, c:int=4565):
    pseudo_random = [SEED]
    for _ in range(RANGE):
        pseudo_random.append(congruent_linear_generator(a, m, c, pseudo_random[-1]))

    MIN = min(pseudo_random)
    MAX = max(pseudo_random)

    def percentage(MIN, MAX, value):
        return round(((value - MIN)/(MAX - MIN)),2)

    return [percentage(MIN, MAX, x) for x in pseudo_random][1:]
