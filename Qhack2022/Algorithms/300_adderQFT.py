#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

def binary_list(m, n):
    """Converts number m to binary encoded on a list of length n
    Args:
        - m (int): Number to convert to binary
        - n (int): Number of wires in the circuit
    Returns:
        - (list(int)): Binary stored as a list of length n
    """

    arr = [0 for i in range(n)]
    # QHACK #
    s = str(bin(m).replace("0b", ""))
    for j in range(len(s)):
        arr[len(arr) - j - 1] = int(s[len(s) - j - 1])

    # QHACK #
    return arr
def qfunc_adder(m, wires):
    """Quantum function capable of adding m units to a basic state given as input.
    Args:
        - m (int): units to add.
        - wires (list(int)): list of wires in which the function will be executed on.
    """

    qml.QFT(wires=wires)

    # QHACK #
    for i in range(len(wires)):
        qml.PhaseShift( np.pi*m/(2**(i)), wires = i )
    # QHACK #

    qml.QFT(wires=wires).inv()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)
        qfunc_adder(m, wires)
        return qml.sample()

    output = test_circuit()
    print(*output, sep=",")
