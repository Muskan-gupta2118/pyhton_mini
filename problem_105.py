#row sum
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

row_sum = arr.sum(axis=1)
print(row_sum)