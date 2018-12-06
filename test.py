city = {
    'west': 'New York'
}

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b2efe5292c39fd73143a306f48ffcd6f'

r = url.format(city['west'])

print(r);