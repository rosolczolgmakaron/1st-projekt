#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#
from flask import Flask, g
from flask import render_template
from modele import *

app = Flask(__name__)
app.config.update(dict(
    SEKRETNY_KLUCZ='bardzotajnyklucz',
    TYTUL='Czat'
))


@app.before_request
def before_request():
    g.db = baza
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    pytania = Pytanie.select().join(Odpowiedz).distinct().order_by(Pytanie.id)
    return render_template('quiz.html', query=pytania)


@app.route('/klasa')
def klasa():
    return render_template('klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
