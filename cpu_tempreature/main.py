import os
import sys
import getopt


def rtcheck(seconds):
    try:
        seconds = int(seconds)
        return seconds
    except ValueError:
        return -1


def usageinfo(check, run, exitmsg):
    print("Usage information:\n")
    print("-h / --help\t\tDisplay this usage info.")
    print(
        "-s / --seconds [seconds]\tRun cputemp for specified number of seconds")
    print("-C / --celsius\t\tDisplay temperature in Celsius")
    print("-F / --fahrenheit\t\tDisplay temperature in Fahrenheit")
    print("-K / --kelvin\t\tDisplay temperature in Kelvin")
    print("-a / --average\t\tDisplays only the results (Use with -s and -F/-C)\n")

    if check == 1 or run == 1:
        print(exitmsg)
    sys.exit()


def hwcheck():
    if os.path.exists("/sys/devices/LNXSYSTM:00/LNXTHERM:00/LNXTHERM:01/thermal_zone/temp"):
        return 4

    elif os.path.exists("/sys/bus/acpi/devices/LNXTHERM:00/thermal_zone/temp"):
        return 5

    elif os.path.exists("/proc/acpi/thermal_zone/THM0/temperature"):
        return 1

    elif os.path.exists("/proc/acpi/thermal_zone/THRM/temperature"):
        return 2

    elif os.path.exists("/proc/acpi/thermal_zone/THR1/temperature"):
        return 3

    else:
        return 0


def getDegree():
    degree = 0
    while degree == 0:
        degree = input("(F)ahrenheit, (C)elsius, (K)elvin: ")
        if degree.upper() == "F" or degree.upper() == "FAHRENHEIT":
            degree = "Fahrenheit"
        elif degree.upper() == "C" or degree.upper() == "CELSIUS":
            degree = "Celsius"
        elif degree.upper() == "K" or degree.upper() == "KELVIN":
            degree = "Kelvin"
    return degree


def getTemp(hardware):
    if hardware == 1:
        temp = open("/proc/acpi/thermal_zone/THM0/temperature").read(
        ).strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 2:
        temp = open("/proc/acpi/thermal_zone/THRM/temperature").read(
        ).strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 3:
        temp = open("/proc/acpi/thermal_zone/THR1/temperature").read(
        ).strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 4:
        temp = open(
            "/sys/devices/LNXSYSTM:00/LNXTHERM:00/LNXTHERM:01/thermal_zone/temp").read().strip().rstrip('000')
    elif hardware == 5:
        temp = open(
            "/sys/bus/acpi/devices/LNXTHERM:00/thermal_zone/temp").read().strip().rstrip('000')
        temp = str(float(temp) / 10.0)
    else:
        return 0
    return temp


def dispTemp(temp, degree, minutes, seconds):
    print("\rCPU Temperature: ", temp, degree, end=' ')
    print("(Time Running: ", minutes, ":", end=' ')
    if seconds < 10:
        print("0" + str(seconds), ")", end=' ')
    else:
        print(seconds, ")", end=' ')


def convertDegree(degree, temp):
    if degree == "Fahrenheit":
        temp = temp * 9 / 5.0 + 32
        return temp
    if degree == "Kelvin":
        temp = temp + 273.15
        return temp
    else:
        return temp


def main():
    avg = 0
    ver = 0
    run = 0
    help = 0
    check = 0
    runtime = 5
    degree = 0
    seccount = 0
    seclast = 0
    minutes = 0
    temp = 21
    tsum = 0
    ticker = 0
    exitmsg = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "aCFKs:hV", [
                                   "average", "celsius", "kelvin", "fahrenheit", "seconds=", "help", "version"])
    except getopt.GetoptError:
        help = 1
        check = 1
        exitmsg = "Argument not recognized."
        usageinfo(check, run, exitmsg)
    if check == 0:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                help = 1
            if opt in ("-C", "--celsius"):
                degree = "Celsius"
            if opt in ("-F", "--fahrenheit"):
                degree = "Fahrenheit"
            if opt in ("-K", "--kelvin"):
                degree = "Kelvin"
            if opt in ("-V", "--version"):
                ver = 1
            if opt in ("-s", "--seconds"):
                run = 1
                runtime = arg
            if opt in ("-a", "--average"):
                avg = 1
                run = 1

    if ver == 1:
        sys.exit()
    if help == 1:
        usageinfo(check, run, exitmsg)
    if run == 1:
        runtime = rtcheck(runtime)
        if runtime < 1:
            help = 1
            exitmsg = "Seconds must be defined as an integer greater than zero."
            usageinfo()
    hardware = hwcheck()
    if hardware == 0:
        print("Sorry, your hardware is not yet supported.")
        sys.exit()
    if avg == 1 and degree == 0:
        degree = "Fahrenheit"
    elif degree == 0:
        degree = getDegree()
    import datetime
    import time
    prevtemp = 21
    tmax = 0
    tmin = 1000
    bseconds = int(time.time())

    if avg == 0:
        print("Press Ctrl+C to exit")

    try:
        while True:
            temp = getTemp(hardware)
            tick = int(time.time()) - int(bseconds)
            seccount = int(seccount) + int(tick) - int(seclast)
            seclast = tick
            if seccount >= 60:
                minutes = int(minutes) + 1
                seccount = int(seccount) - 60
            seconds = int(tick) - (60 * int(minutes))
            temp = float(temp)
            if prevtemp > 20 and temp < 18:
                temp = temp * 10
            prevtemp = temp
            temp = convertDegree(degree, temp)
            if avg == 0:
                dispTemp(temp, degree, minutes, seconds)
            if temp < tmin:
                tmin = temp
            if temp > tmax:
                tmax = temp
            tsum = float(tsum) + float(temp)
            ticker = int(ticker) + 1
            if run == 1 and runtime <= seccount:
                break
            time.sleep(1)
            sys.stdout.flush()
    # When Ctrl-C is pressed, show summary data

    except KeyboardInterrupt:
        pass

    tavg = tsum / ticker
    tavg = round(tavg, 1)
    if avg == 0:
        print("\n\nHighest recorded temperature was",
              tmax, "degrees", degree, ".")
        print("Lowest recorded temperature was", tmin, "degrees", degree, ".")
    print("Average temperature was", tavg, "degrees", degree, ".\n")

    import os
    if avg == 1:
        return 0
    elif os.path.exists("/var/log/cputemp.log") and avg == 0:

        tod = datetime.datetime.now()
        templog = open("/var/log/cputemp.log", "a")
        templog.write("Session started at ")
        templog.write(str(tod))
        templog.write("\b\b\b\b\b\b\b :      \n")
        templog.write("cputemp ")
        templog.write(" was run for ")
        templog.write(str(minutes))
        templog.write(" : ")
        if seconds < 10:
            templog.write("0")
        templog.write(str(seconds))
        templog.write(".\n")
        templog.write("Highest recorded temperature was ")
        templog.write(str(tmax))
        templog.write(" degrees ")
        templog.write(str(degree))
        templog.write(".\n")
        templog.write("Lowest recorded temperature was ")
        templog.write(str(tmin))
        templog.write(" degrees ")
        templog.write(str(degree))
        templog.write(".\n")
        templog.write("Average temperature was ")
        templog.write(str(tavg))
        templog.write(" degrees ")
        templog.write(str(degree))
        templog.write(".\n")
        templog.write("---------------\n\n")
        print("Log has been updated")
    else:
        print("Could not locate log file.  Please re-install.")
        return 1


if __name__ == '__main__':
    main()
