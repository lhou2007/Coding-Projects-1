import time
import datetime
import pygame
import os


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😴")

            BASE = os.path.abspath(os.path.dirname(__file__))  # Path to the folder containing the script
            sound_file = os.path.join(BASE, "my_music.mp3")  # Full path to the font file

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
 
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)