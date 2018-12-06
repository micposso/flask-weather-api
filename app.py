from datetime import datetime
from datetime import timedelta
import requests
from flask import Flask, render_template, request

currentDT = datetime.now()
timeChicago = currentDT - timedelta(hours=1)
timeLosAngeles = currentDT - timedelta(hours=3)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])

def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b2efe5292c39fd73143a306f48ffcd6f'

    ny = requests.get(url.format('New York')).json()
    ch = requests.get(url.format('Chicago')).json()
    la = requests.get(url.format('Los Angeles')).json()

    cities_weather = {
        'location1': {
            'city' : 'New York',
            'temperature' : ny['main']['temp'] ,
            'icon' : ny['weather'][0]['icon'],
            'time' : currentDT.strftime("%I:%M %p")
        },
        'location2': {
            'city' : 'Chicago',
            'temperature' : ch['main']['temp'] ,
            'icon' : ch['weather'][0]['icon'],
            'time' : timeChicago.strftime("%I:%M %p")
        },
        'location3': {
            'city' : 'Los Angeles',
            'temperature' : la['main']['temp'] ,
            'icon' : la['weather'][0]['icon'],
            'time' : timeLosAngeles.strftime("%I:%M %p")
        }
    }

    return render_template('template.html', weather=cities_weather)