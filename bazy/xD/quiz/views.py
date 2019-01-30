#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py
#  
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask import abort
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

# widok QUIZ
@app.route('/quiz', methods = ['GET', 'POST'])
def quiz():
    print(request.form)
    if request.method == 'POST':
        wynik = 0
        for pid, oid in request.form.items():
            odp = Odpowiedz().get(Odpowiedz.id == int(oid)).odpok
            if odp:
                wynik += 1

    pytania = Pytanie.select().join(Odpowiedz).distinct().order_by(Pytanie.id)
    return render_template('quiz.html', query = pytania)

def flash_errors(form):
    """Odczytanie wszystkich błędów formularza i przygotowanie komunikatów"""
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = DodajForm()
    form.kategoria.choices = [(k.id, k.kategoria) for k in Kategoria.select()]
    
    if form.validate_on_submit():
        print(form.data)
        p = Pytanie(pytanie=form.pytanie.data, kategoria=form.kategoria.data)
        p.save()
        for o in form.odpowiedzi.data:
            odp = Odpowiedz(odpowiedz=o['odpowiedz'],
                            pytanie=p.id,
                            odpok=int(o['odpok']))
            odp.save()
        flash("Dodano pytanie!", "sukces")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template('dodaj.html', form=form)

def get_or_404(pid):
    try:
        p = Pytanie.get_by_id(pid)
        return p
    except Pytanie.DoesNotExist:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/usun/<int:pid>', methods=['GET', 'POST'])
def usun(pid):
    """Usuwanie pytania o podanym id"""
    p = get_or_404(pid)
    if request.method == 'POST':
        flash('Usunięto pytanie {}'.format(p.pytanie), 'sukces')
        for o in Odpowiedz.select().where(Odpowiedz.pytanie == p.id):
            o.delete_instance()
        p.delete_instance()
        return redirect(url_for('index'))
    return render_template('pytanie_usun.html', pytanie=p)
