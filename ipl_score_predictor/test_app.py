from app import home
import pickle
import joblib
import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')


def test_app():
    with app.app_context():
        assert home() == render_template('home.html',val='')