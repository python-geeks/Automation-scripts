import requests


# Function to get UV index from the API
def get_uv_index(lat, lon, api_key):
    url = (
        f"http://api.openweathermap.org/data/2.5/uvi?"
        f"lat={lat}&lon={lon}&appid={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        uv_data = response.json()
        return uv_data['value']
    else:
        return None


# Function to provide sunscreen advice based on UV index and location
def sunscreen_advice(uv_index, indoor):
    if indoor:
        return (
            "You are indoors, sunscreen is not necessary unless you're "
            "near windows with intense sunlight."
        )

    advice = ""
    if uv_index < 3:
        advice = (
            "Low UV index. No sunscreen is needed, but wearing sunglasses "
            "is a good idea."
        )
    elif 3 <= uv_index < 6:
        advice = (
            "Moderate UV index. Wear SPF 15-30 sunscreen and consider "
            "sunglasses and a hat."
        )
    elif 6 <= uv_index < 8:
        advice = (
            "High UV index. Use SPF 30-50 sunscreen, sunglasses, and "
            "seek shade if possible."
        )
    elif 8 <= uv_index < 11:
        advice = (
            "Very high UV index. Use SPF 50+ sunscreen, wear protective "
            "clothing, sunglasses, and avoid direct sun exposure between "
            "10 AM and 4 PM."
        )
    else:
        advice = (
            "Extreme UV index. Stay indoors or use very high SPF sunscreen, "
            "protective clothing, sunglasses, and avoid the sun as much "
            "as possible."
        )

    return advice


# Main function
def main():
    # Enter your details
    lat = input("Enter your latitude: ")
    lon = input("Enter your longitude: ")
    indoor = input("Are you indoors? (yes/no): ").lower() == 'yes'

    # Enter your API key here
    # Visit this link to get your API key - https://openweathermap.org/api
    api_key = 'your_api_key_here'

    # Fetch the UV-Index at the input latitude and longitude
    uv_index = get_uv_index(lat, lon, api_key)

    if uv_index is not None:
        print(f"Current UV index: {uv_index}")
        # Provide sunscreen advice
        advice = sunscreen_advice(uv_index, indoor)
        print(advice)
    else:
        print("Error fetching UV index data.")


if __name__ == "__main__":
    main()
