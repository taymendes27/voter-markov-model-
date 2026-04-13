import numpy as np
from src.transition_matrix import get_transition_matrix, validate_transition_matrix
from src.steady_state import steady_state_distribution, matrix_power, evolve_distribution
from src.define_states import STATES

P = get_transition_matrix()

print("Transition matrix:")
print(P)

print("\nValid stochastic matrix?", validate_transition_matrix(P))

pi = steady_state_distribution(P)

print("\nSteady-state distribution by state:")
for state, prob in zip(STATES, pi):
    print(f"{state}: {prob:.4f}")

P2 = matrix_power(P, 2)
P10 = matrix_power(P, 10)

print("\nP^2 (2-step transition matrix):")
print(P2)

print("\nP^10 (10-step transition matrix):")
print(P10)

initial_dist = np.array([0.40, 0.25, 0.20, 0.10, 0.05])

print("\nInitial distribution:")
for state, prob in zip(STATES, initial_dist):
    print(f"{state}: {prob:.4f}")

future_5 = evolve_distribution(initial_dist, P, 5)
future_10 = evolve_distribution(initial_dist, P, 10)

print("\nDistribution after 5 steps:")
for state, prob in zip(STATES, future_5):
    print(f"{state}: {prob:.4f}")

print("\nDistribution after 10 steps:")
for state, prob in zip(STATES, future_10):
    print(f"{state}: {prob:.4f}")
