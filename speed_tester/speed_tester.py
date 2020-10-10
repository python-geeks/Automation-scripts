import speedtest


def test_speed():
    units = ["bps", "Kbps", "Mbps", "Gbps"]
    servers = []
    test = speedtest.Speedtest()
    test.get_servers(servers)
    test.get_best_server()
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
    print(f"Download speed is: {round(download_speed, 3)}{download_units}")
    print(f"Upload speed is: {round(upload_speed, 3)}{upload_units}")


if __name__ == "__main__":
    test_speed()
