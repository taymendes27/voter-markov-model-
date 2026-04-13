from src.transition_matrix import get_transition_matrix, validate_transition_matrix

P = get_transition_matrix()
print("Transition matrix:")
print(P)

print("\nValid stochastic matrix?", validate_transition_matrix(P))
