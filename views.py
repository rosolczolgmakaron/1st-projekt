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


@app.route('/lista_klas')
def lista_klas():
    klasa = Klasa.select()
    return render_template('lista_klas.html', query=klasa)


@app.route('/dodaj_ucznia', methods=['GET', 'POST'])
def dodaj_ucznia():
    form = UczenForm()
    form.klasa.choices = [(k.id, k.klasa) for k in Klasa.select()]

    if form.validate_on_submit():
        print(form.data)
        p = Uczen(imie=form.imie.data, nazwisko=form.nazwisko.data, plec=form.plec.data, klasa=form.klasa.data)
        p.save()
        flash("Dodano ucznia!", "sukces")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template('dodaj_ucznia.html', form=form)


@app.route('/dodaj_klasy', methods=['GET', 'POST'])
def dodaj_klasy():
    form = KlasaForm()
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


def get_or_404(obiekt, pid):
    try:
        o = obiekt.get_by_id(pid)
        return o
    except Klasa.DoesNotExist:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/klasa_usun/<int:pid>', methods=['GET', 'POST'])
def klasa_usun(pid):
    """Usuwanie klasy o podanym id"""
    k = get_or_404(Klasa, pid)
    if request.method == 'POST':
        flash('Usunięto klase {}'.format(k.klasa), 'sukces')
        for o in Klasa.select().where(Klasa.klasa == k.id):
            o.delete_instance()
        k.delete_instance()
        return redirect(url_for('lista_klas'))
    return render_template('klasa_usun.html', klasa=k)


@app.route('/klasa_edytuj/<int:pid>', methods=['GET', 'POST'])
def edytuj(pid):
    """edycja klas"""
    k = get_or_404(pid)
    form = DodajForm(obj=k)
    if form.validate_on_submit():
        k.klasa = form.klasa.data
        k.rok_nab = form.rok_nab.data
        k.rok_mat = form.rok_mat.data
        k.save()

        flash("Zaktualizowano klase: {}".format(form.klasa.data))
        redirect(url_for('lista_klas'))
    else:
        flash_errors(form)

    return render_template('klasa_edytuj.html', form=form)
