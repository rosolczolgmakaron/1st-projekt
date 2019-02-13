# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, HiddenField, FieldList
from wtforms import SelectField, BooleanField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField('Klasa id')
    klasa = StringField('Klasa', validators=[Required(message=blad1)])
    rok_nab = IntegerField('rok naboru', validators=[Required(message=blad1)])
    rok_mat = IntegerField('rok matury', validators=[Required(message=blad1)])


class UczenForm(FlaskForm):
    id = HiddenField('Imie id')
    imie = StringField('Imie:',
                       validators=[Required(message=blad1)])
    nazwisko = StringField('Nazwisko:',
                           validators=[Required(message=blad1)])
    plec = BooleanField('Plec')
    klasa = SelectField('Klasa', coerce=int)
