#!/usr/bin/env python3  
import math

# Define the cost functions phi1 and phi2, as well as the value function c
def phi1(x, k):
    # Compute the cost of replacing a machine of age x at time k
    return  T * math.sqrt(k) - math.exp(-x) 

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

# Initialize the graph with the starting node
graph = {(0, 1): {'J': 0, 'x': 1}}

# Loop over the periods
for k in range(K):
    # Loop over the nodes in the current period
    for node in list(graph.keys()):
        # Calculate the x and J values for u=0 (replacement)
        x1 = node[1] + 1
        f1 = phi1(x1, k+1)  # we replace the machine, so x=x1
        J1 = graph[node]['J'] + f1
        
        # Calculate the x and J values for u=1 (no replacement)
        f2 = -phi2(node[1], k+1)  # operating cost for one more period
        if node[1] < X:
            J2 = graph[node]['J'] + f2
            graph[(k+1, x1)] = {'J': J1, 'x': x1}  # add only if the machine age is less than X
        else:
            # if machine is too old, we must replace it
            f2 += phi1(X+1, k+1)
            J2 = graph[(k+1, 1)]['J'] + f2
        
        # Add the new nodes to the graph
        if node[1] < X:  # add only if the machine age is less than X
            graph[(k+1, node[1])] = {'J': J2, 'x': node[1]}
        
# Find the optimal path by backtracking from the last period
node = max(graph.keys(), key=lambda node: graph[node]['J'])
path = [node]
for k in range(K, 0, -1):
    prev_node1 = (k-1, node[1]-1)
    prev_node2 = (k-1, node[1])
    if prev_node1 in graph and prev_node2 in graph:
        if graph[prev_node1]['J'] > graph[prev_node2]['J']:
            node = prev_node1
        else:
            node = prev_node2
    elif prev_node1 in graph:
        node = prev_node1
    elif prev_node2 in graph:
        node = prev_node2
    path.insert(0, node)

# Print the optimal path and total cost
print('Optimal path:')
for node in path:
    u = 1 if node[1]-path[path.index(node)-1][1]==1 else 0
    print(f'u={u}, k={node[0]}, x={node[1]}, J={graph[node]["J"]}')
print(f'Total cost: {graph[path[-1]]["J"]}')
