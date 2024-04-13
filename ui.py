import time

while True:
    userInput = int(input("Enter 1 and I'll write the file path to a flower. Enter any other key to exit: "))

    if userInput == 1:
        # writes run in the prng-service.txt file
        with open('prng-service.txt', 'w') as outfile:
            outfile.write("run")
        time.sleep(10)

        # reads the random number in the prng-service.txt file
        with open('prng-service.txt', 'r') as infile:
            randoNum = infile.readline()
        # writes the random integer into the image-service.txt file
        with open('image-service.txt', 'w') as outfile:
            outfile.write(randoNum)
        time.sleep(10)

        # display the flower I picked for the user from my garden
        with open('image-service.txt', 'r') as infile:
            location = infile.readline()
            print(location)
    else:
        print("Goodbye!")
