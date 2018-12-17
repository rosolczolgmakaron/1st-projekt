#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#
from flask import Flask
from flask import render_template, request, redirect, url_for
from modele import *
from forms import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lista')
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', query=pytania)


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


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = DodajForm()
    form.kategoria.choices = [(k.id, k.kategoria) for k in Kategoria.select()]
    if form.validate_on_submit():
        print(form.data)
        p = Pytanie(pytanie=form.pytanie.data, kategoria=form.kategoria.data)
        p.save()
        for o in form.odpowiedzi.data:
            odp = Odpowiedz(odpowiedz=o['odpowiedz'], pytanie=p.id, odpok=int(o['odpok']))
            odp.save()
        return redirect(url_for('index'))
    return render_template('dodaj.html', form=form)
