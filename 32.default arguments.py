# default arguments = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. default, 3. keyword, 4. arbitrary
import time

def count(end, start = 0):
    for times in range(start, end + 1):
        print(times)
        time.sleep(1)
    print("Done!")

count(10)