import time
import datetime
import simpleaudio

t = int()


def snooze(t):
    global set_time
    HH_MM = set_time.split(':')
    HH_MM[1] = str(int(HH_MM[1]) + t)
    set_time = ':'.join(HH_MM)


set_time = input("please enter the time in HH:MM format to set an alarm : ")
label = input("Alarm label: ")


def alarm(set_time):
    while True:
        time.sleep(1)
        obj = simpleaudio.WaveObject.from_wave_file("./alarm.wav")
        current_time = datetime.datetime.now().time().strftime("%H:%M")
        curr_l = current_time.split(":")
        curr_l = [int(i) for i in curr_l]
        set_l = set_time.split(":")
        set_l = [int(i) for i in set_l]
        if curr_l[0] == set_l[0] and curr_l[1] == set_l[1]:
            print(label)
            obj.play()
            break


while True:
    alarm(set_time)
    x = input("Press y if you want the alarm to snooze: ")
    if x == 'y':
        t = int(input("Snooze time: "))
        snooze(t)
        print(f"The alarm will ring again in {t} min")
    else:
        break
