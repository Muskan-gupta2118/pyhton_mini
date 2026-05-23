#top 3 largest number
import numpy as np
arr = np.array([10, 5, 3, 50, 23, 90])

k = 3
top_k = np.sort(arr)[-k:]

print(top_k)