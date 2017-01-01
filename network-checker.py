#!/usr/bin/env python3

import os
import time


'''Use this using this command: `python network-checker.py > /dev/null &`'''
if __name__ == '__main__':
    minutes = 0
    message = '''
    Koneksi terputus setelah online selama {} menit
    '''

    while(True):
        response = os.system('timeout 2 ping -c 1 www.google.co.id')
        if response != 0:
            os.system("notify-send -u 'critical' -i face-angry '" + message.format(minutes,) + "'")
            exit(1)
        minutes += 1
        time.sleep(60)
