#!/usr/bin/env python3  
import numpy as np

def optimal_replacement_policy(X, K, T, phi1, phi2):
    # Initialize the value function to zero
    V = np.zeros(K+1)

    # Loop backwards in time from K-1 to 0
    for k in range(K-1, -1, -1):
        # Compute the value function for all possible actions
        action_values = [(1-u)*phi2(X[k],k) + u*(np.exp(-X[k])-T*np.sqrt(k)) + V[k+1] for u in [0, 1]]

        # Choose the optimal action (0 = keep, 1 = replace)
        u_star = np.argmin(action_values)

        # Update the value function and optimal policy
        V[k] = action_values[u_star]
        u_k = u_star

    return u_k

# Example usage:
phi1 = lambda x, k: np.exp(-x)
phi2 = lambda x, k: x**2

X = np.array([1, 2, 3, 4, 5])
K = len(X)-1
T = 10

u_star = optimal_replacement_policy(X, K, T, phi1,phi2)
print("Optimal replacement policy:", u_star)

X = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
K = len(X)-1
T = 2.0

u_star = optimal_replacement_policy(X, K, T, phi1,phi2)
print("Optimal replacement policy:", u_star)

