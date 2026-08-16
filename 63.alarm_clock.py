# Python Alarm Clock
import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"The alarm time is {alarm_time}")
    sound_file = "freesound_community-alarm-clock-90867.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.get_busy():
                time.sleep(1)
            is_running = False
        elif current_time > alarm_time:
            print("The alarm time is the passed.")
            is_running = False  

        time.sleep(1)



alarm_time = input("Enter the alarm time (HH:MM:SS): ")
set_alarm(alarm_time)