import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=982a1a65e33b771f854328def04d75c4")

        except:
            print("No internet access")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        unit_symb = "C"
        if self.units == "imperial":
            unit_symb = "F"
        print(f"In {self.name} it is currently {self.temp} °{unit_symb}")
        print(f"Today's High: {self.temp_max} °{unit_symb}")
        print(f"Today's Low {self.temp_min} °{unit_symb}")

my_city = City("Delhi", 28.7041, 77.1025)
my_city.temp_print()
leela_city = City("Sikkim", 27.3516, 88.3239)
leela_city.temp_print()
dream_city = City("Helsinki", 60.1699, 24.9384)
dream_city.temp_print()