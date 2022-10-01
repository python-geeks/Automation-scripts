import sys
import getopt
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta


# --- INFO ON PARAMS ---
def print_help():
    print('[+] use --cu and pass custom timezone to find time.')
    print('[+] use --cm to get the time of common timezones around the world.')
    print('[+] use --cmp and pass two \'-\' seperated timezones to compare.')
    print('[+] use --help again if needed.')
    print('\n' + '-' * 50 + '\n')


# --- GET DATETIME OF PASSED TIMEZONE ---
def get_datetime(time_zone):
    utcnow = timezone('utc').localize(datetime.utcnow())
    output_datetime = utcnow.astimezone(timezone(time_zone)).replace(tzinfo=None)
    return output_datetime


# --- GET DATETIME OF CUSTOM TIMEZONE ---
def get_custom_tz(time_zone):
    response = str(get_datetime(time_zone))
    print(f'%20s' % 'Timezone' + '  :' + ' ' * 2 + time_zone)  # noqa
    date, time = response.split(' ')
    hours, minutes, seconds = time.split(':')
    print('%20s' % 'Hours' + '  :' + ' ' * 2 + hours)
    print('%20s' % 'Minutes' + '  :' + ' ' * 2 + minutes)
    print('%20s' % 'Seconds' + '  :' + ' ' * 2 + seconds)
    print('%20s' % 'Date' + '  :' + ' ' * 2 + date)
    print('\n' + '-' * 50 + '\n')


# --- GET DATETIMES OF COMMON TIMEZONES ---
def get_common_tz():
    common_tz_list = [
        'America/Sao_Paulo',
        'America/New_York',
        'America/Mexico_City',
        'Asia/Kolkata',
        'Asia/Tokyo',
        'Europe/Paris',
        'Europe/Berlin',
        'Africa/Johannesburg',
        'Africa/Casablanca',
        'Australia/Melbourne',
    ]
    for item in common_tz_list:
        print('%-20s' % item, end='')
        print(':' + ' ' * 2 + str(get_datetime(item)))
    print('\n' + '-' * 50 + '\n')


# --- COMPARE DIFFERENCES BTW TWO TIMEZONES ---
def get_comparisons(tz_1, tz_2):
    offset = relativedelta(get_datetime(tz_1), get_datetime(tz_2))
    print('%25s' % 'Comparing :', tz_1)
    print('%25s' % 'With :', tz_2)
    print('')
    print('%25s' % 'Hours :', offset.hours)
    print('%25s' % 'Minutes :', offset.minutes)
    print('%25s' % 'Seconds :', offset.seconds)
    print('\n' + '-' * 50 + '\n')


# --- MAIN FUNCTION ---
def Main():
    print('\n' + '-' * 50 + '\n')
    print(' ' * 16 + 'TIMEZONE TOOL')
    print('\n' + '-' * 50 + '\n')

    # --- SET DEFAULTS ---
    argument_list = sys.argv[1:]
    options = ''
    long_options = ['cu=', 'cm', 'cp=', 'help']

    # --- TRY-CATCH BLOCK FOR ARGS ---
    try:
        args, _ = getopt.getopt(argument_list, shortopts=options, longopts=long_options)
        for current_argument, current_value in args:
            if current_argument in ('--help'):
                print_help()
            if current_argument in ('--cu'):
                get_custom_tz(current_value)
            if current_argument in ('--cm'):
                get_common_tz()
            if current_argument in ('--cp'):
                timezones = current_value.split('-')
                if len(timezones) == 2:
                    get_comparisons(timezones[0], timezones[1])
                else:
                    print(' ' * 5, '[+] Seperate the Timezones with \'-\'')
                    print('\n' + '-' * 50 + '\n')

    except getopt.error as error:
        print(str(error))


if __name__ == '__main__':
    Main()
