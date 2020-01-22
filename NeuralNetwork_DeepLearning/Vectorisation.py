## Vectorisation example
"""
This script measures the difference between vectorised code execution and basic loop code execution.
"""
## Loading packages
import numpy as np
import time

## Measuring time needed:
# Vectorised version:
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time() # Record start time
c = np.dot(a,b)
toc = time.time() # Record end time
print(c)
print("Vectorised version:" + str(1000*(toc-tic)) + "ms")

# Loops version:
c=0
tic = time.time() # Record start time
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time() # Record end time
print(c)
print("Vectorised version:" + str(1000*(toc-tic)) + "ms")