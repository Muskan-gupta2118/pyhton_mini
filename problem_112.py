#top 3 largest number
import numpy as np
arr = np.array([1, 5, 3, 5, 23, 9])

k = 3
top_k = np.sort(arr)[-k:]

print(top_k)