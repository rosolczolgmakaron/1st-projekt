CREATE TABLE kategorie(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kategoria TEXT
);

CREATE TABLE pytania(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pytanie TEXT,
    id_kat INTEGER NOT NULL,
    FOREIGN KEY (id_kat) REFERENCES kategorie(id)
);

CREATE TABLE odpowiedzi(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_p INTEGER NOT NULL,
    odpowiedz TEXT,
    odpok BOOL DEFAULT False,
    FOREIGN KEY (id_p) REFERENCES pytania(id)
);

