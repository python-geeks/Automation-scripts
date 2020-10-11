import speedtest
import subprocess
import platform
import re


def ping_google():
    try:
        system = platform.system().lower()
        option = "n" if system == "windows" else "c"
        res = subprocess.check_output(
            f"ping -{option} 10 google.com",
            shell=True, universal_newlines=True
        )
        if "unreachable" in res:
            return False
        else:
            return res
    except Exception:
        return False


def test_speed():
    units = ["bps", "Kbps", "Mbps", "Gbps"]
    test = speedtest.Speedtest()
    download_speed = test.download()
    unit_index = 0
    while download_speed > 999:
        download_speed /= 1000
        unit_index += 1
    download_units = units[unit_index]
    upload_speed = test.upload()
    unit_index = 0
    while upload_speed > 999:
        upload_speed /= 1000
        unit_index += 1
    upload_units = units[unit_index]
    ping = ping_google()
    if ping:
        times = re.findall(r"(?<=time=)\d+\.?\d*", ping)
        times = [float(time) for time in times]
        av_ping = sum(times) / len(times)
        print(f"Average ping time for google.com is: {av_ping}ms")
    else:
        print("Can't connect to google.com")
    print(f"Download speed is: {round(download_speed, 3)}{download_units}")
    print(f"Upload speed is: {round(upload_speed, 3)}{upload_units}")


if __name__ == "__main__":
    test_speed()
