from typing import Dict
from node import Node as N
from connection import Connection as C

ND = {
    'S': N('S'),
    'R1': N('R1'),
    'R2': N('R2'),
    'R3': N('R3'),
    'A': N('A'),
    'B': N('B'),
    'C': N('C'),
    'D': N('D')
}

network = N('S', C(C=10.000, T=0.1, ))

def main():
    ND['S'].print_network()

if __name__ == '__main__':
    main()