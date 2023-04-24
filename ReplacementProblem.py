#!/usr/bin/env python3  
import math
# Define the cost functions phi1 and phi2, as well as the value function c
def phi1(x, k):
    # Compute the cost of replacing a machine of age x at time k
    return math.exp(-x) - T * math.sqrt(k)

def phi2(x, k):
    # Compute the cost of operating a machine of age x at time k
    return x**2

def c(x, k):
    # Compute the value of a machine of age x at time k
    return math.exp(-x)

# Define the time horizon K and the maximum machine age X
K = 5
X = 4  
T = 10

# Initialize the value function array and the optimal policy array
V = [[0 for x in range(X+1)] for k in range(K+1)]
optimal_policy = [0 for k in range(K)]

x = 1
k = 0

while x <= X and k < K:
    # Compute the expected cost of keeping the machine
    keep_cost = phi2(x, k) + V[k+1][x]
    print("keep cost:",keep_cost)

    # Compute the expected cost of replacing the machine
    replace_cost = phi1(x, k) + V[0][0]
    print("replace cost:",abs(replace_cost))

    # Check if the machine age is equal to the maximum age 
    if x == X :
        V[k][x] = replace_cost
        optimal_policy[k] = 1
        x=1
        k+=1
    else:
        # Choose the action with the lowest expected cost 
        if abs(replace_cost) < keep_cost:
            V[k][x] = replace_cost
            optimal_policy[k] = 1
            print("here")
        else:
            V[k][x] = keep_cost
            optimal_policy[k] = 0
        x += 1
        k += 1


print(optimal_policy)

