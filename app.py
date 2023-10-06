from flask import Flask, url_for, redirect
from flask import request
from urllib.request import urlopen
from markupsafe import escape
import json
from flask import render_template
import wcodeparsers as wcp

app = Flask(__name__)

@app.route("/")
def hello():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=53.9&longitude=27.5667&current_weather=true'
    data_json = json.loads(urlopen(url).read())
    cw = data_json['current_weather']
    return render_template('main.html', temp = cw['temperature'], wsp = cw['windspeed'],
                           wd = wcp.parse_direction(cw['winddirection']), w = wcp.parse_weathercode(cw['weathercode']))

@app.route("/schedule")
def schedule():
    return render_template('timeselect.html')

@app.route("/show")
def show():
    selection = request.args.getlist('select')
    url = 'https://api.open-meteo.com/v1/forecast?latitude=53.9&longitude=27.5667&hourly=temperature_2m,weathercode,windspeed_10m,winddirection_10m'
    data_json = json.loads(urlopen(url).read())
    h = data_json['hourly']
    w = []
    for i in selection:
        w.append((wcp.parse_time(int(i)), h['temperature_2m'][int(i)], wcp.parse_weathercode(h['weathercode'][int(i)]),
                  h['windspeed_10m'][int(i)], wcp.parse_direction(h['winddirection_10m'][int(i)])))
        w.append((wcp.parse_time(int(i) + 24), h['temperature_2m'][int(i) + 24], wcp.parse_weathercode(h['weathercode'][int(i) + 24]),
                  h['windspeed_10m'][int(i) + 24], wcp.parse_direction(h['winddirection_10m'][int(i)] + 24)))
        w.append((wcp.parse_time(int(i) + 48), h['temperature_2m'][int(i) + 48], wcp.parse_weathercode(h['weathercode'][int(i) + 48]),
                  h['windspeed_10m'][int(i) + 48], wcp.parse_direction(h['winddirection_10m'][int(i) + 48])))
    return render_template('show.html', w = w)
    #return redirect(url_for('hello_world'))
