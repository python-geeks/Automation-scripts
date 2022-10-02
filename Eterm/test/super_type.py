import sys, time


def super_type(b):  # used
    for a in b:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.03)


super_type('\nHEllo')
