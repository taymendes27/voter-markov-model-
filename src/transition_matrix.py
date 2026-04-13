import numpy as np

def get_transition_matrix():
    P = np.array([
        [0.60, 0.30, 0.05, 0.00, 0.05],  # U
        [0.05, 0.50, 0.25, 0.15, 0.05],  # R
        [0.00, 0.05, 0.75, 0.15, 0.05],  # A
        [0.05, 0.15, 0.20, 0.50, 0.10],  # I
        [0.00, 0.00, 0.00, 0.00, 1.00]   # D
    ])
    return P

def validate_transition_matrix(P):
    row_sums = P.sum(axis=1)
    return np.allclose(row_sums, 1.0)
