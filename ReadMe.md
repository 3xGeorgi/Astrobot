# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also furhter investigate the application of Web Architecture and MVC design pattern in development of the Bot

---

##  Webex Messaging API (4 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | ` https://webexapis.com ` |
| Authentication Method | `Bearer token` |
| Endpoint to list rooms | `/v1/rooms` |
| Endpoint to get messages | `_______________________________` |
| Endpoint to send message | `_______________________________` |
| Required headers | `Authorization , Accept` |
| Sample full GET or POST request | `_______________________________` |

---

##  ISS Current Location API (2 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `"http://api.open-notify.org"` |
| Endpoint for current ISS location | `/iss-now.json` |
| Sample response format (example JSON) |  
```
Current ISS Location:
Latitude: 13.9435
Longitude: -104.8952
Place: Over Ocean / No Nearby City
```
|

---

##  Geocoding API (4 marks)

| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other -provide detail** |
| API Base URL | `http://api.openweathermap.org/geo/1.0/direct` |
| Endpoint for geocoding | `f"City: {weather['name']}, Country: {weather['sys']['country']}\n"
        f"Temperature: {weather['main']['temp']}°C\n"
        f"Description: {weather['weather'][0]['description']}\n"
        f"Humidity: {weather['main']['humidity']}%\n"
        f"Wind Speed: {weather['wind']['speed']} m/s"` |
| Endpoint for reverse geocoding | `_params = {
        "lat": location["lat"],
        "lon": location["lon"],
        "units": "metric",
        "appid": api_key
    }_` |
| Authentication method | `__Api authentication key____` |
| Required query parameters | `___q appid limit lon lat____________` |
| Sample request with latitude/longitude | `_______________________________` |
| Sample JSON response (formatted example) |  
```
City: Mogadishu, Country: SO
Temperature: 29.92°C
Description: broken clouds
Humidity: 70%
Wind Speed: 3.6 m/s
```
|

---
messaging

##  Weather API (3 marks)

| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | **OpenWeather** |
| API Base URL | `____https://api.openweathermap.org/geo/1.0/direct_____` |
| Endpoint for current weather | `___weather tag in webex messaging____________` |
| Authentication method | `______api auth keu______________` |
| Required query parameters | `_______lon lat______________` |
| Sample JSON response (formatted example) |   f"City: {weather['name']}, Country: {weather['sys']['country']}\n"
        f"Temperature: {weather['main']['temp']}°C\n"
        f"Description: {weather['weather'][0]['description']}\n"
        f"Humidity: {weather['main']['humidity']}%\n"
        f"Wind Speed: {weather['wind']['speed']} m/s"
```

```
|

---

##  Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details |
|---------|---------|
| Library used | `____datetime_____` |
| Function used to convert epoch | `___{datetime.fromtimestamp(weather['dt']).strftime('%d-%m-%Y %H:%M:%S')}\n_____` |
| Sample code to convert timestamp |  
```  
```
|
| Output (human-readable time) | `_
Time: 24-10-2026 08:34:52___` |

---

##  Extended Feature API ( 3 marks)

| Criteria | Details |
|---------|---------|
| API Provider | '_Nasa_' |
| API Base URL | `_https://science.nasa.gov__` |
| Endpoint | `___wp-json/wp/v2/apod-basic______` |
| Authentication method | `____Api key______` |
| Required query parameters | `_____hdurl_________` |
| Sample JSON response (formatted example) |  
```
<strong>Explanation:</strong> <a href="https://blogs.esa.int/rosetta/2014/10/14/mission-selfie-from-16-km/">This Rosetta spacecraft selfie</a> was snapped on October 7th, 2014. At the time the <a href="https://rosetta.esa.int/">comet-chasing spacecraft</a> was about 472 million kilometers from planet Earth, but only 16 kilometers from the surface of <a href="https://science.nasa.gov/image-article/apod-2021-november-13-rosettas-comet-in-gemini/">comet 67P/Churyumov-Gerasimenko</a>. Looming beyond the spacecraft near the top of the frame, dust and gas stream away from the comet's curious <a href="https://science.nasa.gov/image-article/apod-2014-august-7-rosettas-rendezvous/">double-lobed nucle...
```
|

--- 

##  Evaluation – Web Architecture, MVC Design & Security 

In this section, evaluate how web technologies, architecture, and design patterns have been applied in your **AstroBot**. Your responses must relate directly to your implementation and include reflection on your design decisions.

--- 

###  Web Architecture – Client–Server Model (3 marks)

Explain how the client–server model applies to your AstroBot:

- Identify the **client** 
/The python program
- Identify the **server(s)** 
/the api's that astrobot is pulling from, for example the openweather api
- Describe how data flows between:
  - User, AstroBot and APIs
1 user enters a command 2. program goes over what the user sent 3 bot thinks for a 5 seconds 4 the bot asks the api it was asked to request from 5 the user is able to see what the bot pulled in the webex app

Include a **simple block diagram** to illustrate this interaction.

####  Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate limiting, and Input validation (e.g., handling user commands safely), include examples from code where necessary to illustrate.

---
Api keys are used in order to verify that the python program is legitimate and is not spam, rate limits are implemented for a simmilar reason to prevent the bot from disturbing the flow of information to the servers. Validation is implemented in user commands in order to preventusers from inputing the wrong things in the bot, as well as to prevent the bot from doing things its not designed to do.

###  RESTful API Usage in Your Application (3 marks )

Explain how REST APIs are used in your AstroBot: 

- Describe how HTTP methods (GET, POST) are used  
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)  
- Describe how JSON responses are received and processed  

Note: Relate your explanation directly to your code for higher grade. 

Astrobot uses rest apis in the form of requests in order to get information such as the longitude and latitude of the iss when it is called to do so.


The program uses JSON files in order to transmit responses so that they are easily readable by the user

#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses, Avoiding excessive API calls

--- Astrobot checks links and returns error messages if the links are invalid, this is done so in the if response.status_code != 200: line in order to make sure that the response code is valid.

###  MVC Design Pattern in AstroBot (3 Marks)

Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation

| Component   | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model**  | Handles data retrieval and processes. get_city_coordinates is an example | 
| **View**   | Displays data to the user in readable format. send_message is an example | 
| **Controller** | If and Elif loop, makes sure that the user doesnt input invalid commands | 

---

### 📝 Reflection and Evaluation ( 8 marks )

Reflect on your AstroBot (400 words):

- How effective is your bot in meeting the Astronomy Club’s needs?  
- What design decisions worked well?  
- What challenges did you face when integrating APIs?  
- What security risks did you identify and how were they handled?  
- How could your solution be improved in the future?  

---

 **Tip:** Link your answers directly to your code and examples for higher marks.
### Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

###  Total: /40