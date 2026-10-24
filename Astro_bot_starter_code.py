#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step by step instructions can be found in the appendix A of this assignment brief. 
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by stepdevelopment process. 

# =========================
# REQUIRED LIBRARIES
# =========================

import requests
import json
import time
from datetime import datetime

# =========================
# CONFIGURATION FUNCTIONS
# =========================
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return f"Bearer {token}"
    else:
        return "Bearer MDllZTJmZjQtNDk1YS00ZGE2LWJiODItNGRjOWE2ZDg4YWY1ZTY0YjJlNTItMjNi_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"

def get_api_key(prompt, hardcoded_key):
    choice = input(f"Use hard-coded {prompt}? (y/n): ").lower()
    if choice == "n":
        return input(f"Enter your {prompt}: ")
    else:
        return hardcoded_key

  #complete the function to get the API key from user input or use a hardcoded key

# =========================
# WEBEX FUNCTIONS
# =========================

def get_rooms(token):

    url = "https://webexapis.com/v1/rooms"
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching rooms:", response.status_code)
        return []
    return response.json().get("items", [])

def print_rooms(rooms):
    for rooms in rooms:
        print("Available Room: ", rooms["title"])


def select_room(rooms):
    while True:
        name = input("Enter the name of the room you want to select: ")
        for room in rooms:
            if name.lower() in room["title"].lower():
                print(f"Selected Room: {room['title']}")
                return room["id"]
        print("Room not found. Please try again.")


def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": room_id, "max": 1}
    headers = {"Authorization": token}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None, None

    data = response.json().get("items", [])
    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")


def send_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    data = {
        "roomId": room_id,
        "text": message
    }
    requests.post(url, headers=headers, data=json.dumps(data))

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "limit": 1, "appid": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return f"Could not find coordinates for city: {city}"

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": location["lat"],
        "lon": location["lon"],
        "units": "metric",
        "appid": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Sorry, I could not retrieve the weather data."
    weather = response.json()

    return (
        f"City: {weather['name']}, Country: {weather['sys']['country']}\n"
        f"Temperature: {weather['main']['temp']}°C\n"
        f"Description: {weather['weather'][0]['description']}\n"
        f"Humidity: {weather['main']['humidity']}%\n"
        f"Wind Speed: {weather['wind']['speed']} m/s"
    )

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = "http://api.openweathermap.org/geo/1.0/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "limit": 1,
        "appid": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)

    if response.status_code != 200:
        return "Iss location could not be retrieved."

    data = response.json()

    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location["name"]

    return (
        f"Current ISS Location:\n"
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
        f"Place: {place}"
    )

    data = response.json()

    lat = data[ "iss_position"]["latitude"]
    lon = data[ "iss_position"]["longitude"]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location["name"]

    return (
        f"Current ISS Location:\n"
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
        f"Place: {place}"
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main():

    token = get_webex_token()

    weather_key = get_api_key(
        "openweather API key",
        "50922935a8514f2227993bbd1bb6e3f6"
    )

    rooms = get_rooms(token)

    if not rooms:
        print("No rooms available or failed to fetch rooms. Exiting.")
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(f"Received message: {message_text}")

            if not message_text.startswith("Could not receive message"):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith("/weather"):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()