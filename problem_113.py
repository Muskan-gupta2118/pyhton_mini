#find index of row having maximum sum
import numpy as np
arr = np.array([[1, 2, 3],
                [10, 2, 1],
                [4, 5, 6]])

row_sum = arr.sum(axis=1)
index = np.argmax(row_sum)

print(index)