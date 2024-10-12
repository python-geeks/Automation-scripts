# Import necessary modules
from datetime import datetime, timedelta
from skyfield.iokit import parse_tle_file
from skyfield.api import load
from selenium import webdriver
import folium
import time
import os


# Constants
TLE_FILENAME = "data_files/iss_zarya_tle.tle"
TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"
MAP_FILENAME = "map/tracker_map.html"
MAP_ZOOM_START = 2
ORBIT_DURATION_MINUTES = 90
UPDATE_INTERVAL_SECONDS = 60


# Functions
def download_tle_file():
    """
    If the TLE file is missing or is outdated, download the latest data.
    """
    if not load.exists(TLE_FILENAME) or load.days_old(TLE_FILENAME) > 1.0:
        try:
            load.download(TLE_URL, filename=TLE_FILENAME)
        except Exception as e:
            print(f"ERROR: Failed to download the TLE data.{e}")
            exit(1)


def load_satellite_data():
    """
    Load the satellite data from the TLE file.
    """
    with load.open(TLE_FILENAME) as f:
        satellites = list(parse_tle_file(f, load.timescale()))
    # Index ISS (ZARYA) by NORADID number.
    return {sat.model.satnum: sat for sat in satellites}[25544]


def create_map(sat_lat, sat_lon):
    """
    Create a new map with the ISS's current position.
    """
    # Create a map centered onto the ISS position.
    iss_map = folium.Map(
        location=[sat_lat, sat_lon],
        zoom_start=MAP_ZOOM_START
    )
    # Pinpoint the satellite's current position on the map.
    folium.Marker(
        location=[sat_lat, sat_lon],
        tooltip=f"ISS (Lat: {sat_lat}, Lon: {sat_lon})",
        popup="International Space Station (ZARYA)",
        icon=folium.Icon(color="red", icon="satellite", prefix="fa")
    ).add_to(iss_map)
    return iss_map


def predict_orbit(satellite, current_time):
    """
    Predict the orbit of the satellite by predicting its future poitions.
    ISS completes one orbit around the Earth in approximately 90 minutes.
    """
    # Add current position of the satellite
    current_sat_lat = satellite.at(current_time).subpoint().latitude.degrees
    current_sat_lon = satellite.at(current_time).subpoint().longitude.degrees
    orbit_coordinates = [(current_sat_lat, current_sat_lon)]
    for i in range(1, ORBIT_DURATION_MINUTES + 1):
        future_time = current_time + timedelta(minutes=i)
        future_geocentric_pos = satellite.at(future_time)
        future_sub_pos = future_geocentric_pos.subpoint()
        future_sat_lat = future_sub_pos.latitude.degrees
        future_sat_lon = future_sub_pos.longitude.degrees
        # Longitude Adjustment: Check for large jumps in longitude.
        if abs(future_sat_lon - orbit_coordinates[-1][1]) > 180:
            if future_sat_lon < orbit_coordinates[-1][1]:
                future_sat_lon += 360
            else:
                future_sat_lon -= 360
        # Add the fixed coordinates to the list of orbit coordinates.
        orbit_coordinates.append((future_sat_lat, future_sat_lon))
    return orbit_coordinates


def main():
    download_tle_file()
    satellite = load_satellite_data()
    driver = webdriver.Firefox()
    driver.get(f"file:///{os.path.abspath(MAP_FILENAME)}")
    while True:
        current_time = datetime.utcnow()
        t = load.timescale().utc(
            current_time.year,
            current_time.month,
            current_time.day,
            current_time.hour,
            current_time.minute,
            current_time.second
        )
        geocentric_pos = satellite.at(t)
        sub_pos = geocentric_pos.subpoint()
        sat_lat = sub_pos.latitude.degrees
        sat_lon = sub_pos.longitude.degrees
        iss_map = create_map(sat_lat, sat_lon)
        orbit_coordinates = predict_orbit(satellite, t)
        folium.PolyLine(
            locations=orbit_coordinates,
            color="black",
            weight=1,
            dash_array="5"
        ).add_to(iss_map)
        iss_map.save(MAP_FILENAME)
        driver.refresh()
        time.sleep(UPDATE_INTERVAL_SECONDS)


# Ensure the "main" function is only executed when the script is run directly.
if __name__ == "__main__":
    main()
