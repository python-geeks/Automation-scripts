class InvalidHours(Exception):
    """Invalid"""
    pass


class InvalidMins(Exception):
    """Invalid"""
    pass


# Taking user input
starting_zone = input("Enter starting zone: ")
time = input("Enter time: ")
end_zone = input("Enter desired time zone: ")

lst = time.split(":")
hours1 = int(lst[0])
mins1 = int(lst[1][:2])
ampm = lst[1][2:]

# Exception handling
try:
    if hours1 >= 12:
        raise InvalidHours
except InvalidHours:
    print("Invalid Hours")
    exit()

try:
    if mins1 >= 60:
        raise InvalidMins
except InvalidMins:
    print("Invalid Minutes")

# Time conversion according to zone
if starting_zone == "CST":
    hours1 = hours1 + 6
    pass
elif starting_zone == "EST":
    hours1 = hours1 - 10
    pass
elif starting_zone == "MST":
    hours1 = hours1 + 7
    pass
elif starting_zone == "PST":
    hours1 = hours1 + 8

if hours1 > 12:
    hours1 = hours1-12
    if ampm == 'am':
        ampm = 'pm'
    elif ampm == 'pm':
        ampm = 'am'
elif hours1 < 0:
    hours1 = hours1+12
    if ampm == 'am':
        ampm = 'pm'
    elif ampm == 'pm':
        ampm = 'am'

if end_zone == "CST":
    hours1 = hours1 - 6
elif end_zone == "EST":
    hours1 = hours1 + 10
elif end_zone == "MST":
    hours1 = hours1 - 7
elif end_zone == "PST":
    hours1 = hours1 - 8

if hours1 > 12:
    hours1 = hours1-12
    if ampm == 'am':
        ampm = 'pm'
    elif ampm == 'pm':
        ampm = 'am'
elif hours1 < 0:
    hours1 = hours1+12
    if ampm == 'am':
        ampm = 'pm'
    elif ampm == 'pm':
        ampm = 'am'

# Result
print('Time: ' + str(hours1) + ":" + str(mins1) + ampm)
