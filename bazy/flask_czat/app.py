#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, g
from flask import render_template

app = Flask(__name__)
app.config.update(dict(
    SEKRETNY_KLUCZ='bardzo fajny klucz',
    TYTUL='Czat'
))


@app.route('/')  # adres główny
def index():
    return render_template('index.html')


@app.route('/klasa')
def klasa():
    return render_template('klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
