import time
import random

while True:
    time.sleep(1)
    # open and read prng text file
    prngFile = open('prng-service.txt', 'r')
    prngValue = prngFile.readline()
    if prngValue == 'run':
        time.sleep(5)
        randoNum = str(random.randint(0, 4))
        prngFile = open('prng-service.txt', 'w')
        prngFile.write(randoNum)
    prngFile.close()