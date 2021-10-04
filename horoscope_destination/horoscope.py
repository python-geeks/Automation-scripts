import requests


def get_info(sign, day):
    """This function makes the API call to get the result
    of the desired zodiac sign for the desired day."""

    base_url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

    parameters = {"sign": sign, "day": day}

    headers = {'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
               'x-rapidapi-key':
               "9b63804a3cmsh368b3af884ede93p1e0b5djsn7ebb3eb30986"}

    robj = requests.post(base_url, headers=headers, params=parameters)
    return_object = robj.json()
    if robj.status_code == 200:
        res = f'''We see that you are {sign.capitalize()}. Your horoscope for the date
 {return_object['current_date']} says that : '{return_object["description"]}'\n
 You are compatible with {return_object["compatibility"]}. Your lucky color,
 number and time are {return_object["color"]}, {return_object["lucky_number"]}
 and {return_object["lucky_time"]} respectively.\n
 You are expected to be in '{return_object["mood"]}' mood.'''

        return res
    else:
        return "Sorry! No result found."


def bad_input(container, code):
    """This function is used to handle bad user input and gives the user a choice
    to either QUIT the game or enter a valid input."""

    print("\nThis is NOT a valid entry.")
    yn = input("Are you requesting to QUIT? (press y / n) : ")
    if yn == 'y':
        print("\nThankyou for holding up!\n")
        return 1
    elif yn == 'n':
        print("\nPlease enter a valid number.\n")
        return 0
    else:
        print("\nBad Input Again!\nBye Bye.\n")
        return 1


def main():
    """This function displays the complete menu to the user and asks
    for user input. It also invokes bad_input() function in case of
    an invalid entry by the user. It then invokes the get_info() function
    to collect the required result and print it."""

    info_zodiac = '''
    Hello and Welcome to your Horoscope Destination!\n\n
    Select your Zodiac Sign from the list below. Press the code
 along the Sign to proceed.\n
    1. Aries
    2. Taurus
    3. Gemini
    4. Cancer
    5. Leo
    6. Virgo
    7. Libra
    8. Scorpio
    9. Sagittarius
    10. Capricorn
    11. Aquarius
    12. Pisces
    Press any other character to QUIT.\n'''

    info_day = '''
    Which day's horoscope are you looking for?\n
    1. Yesterday
    2. Today
    3. Tomorrow
    Press any other character to QUIT.\n'''

    zodiac = {'1': 'aries', '2': 'taurus', '3': 'gemini',
              '4': 'cancer', '5': 'leo', '6': 'virgo', '7': 'libra',
              '8': 'scorpio', '9': 'sagittarius', '10': 'capricorn',
              '11': 'aquarius', '12': 'pisces'}
    day = {'1': "yesterday", '2': "today", '3': "tomorrow"}

    zodiac_code, day_code = 0, 0

    print(info_zodiac)

    while True:

        while True:
            zodiac_code = input("Press the zodiac code : ")
            if not zodiac.get(zodiac_code, 0):
                if bad_input(zodiac, zodiac_code):
                    return
                else:
                    continue
            break

        print(info_day)

        while True:
            day_code = input("Press the day code : ")
            if not day.get(day_code, 0):
                if bad_input(day, day_code):
                    return
                else:
                    continue
            break
        result = get_info(zodiac[zodiac_code], day[day_code])
        print(f'\n\nWe have an astro prediction for you!\n\n" {result} "\n')


if __name__ == '__main__':
    """The main driver code."""
    main()
