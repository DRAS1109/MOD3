# Range
"""
range (5) = (0, 1, 2, 3, 4)
range (1, 5) = (1, 2, 3, 4)
range (5, 1) = (5, 4, 3, 2)
range (1, 10, 2) = (1, 3, 5, 7, 9)
range (10, 1, 2) = (10, 8, 6, 4, 2)
"""

from time import sleep
for N in range (5, -1, -1):
    print(N)
    sleep (1)