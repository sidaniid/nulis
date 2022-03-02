import BotNulis
from flask
import Flask, render_template, request, jsonify
from PIL
import Image, ImageDraw, ImageFont
import time
import requests
import os

app = Flask(__name__)

waktuFile = time.strftime("%y%m%d-%H%M%S")

@app.route('/')
def index():
    return 'Hello :)'

@app.route('/write')
def write():
    text = request.args.get('text')
if not text:
    return jsonify({
        'error': True,
        'msg': 'Must add argument text'
    })

mpaper = request.args.get('paper')
if not mpaper:
    mpaper = 1

pfont = request.args.get('font')
if not pfont:
    pfont = 1

header = request.args.get('header')
if not header:
    header = ''

date = request.args.get('date')
if not date:
    date = ''

bot = BotNulis(text, int(mpaper), int(pfont), header, date)
result = bot.start()
return jsonify(result)
