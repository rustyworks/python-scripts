from itertools import cycle
import time


def loading(seconds, message=' '):
    current_seconds = 0
    symbol = cycle('\|/-')
    while current_seconds < seconds:
        time.sleep(.1)
        print('\r', next(symbol), sep='', end='', flush=True)
        current_seconds += .1
    else:
        print('\r', message, sep='')


if __name__ == '__main__':
    loading(3)
