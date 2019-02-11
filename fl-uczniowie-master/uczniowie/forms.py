# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class UczenForm(FlaskForm):
    id = HiddenField('Uczeń id')
    imie = HiddenField('Imie id')
    nazwisko = HiddenField('Nazwisko id')
    klasa = HiddenField('Klasa id')


class DodajForm(FlaskForm):
    id = HiddenField('Pytanie id')
    imie = StringField('Imie:',
                       validators=[Required(message=blad1)])
    nazwisko = StringField('Nazwisko:',
                           validators=[Required(message=blad1)])
    klasa = SelectField('Klasa', coerce=int)


class DodajKlaseForm(FlaskForm):
    klasa = StringField('Klasa', validators=[Required(message=blad1)])
    rok_nab = IntegerField('rok naboru', validators=[Required(message=blad1)])
    rok_mat = IntegerField('rok matury', validators=[Required(message=blad1)])
