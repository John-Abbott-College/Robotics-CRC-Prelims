### Master of the mind (100 points) ###
import random

def solve(verif_function):
    # a small helper to let you know how to call the function
    for i in range(20):
        print(verif_function([random.choice(['/', '#', '=', '+', '-', '*']) for _ in range(4)]))
    