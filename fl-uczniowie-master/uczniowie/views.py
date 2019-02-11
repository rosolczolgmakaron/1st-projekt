# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)


def flash_errors(form):
    """Odczytanie wszystkich błędów formularza i przygotowanie komunikatów"""
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))


@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')


@app.route('/lista')
def lista():
    imie = Uczen.select()
    return render_template('lista.html', query=imie)


@app.route('/dodaj_ucznia', methods=['GET', 'POST'])
def dodaj_ucznia():
    form = DodajForm()
    form.klasa.choices = [(k.id, k.klasa) for k in Klasa.select()]

    if form.validate_on_submit():
        print(form.data)
        p = Uczen(uczen=form.uczen.data, klasa=form.klasa.data)
        p.save()
        for o in form.uczen.data:
            ucz = uczen(imie=o['imie'],
                        nazwisko=o['nazwisko'],
                        uczen=p.id)
            ucz.save()
        flash("Dodano ucznia!", "sukces")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash_errors(form)


@app.route('/dodaj_klasy', methods=['GET', 'POST'])
def dodaj_klasy():
    form = DodajKlaseForm()
    form.klasa.choices = [(k.id, k.klasa) for k in Klasa.select()]

    if form.validate_on_submit():
        print(form.data)
        k = Klasa(klasa=form.klasa.data, rok_nab=form.rok_nab.data, rok_mat=form.rok_mat.data)
        k.save()
        for o in form.klasa.data:
            kl = Klasa(klasa=k.id,
                       rok_nab=k.id,
                       rok_mat=k.id,
                       )
            # kl = Klasa(klasa=o['klasa'],
            #            rok_nab=o['rok_nab'],
            #            rok_mat=o['rok_mat'],
            #            )
            kl.save()
        flash("Dodano klase!", "sukces")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template('dodaj_klasy.html', form=form)
