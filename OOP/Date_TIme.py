from playsound import playsound
from datetime import datetime
import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ Wake Up!")
        playsound("alarm.mp3")   # Put alarm.mp3 in the same folder
        break

    time.sleep(1)