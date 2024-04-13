import time

while True:
    time.sleep(1)
    imgServFile = open('image-service.txt', 'r')
    randoNum = imgServFile.readline()
    if randoNum.isnumeric():
        time.sleep(5)
        picNum = int(randoNum)
        picLocation = f'Relative file path: Images/{picNum}.jpg'
        imgServFile = open('image-service.txt', 'w')
        imgServFile.write(picLocation)
    imgServFile.close()