#replace all value >5 into 0
import numpy as np
arr = np.array([2, 6, 3, 8, 1])

arr[arr > 5] = 0
print(arr)