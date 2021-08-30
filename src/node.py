from typing import Dict
from connection import Connection

class Node:

    def __init__(self, name: str, processing: float = 0, queue: float = 0, connections: [Connection] = []):
        self.name = name
        self.proc = processing
        self.queue = queue
        self.con = connections

    def __str__(self):
        str_repr = f'Node {id(self)} | Name: {self.name} | Delays: Processing: {self.proc} ms | Queue: {self.queue} ms'
        if len(self.con) > 0:
            str_repr = str_repr + ' | Connections:'
        return str_repr

    def print_network(self, depth: int = 0):
        print(('-' * depth) + self.__str__())
        for connection in self.con:
            destination: Node = connection.get_dest()
            destination.print_network(depth=depth+1)