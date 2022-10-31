import os
import playsound
import time
from time import sleep
import sys
import multiprocessing


def remind():
	startTime = time.time()
	while True:
		sleep(20*60)
		os.popen('osascript -e "set Volume 6"')
		p = multiprocessing.Process(target=playsound.playsound, args=("danger.mp3",))
		p.start()
		inp = input('Dismiss? y|n')

		if inp == 'y':
			print("yes")
			p.terminate()
			continue


if __name__ == "__main__":
	remind()
