#!/usr/bin/python

import subprocess 
import signal
from datetime import datetime

OUTPUT_FILE = "/home/pi/speedtest/speeds.csv"

def test():
	ts = str(datetime.now())
	speed_lines = subprocess.Popen("speedtest-cli --simple", shell=True, stdout=subprocess.PIPE).stdout.read().split("\n")
	ping = " ".join(speed_lines[0].split(" ")[1:])
	dl = " ".join(speed_lines[1].split(" ")[1:])
	ul = " ".join(speed_lines[2].split(" ")[1:])
	line = ",".join([ts, ping, dl, ul]) + "\r\n"

	with open(OUTPUT_FILE, "a") as speeds_file:
		speeds_file.write(line)
		print "Speedtest output written to %s" % OUTPUT_FILE

class timeout:
	def __init__(self, seconds = 60, error_message='Timeout'):
		self.seconds = seconds
		self.error_message = error_message
	def handle_timeout(self, signum, frame):
		raise TimeoutError(self.error_message)
	def __enter__(self):
		signal.signal(signal.SIGALRM, self.handle_timeout)
		signal.alarm(self.seconds)
	def __exit__(self, type, value, traceback):
		signal.alarm(0)

class TimeoutError(Exception):
	pass

if __name__ == '__main__':
	with timeout(seconds=300):
		test()
