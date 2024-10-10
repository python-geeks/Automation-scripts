import subprocess
import getpass
import time
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile


def connect_wifi(ssid, password):
    # function to connect to Wi-Fi with Password

    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()  # disconnects from the current Wi-Fi if any
    time.sleep(2)

    profile = Profile()  # adding new Profile for given Wi-Fi
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    print("\nConnecting to WiFi....")
    iface.connect(iface.add_network_profile(profile))
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print("\t>> Connected Successfully!")
    else:
        print("\t>> Failed to Connect!")


def get_available_wifi():
    # function to get 3 strongest Wi-Fi with SSIDs in Windows

    try:

        cmd = ['netsh', 'wlan', 'show', 'network', 'mode=Bssid']
        wifidata = subprocess.check_output(cmd).decode(
            'ascii').replace("\r", "").split("\n\n")

    except subprocess.CalledProcessError:
        print("\nWhoops! Your Wi-Fi seems to be powered off.")
        raise SystemExit

    else:
        networks = []
        for i in range(1, len(wifidata) - 1):  # parsing SSIDs and signals
            temp = wifidata[i].split("\n")
            ssid = temp[0].rstrip().split(" : ")[-1]
            signal = int(temp[5].rstrip().split(" : ")[-1][:-1])
            networks.append((ssid, signal))

        networks = sorted(networks, reverse=True, key=lambda x: x[1])
        return (networks)


def main():
    # main function to take 3 strongest Wi-Fis and connect

    networks = get_available_wifi()[:3]  # get top 3 strongest networks

    print(f"\nYour {len(networks)} Strongest Networks are :")
    for key, network in enumerate(networks):
        print(f"\t[{key + 1}] {network[0]}, Signal: {network[1]}%")

    choice = input("\nPlease enter your choice : \n\t>> ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(networks)):
        print("Wrong Choice Entered. Exiting...")
        return False

    ssid = networks[int(choice) - 1][0]

    #  check if the chosen SSID is already connected
    if ssid in subprocess.check_output("netsh wlan show interfaces").decode():
        print(f"\nYou are already connected to {ssid} Network. \nExiting...")
    else:
        print(f"\nYou Selected: {ssid}")
        password = getpass.getpass()
        # connect to the chosen SSID with password
        connect_wifi(ssid, password)


if __name__ == "__main__":
    main()
