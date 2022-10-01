import speech_recognition as sr


def speech_rec_for_linux():
    import espeak
    espeak.init()
    speaker = espeak.Espeak()
    # import pyttsx3
    # speaker = pyttsx3.init()

    r = sr.Recognizer()
    text = ""
    count = 0
    medicines = {}

    with sr.Microphone() as source:
        while (True):
            medicine_dict = {}
            count += 1

            print("Medicine-" + str(count) + " Information")

            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)

            print("Medicine Name:")
            speaker.say("Medicine name")
            # speaker.rate = 300

            recorded_audio = r.listen(source, timeout=6)
            print("Done")

            try:
                text = r.recognize_google(
                    recorded_audio,
                    language="en-US"
                )
                if 'exit' in str(text).lower():
                    print("Thanks for using our service!")
                    break

                medicine_dict["Medicine Name"] = str(text)
                print("Decoded Text : {}".format(text))

            except Exception as e:
                print(e)

            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)

            print("Medicine Instruction:")
            speaker.say("Medicine Instruction")

            recorded_audio = r.listen(source, timeout=6)
            print("Done")

            try:
                text = r.recognize_google(
                    recorded_audio,
                    language="en-US"
                )
                medicine_dict["Instruction"] = str(text)
                print("Decoded Text : {}".format(text))

            except Exception as e:
                print(e)

            medicines["Medicine No. " + str(count)] = medicine_dict

    return medicines


def speech_rec_for_windows():
    import pyttsx3
    speaker = pyttsx3.init()
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.SpVoice").Speak

    r = sr.Recognizer()
    text = ""
    count = 0
    medicines = {}

    with sr.Microphone() as source:
        while (True):
            medicine_dict = {}
            count += 1

            print("Medicine-" + str(count) + " Information")

            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)

            print("Medicine Name:")
            speaker.say("Medicine name")
            speaker.runAndWait()

            recorded_audio = r.listen(source, timeout=6)
            print("Done")

            try:
                text = r.recognize_google(
                    recorded_audio,
                    language="en-US"
                )
                if 'exit' in str(text).lower():
                    print("Thanks for using our service!")
                    break

                medicine_dict["Medicine Name"] = str(text)
                print("Decoded Text : {}".format(text))

            except Exception as e:
                print("Exception", e)

            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)

            print("Medicine Instruction:")
            speaker.say("Medicine Instruction")
            speaker.runAndWait()

            recorded_audio = r.listen(source, timeout=6)
            print("Done")

            try:
                text = r.recognize_google(
                    recorded_audio,
                    language="en-US"
                )
                medicine_dict["Instruction"] = str(text)
                print("Decoded Text : {}".format(text))

            except Exception as e:
                print("Exception", e)

            medicines["Medicine No. " + str(count)] = medicine_dict

    return medicines
