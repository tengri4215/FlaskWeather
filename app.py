from flask import Flask
from urllib.request import urlopen
from markupsafe import escape
import json
from flask import render_template
import wcodeparsers as wcp

app = Flask(__name__)

@app.route("/")
def hello_world():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=53.9&longitude=27.5667&current_weather=true'
    data_json = json.loads(urlopen(url).read())
    print(data_json)
    cw = data_json['current_weather']
    return render_template('main.html', temp = cw['temperature'], wsp = cw['windspeed'],
                           wd = wcp.parse_direction(cw['winddirection']), w = wcp.parse_weathercode(cw['weathercode']))