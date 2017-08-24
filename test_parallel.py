from multiprocessing import Pool
import numpy as np

def foo(x, y, z):
    np.tanh(np.random.random(100000000))
    print x, y, z


def wrap(args):
    return foo(*args)

pool = Pool()

args = [('my', 'first', 'parallel'), ('program', 'in', 'python')]

pool.map(wrap, args)
