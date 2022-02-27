#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.
    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'
    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    c1=cnot.wires[0]
    c2=cnot.wires[1]
    d0={1:0,2:2,3:2,4:2,5:4,6:6,7:4,8:4}
    d1={0:1,2:0,3:0,4:0,5:2,6:4,7:2,8:2}
    d2={1:0,0:2,3:2,4:2,5:4,6:6,7:4,8:4}
    d3={1:0,2:2,0:2,4:2,5:4,6:6,7:4,8:4}
    d4={1:0,2:2,3:2,0:2,5:0,6:2,7:0,8:0}
    d5={1:2,2:4,3:4,4:0,0:4,6:0,7:2,8:2}
    d6={1:4,2:6,3:6,4:2,5:0,0:6,7:0,8:4}
    d7={1:2,2:4,3:4,4:0,5:2,6:0,0:4,8:2}
    d8={1:2,2:4,3:4,4:0,5:2,6:4,7:2,0:4}
    L=[d0,d1,d2,d3,d4,d5,d6,d7,d8]
    return L[c1][c2]

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")