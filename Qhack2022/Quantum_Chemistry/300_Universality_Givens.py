#! /usr/bin/python3

import sys
import numpy as np


def givens_rotations(a, b, c, d):
    """Calculates the angles needed for a Givens rotation to out put the state with amplitudes a,b,c and d
    Args:
        - a,b,c,d (float): real numbers which represent the amplitude of the relevant basis states (see problem statement). Assume they are normalized.
    Returns:
        - (list(float)): a list of real numbers ranging in the intervals provided in the challenge statement, which represent the angles in the Givens rotations,
        in order, that must be applied.
    """

    # QHACK #
    # theta1=2*np.arccos(np.sqrt((a*a+d*d)))%np.pi

    # theta3=(2*np.arcsin(-d/np.cos(theta1/2)))%np.pi
    theta3 = 2 * np.arctan(-d / a)
    # theta2=((2*np.arccos((-b/np.sin(theta1/2))))%np.pi)
    theta2 = 2 * np.arctan(-c / (b))
    theta1 = 2 * np.arctan(-b / a * (np.cos(theta3 / 2) / np.cos(theta2 / 2)))
    return [theta1, theta2, theta3]

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    theta_1, theta_2, theta_3 = givens_rotations(
        float(inputs[0]), float(inputs[1]), float(inputs[2]), float(inputs[3])
    )
    print(*[theta_1, theta_2, theta_3], sep=",")