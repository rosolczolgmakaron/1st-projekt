#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship

# klasa bazowa
BazaModel = declarative_base()


class Osoba(BazaModel):
    __tablename__ = 'osoba'
    id = Column(Integer, primary_key=True)
    login = Column(String(100), nullable=False)
    haslo = Column(String(100), nullable=False)
    zadania = relationship('Zadanie', backref='osoba')


class Zadanie(BazaModel):
    __tablename__ = 'zadanie'
    id = Column(Integer, primary_key=True)
    tresc = Column(String(100), nullable=False)
    datad = Column(DateTime, default=func.now())
    wykonane = Column(Boolean, default=False)
    osoba_id = Column(Integer, ForeignKey('osoba.id'))
