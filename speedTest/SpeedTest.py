from plyer import notification
import speedtest

st = speedtest.Speedtest(secure=True)

# information about server for the ping test
names = st.get_servers()

download = st.download() / 1048576
upload = st.upload() / 1048576
ping = st.results.ping
country = st.results.server['country']
city_of_country = st.results.server['name']


# printing the data
print(f"Speedtest from a server located in {city_of_country}, {country}")
print(f"Download Speed: {download:.2f} Mbps, \nUpload Speed: {upload:.2f} Mbps,\nPing: {ping} ms")


# displaying the notification
notification.notify(
    title=f"Speedtest from a server located in {city_of_country}, {country}",
    message=f"Download Speed: {download:.2f} Mbps, \nUpload Speed: {upload:.2f} Mbps,\nPing: {ping} ms",
    # displaying time
    timeout=5
)
