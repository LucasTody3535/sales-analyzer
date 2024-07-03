from random import random

from src.sample.sample import Sample

def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    rol = []
    for i in range(100):
        rol.append(round(random() * 2500))
    rol.sort()
    sample = Sample(rol)
    sample.setup()
    print(sample.show_data_formatted())
