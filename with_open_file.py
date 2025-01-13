# Assume that there is no file abc.txt prior to execution of this code.
try:
    with open ("abc.txt","w") as f:
        for i in range(2):
           f.write("Hello World\n")
           f=open ("abc.txt", "w")

        for i in range(3):
            f.write("Hello Universe\n")
            f. close ()

        with open("abc.txt") as f:
            print(f.readline())

except IOError:
    print("Error reading the file")