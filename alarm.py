import datetime
import time
import winsound

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Time's up! Alarm activated.")
            play_alarm_sound()
            break

        time.sleep(10)  # Check every 10 seconds

def play_alarm_sound():
    frequency = 2500  # Set frequency (range: 37-32767 Hz)
    duration = 3000  # Set duration in milliseconds

    for _ in range(3):
        winsound.Beep(frequency, duration)
        time.sleep(1)

set_alarm()
