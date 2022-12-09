import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the two probability distributions
p1 = np.array([0.2, 0.3, 0.2, 0.3])
p2 = np.array([0.3, 0.2, 0.3, 0.4])

# Calculate simple cost matrix
cost_matrix = np.zeros((len(p1), len(p2)))
for i in range(len(p1)):
    for j in range(len(p2)):
        cost_matrix[i, j] = np.abs(p1[i] - p2[j])

print (cost_matrix)
# Perform the optimal transport
row_ind, col_ind = linear_sum_assignment(cost_matrix)
print (row_ind, 'row_ind')
print (col_ind, 'col_ind')
print (type(col_ind))
# Calculate the optimal transport cost
optimal_cost = cost_matrix[row_ind, col_ind].sum()

# Print the results
print("Optimal transport cost:", optimal_cost)
print("Optimal transport matrix:")
for i in range(len(p1)):
    print(p1[i], "->", p2[col_ind[i]])