#find index of row having maximum sum
import numpy as np
arr = np.array([[1, 2, 3],
                [1, 3, 1],
                [5, 5, 6]])

row_sum = arr.sum(axis=1)
index = np.argmax(row_sum)

print(index)