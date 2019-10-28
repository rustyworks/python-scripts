import random
import sys
import time


# https://www.youtube.com/watch?v=m9joBLOZVEo
for i in range(10000):
    sys.stdout.write(chr(9585 + random.randint(0, 2)))
    time.sleep(.001)
    sys.stdout.flush()
