DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy
(
	id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT(20),
	nazwisko TEXT(25),
	kod STRING(10),
	miasto_z TEXT(25),
	ulica TEXT(30),
	data_u DATE,
	miasto_u TEXT(30)
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty
(
	id_pracownika INTEGER NOT NULL,
	typ_k BOOLEAN,
	kontakt STRING(15),
	uwagi TEXT(40),
	FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id_pracownika) ON DELETE NO ACTION ON UPDATE NO ACTION
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska
(
	id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
	stanowisko TEXT(25)
);

DROP TABLE IF EXISTS place;
CREATE TABLE place
(
	id_p INTEGER NOT NULL,
	id_s INTEGER NOT NULL,
	placa INTEGER,
	data_z DATE,
	FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika) ON DELETE NO ACTION ON UPDATE NO ACTION
	FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska) ON DELETE NO ACTION ON UPDATE NO ACTION
);
