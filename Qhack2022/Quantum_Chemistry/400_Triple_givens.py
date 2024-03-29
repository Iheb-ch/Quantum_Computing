import sys
import pennylane as qml
from pennylane import numpy as np

NUM_WIRES = 6


def triple_excitation_matrix(gamma):
    """The matrix representation of a triple-excitation Givens rotation.
    Args:
        - gamma (float): The angle of rotation
    Returns:
        - (np.ndarray): The matrix representation of a triple-excitation
    """

    # QHACK #
    return np.eye(2**3)
    # QHACK #


dev = qml.device("default.qubit", wires=6)


@qml.qnode(dev)
def circuit(angles):
    """Prepares the quantum state in the problem statement and returns qml.probs
    Args:
        - angles (list(float)): The relevant angles in the problem statement in this order:
        [alpha, beta, gamma]
    Returns:
        - (np.tensor): The probability of each computational basis state
    """
    psi=np.zeros(2**6)
    psi[56]=np.cos(angles[0]/2)*np.cos(angles[1]/2)*np.cos(angles[2]/2)
    psi[7]=-np.cos(angles[0]/2)*np.cos(angles[1]/2)*np.sin(angles[2]/2)
    psi[11]=-np.cos(angles[0]/2)*np.sin(angles[1]/2)
    psi[25]=-np.sin(angles[0]/2)
    qml.AmplitudeEmbedding(psi,wires=range(NUM_WIRES))
    # QHACK #

    # QHACK #

    return qml.probs(wires=range(NUM_WIRES))


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = np.array(sys.stdin.read().split(","), dtype=float)
    probs = circuit(inputs).round(6)
    print(*probs, sep=",")