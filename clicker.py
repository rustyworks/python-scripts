import argparse
import shlex
import subprocess
import time


def click(number_of_click):
    time.sleep(5)
    for i in range(number_of_click):
        # cmd = shlex.split('xdotool mousemove 1270 604 click 1')
        cmd = shlex.split('xdotool click 1')
        subprocess.call(cmd)
        time.sleep(0.01)

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--click', default=100, type=int)
args = vars(parser.parse_args())
click(args['click'])
