# coding=utf-8

import os
import random

from flask import Flask

app = Flask(__name__)

def lucky_color():
    return os.getenv('COLOR') or "purple"

def lucky_number():
    return random.randint(1,7)

@app.route('/')
def index():
    return "Your lucky colored number is %s — %s!" % (lucky_number(), lucky_color())
