# ISS Tracker 🛰️
A Python script to fetch TLE data of the ISS (ZARYA) satellite, calculate its position, predict its orbit and visualize its trajectory on an interactive map. Thanks to [Celestrak](https://celestrak.org/) We can access to the TLE data of satellites, including International Space Station.

## How to Run
- Install required modules: `pip install -r requirements.txt`
- Run the script: `python3 tracker.py`
- Wait for the map to launch.

## Key Concepts
### What is a TLE?
A Two-Line Element Set (TLE) is a standardized format used to describe the orbit of a satellite. It consists of two lines of data that include important orbital parameters, such as the satellite's position, velocity, and other relevant information at a specific time known as the epoch (Source: ["Two-line-element set"](https://en.wikipedia.org/wiki/Two-line_element_set)).

### What is a Geocentric Position?
A geocentric position refers to a viewpoint or coordinate system that is centered on the Earth. In astronomy, it describes a model where the Earth is considered the center of the universe, with celestial bodies like the Sun and planets (or even satellites) orbiting around it (Source: ["Earth-centered, Earth-fixed coordinate system"](https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system) and ["Geocentric model"](https://en.wikipedia.org/wiki/Geocentric_model)).

### What is a Subpoint Position?
In Astronomy, the subpoint position (or subsatellite point) of a satellite refers to the point on the Earth's surface that is directly beneath the satellite at any given moment. It is defined by its geographical coordinates, latitude and longitude (Source: ["Geodesy for the Layman" by U.S. Geological Survey](https://www.ngs.noaa.gov/PUBS_LIB/Geodesy4Layman/TR80003D.HTM#ZZ9)). This point is significant because it represents the satellite's ground track, which is the path that the satellite appears to trace over the Earth's surface as it orbits (Source: ["Satellite Communications" by Dennis Roddy](https://books.google.com/books/about/Satellite_Communications_Fourth_Edition.html?id=2KEt_hFyjwgC)).

### What is International Date Line (IDL)?
The International Date Line is an imaginary line that runs from the North Pole to the South Pole, primarily along the 180th meridian in the Pacific Ocean. It serves as the boundary between two consecutive calendar dates, meaning when you cross it, you either gain or lose a day depending on the direction you are traveling (Source: ["The international date line, explained"](https://www.livescience.com/44292-international-date-line-explained.html) and ["International Date Line"](https://www.britannica.com/topic/International-Date-Line)).

### What libraries are used in the script?
- `Skyfield` ([Documentation](https://rhodesmill.org/skyfield/))
- `Folium` ([Documentation](https://python-visualization.github.io/folium/latest/index.html))
- `Selenium` ([Documentation](https://www.selenium.dev/documentation/))
- `Datetime` ([Documentation](https://docs.python.org/3/library/datetime.html))
- `Time` ([Documentation](https://docs.python.org/3/library/time.html))
- `OS` ([Documentation](https://docs.python.org/3/library/os.html))

## Output
![Screenshot_1](https://github.com/user-attachments/assets/1027863f-fe7a-46ee-abb6-daef4b6a12a3)
![Screenshot_2](https://github.com/user-attachments/assets/4ee308a3-41b1-4bb0-b02a-e394f090444b)

## Author
Mohammad Bazargan ([BazarganDev](https://github.com/BazarganDev))

