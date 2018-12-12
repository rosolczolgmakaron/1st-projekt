#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#
from flask import Flask, g
from flask import render_template, request
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


# widok quiz
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    print(request.form)
    if request.method == 'POST':
        wynik = 0
        for pid, oid in request.form.items():
            odp = Odpowiedz().get_by_id(int(oid))
            print(odp)
    pytania = Pytanie.select().join(Odpowiedz).distinct().order_by(Pytanie.id)
    return render_template('quiz.html', query=pytania)


@app.route('/klasa')
def klasa():
    return render_template('klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
