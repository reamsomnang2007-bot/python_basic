# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  good for I/O(input/output) bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)
import threading
import time

def walk_dog(first_name, last_name):
    time.sleep(5)
    print(f"You finish walking {first_name} {last_name}.")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash.")

def get_mail():
    time.sleep(3)
    print("You get the mail.")

act1 = threading.Thread(target = walk_dog, args = ("KIKI", "TO"))
act1.start()

act2 = threading.Thread(target = take_out_trash)
act2.start()

act3 = threading.Thread(target = get_mail)
act3.start()

act1.join()
act2.join()
act3.join()
print("You are finish all the work...")


