import numpy as np

def steady_state_distribution(P):
    eigenvalues, eigenvectors = np.linalg.eig(P.T)
    idx = np.argmin(np.abs(eigenvalues - 1))
    steady_state = np.real(eigenvectors[:, idx])
    steady_state = steady_state / steady_state.sum()
    return steady_state

def matrix_power(P, n):
    return np.linalg.matrix_power(P, n)

def evolve_distribution(initial_dist, P, n):
    return initial_dist @ np.linalg.matrix_power(P, n)
