import os
from dotenv import load_dotenv
load_dotenv()
import requests
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QLineEdit,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt
from urllib3.exceptions import HTTPError
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.city_input=QLineEdit(self)
        self.city_input.setPlaceholderText("   Enter city name")
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temp_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""QLabel,QPushButton{
                           font-family:Times New Roman;
                           font-size:40px;
                           font-weight:bold;}
                           QLineEdit{
                           font-size:50px;}
                           QPushButton{
                           color:white;
                           background-color:red;
                           }""")
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_input.setStyleSheet("font-weight:bold;")
        self.get_weather_button.clicked.connect(self.getweather)
    def getweather(self):
        api_key=os.getenv("API_KEY")
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data=response.json()
            if data["cod"]==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\n Please check your input")
                case 401:
                    self.display_error("Unauthorized:\n Invalid API key")
                case 403:
                    self.display_error("Forbidden:\n Access is denied")
                case 404:
                    self.display_error("Not found:\n City not found")
                case 500:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable\n Server is down")
                case 504:
                    self.display_error("Gateway Timeout:\n No response from the server")
                case _:
                    self.display_error(f"HTTP error occured \n {HTTPError}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\n Check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Connection timeout:\n The request time out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many directs:\n Check the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error \n{req_error}")
    def display_error(self,message):
        self.temp_label.setText(message)
        self.description_label.clear()
        self.emoji_label.clear()

    def display_weather(self,data):

        temp_k=data["main"]["temp"]
        temp_c=temp_k-273.15

        self.temp_label.setText(f"{temp_c:.0f}°C")
        weather_description=data["weather"][0]["description"]
        self.description_label.setText(f"{weather_description}")
        weather_id=data["weather"][0]["id"]
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.emoji_label.setStyleSheet("font-size:200px;")
        self.temp_label.setStyleSheet("font-size:50px;")

    @staticmethod
    def get_emoji(weather_id):
        if 200<= weather_id <= 232:
            return "🌩️ "
        elif 300 <= weather_id <= 321:
            return "🌧️"
        elif 500 <= weather_id <= 531:
            return "☔️"
        elif 600 <= weather_id <= 622:
            return "⛄"
        elif 701 <= weather_id <= 741:
            return "😶‍🌫️"
        elif  weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "💭"
        else:
            return ""
def main():
    app=QApplication(sys.argv)
    weatherapp=WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()