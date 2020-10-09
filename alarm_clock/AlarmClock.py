import time
import datetime
import simpleaudio


set_time = input("please enter the time in HH:MM format to set an alarm : ")
while True:
    time.sleep(1)
    obj = simpleaudio.WaveObject.from_wave_file("./alarm.wav")
    current_time = datetime.datetime.now().time().strftime("%H:%M")
    curr_l = current_time.split(":")
    curr_l = [int(i) for i in curr_l]
    set_l = set_time.split(":")
    set_l = [int(i) for i in set_l]
    print(f"current time : {current_time}")
    print(f"alarm time : {set_time}")
    if curr_l[0] == set_l[0] and curr_l[1] == set_l[1]:
        obj.play()
        print("Time to Wake up")
        input("Press enter to Stop")
        break
