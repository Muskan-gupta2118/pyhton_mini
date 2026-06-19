#swap two number row in matrix
import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr[[0,2]] = arr[[2,0]]

print(arr)