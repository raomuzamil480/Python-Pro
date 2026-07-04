# use for multiple task use in reading writing files and
#  use apis for fetching data

import threading
import time

def download():
    print("Downloading...")
    time.sleep(3)
    print("Download complete")

def music():
    print("Playing music...")
    time.sleep(2)
    print("Music stopped")

t1 = threading.Thread(target=download)
t2 = threading.Thread(target=music)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program finished")