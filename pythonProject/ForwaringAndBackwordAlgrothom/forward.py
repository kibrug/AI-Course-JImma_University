import pandas as pd
import numpy as np

V = np.array([0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 2])

# Transition Probabilities
a = np.array(((0.54, 0.46), (0.49, 0.51)))

# Emission Probabilities
b = np.array(((0.16, 0.26, 0.58), (0.25, 0.28, 0.47)))

# # Equal Probabilities for the initial distribution
pi = np.array((0.5, 0.5))

def forward(V, a, b, pi):
    alpha = np.zeros((V.shape[0], a.shape[0]))
    alpha[0, :] = initial_distribution * b[:, V[0]]

    for t in range(1, V.shape[0]):
        for j in range(a.shape[0]):
            alpha[t, j] = alpha[t - 1].dot(a[:, j]) * b[j, V[t]]

    return alpha

alpha = forward(V, a, b, pi)


def forward(V, a, b, pi):
    p = 1
    alpha = np.zeros((V.shape[0], a.shape[0]))
    alpha[0, :] = pi * b[:, V[0]]

    for t in range(1, V.shape[0]):
        probability_of_observation = 0 #my code
        for j in range(a.shape[0]):
            alpha[t, j] = alpha[t - 1].dot(a[:, j]) * b[j, V[t]]
            probability_of_observation += alpha[t, j]  #my code
        p = p * probability_of_observation #my code

    return p #changed

p = forward(V, a, b, pi)  #changed