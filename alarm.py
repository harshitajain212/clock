import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour:"))
alarmMin = int(input("Enter Min:" ))
amPm = str(input("am/pm:"))
if amPm =="pm":
    alarmHour = alarmHour + 12
while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin ==datetime.datetime.now().minute:
        print("Wake Up")
        playsound("alarm.mp3")
        break
