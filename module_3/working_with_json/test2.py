# import datetime
# import json
#
# import requests
# import datetime
#
# KEY = "gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"
# #
# # url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"
# #
# # resp = requests.get(url)
# # print(resp.status_code)
# #
# # with open("weather.json", "w") as f:
# #     json.dump(json.loads(resp.text), f)
# #
# # # Method2
# #
# url = f"https://api.freecurrencyapi.com/v1/latest"
#
# resp = requests.get(
#     url,
#     params={"apikey": KEY}
# )
# print(resp.text)
# res = json.loads(resp.text)
#
#
# def get_timelines(res):
#     return res.get("timelines")
#
#
# def get_daily_data(res, timelines_data):
#     return get_timelines(res).get("daily")
#
#
# response = json.loads(resp.text)
# for day in get_daily_data(response):
#     print(day.get("time"))
#     average_temperature = None
#     day_values = day.get("values")
#     if day_values:
#         average_temperature = day.get("values").get(temperatureAvg)
#         time = day.get("time")
#
#     datetime.strftime(time, "%Y-%m%dT%H:%M:%SZ")
#     print(datetime.strftime("%Y/%m/%d"))
#     print(day.get("time"))
#     print(f"date:{date.strftimetime('%Y.%m.%d')}\n average temperature:{average_temperature}")
#
#     print(average_temperature)
#
# def convert_to_datetime(date:str):
#     return datetime.strptime(time,"%Y-%m-%dT%")
#
# def get_hourly_temperature(timelines,date_):
#     return [{
#         "time":hour_data.get("time")
#         "temperature":hour_data["values"].get("temperature")
#     }
#         for hour_data in res.get("hourly"):
#     if convert_to_datetime(hourly_data.get("time")).date()==date_.date()
#
#     ]
#
# #
# # url='https://currency-converter5.p.rapidapi.com/currency/convert'
# # KEY='8499912dd7msh55277bc92f8364fp17837fjsnbe947087faeb'
# # res = requests.get(
# #     url,
# #     params={"apikey": KEY}
# # )
# #
# # print(res)
# # import requests
# #
# # APIKEY = 'ZQ48KUlOHW4H7bnsvgNlF02Z06kwKvoB'
# #
# # url = f"https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey={APIKEY}"
# #
# # headers = {"accept": "application/json"}
# #
# # response = requests.get(url, headers=headers)
# # with open("weather/weather.json", "w") as f:
# #     data = json.dump(json.loads(response.text),f)
#
# countries={
#     "Uzbekistan":{
#         "cities":["Tashkent","Bukhara"]
#     }
#
# }
