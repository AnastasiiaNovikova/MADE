import sys
import numpy as np


n = 0
chunk_size = 1024
values = np.zeros(chunk_size)

for line in sys.stdin:
    try:
        price = line.split(',')[-7]
        values[n] = int(price)
        n += 1
        if n == chunk_size:
            print(chunk_size, values.mean())
            n = 0
    except Exception:
    	continue

print(n, values[:n].mean())
