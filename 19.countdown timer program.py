import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}", end="\r")
    time.sleep(1)

print("Let's go ...!") 
