import requests


def get_weather_info():
    PIKEY = 'ZQ48KUlOHW4H7bnsvgNlF02Z06kwKvoB'

    url = f"https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey={APIKEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    with open("weather/weather.json", "w") as f:
        data = json.dump(json.loads(response.text), f)

    try:
        select_city = text_filed.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description_ = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure_ = json_data["main"]["pressure"]
        humidity_ = json_data["main"]["humidity"]
        wind_ = json_data["wind"]["speed"]

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        wind.config(text=wind_)
        humidity.config(text=humidity_)
        description.config(text=description_)
        pressure.config(text=pressure_)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")