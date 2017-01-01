#!/usr/bin/env python3

import os
import time


'''Use this using this command: `python network-checker.py > /dev/null &`'''
if __name__ == '__main__':
    minutes = 0
    message = '''
    Peringatan!
    Koneksi terputus setelah online selama {} menit
    '''

    while(True):
        response = os.system('ping -c 1 -W 2 www.google.co.id')
        time.sleep(60)
        minutes += 1
        if response != 0:
            os.system("notify-send -u 'critical' -i face-angry '" + message.format(minutes,) + "'")
            exit(1)
