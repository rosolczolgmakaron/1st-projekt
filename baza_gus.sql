-- baza_gus.sql
drop table if exists miasta;
drop table if exists powierzchnia_miasta;
drop table if exists dane_demograficzne;

create table miasta (
    id_miasta integer primary key autoincrement,
    nazwa_miasta text(30),
    nazwqa_wojewodztwa text(30)
);
create table powierzchnia_miasta (
    id integer primary key autoincrement,
    powierzchnia_miasta decimal,
    powierzchnie_zielone decimal,
    data_aktualizacji date,
    id_miasta integer,
    foreign key (id_miasta) references miasta(id_miasta)
);

create table dane_demograficzne (
    id integer primary key autoincrement,
    liczba_mieszkancow integer,
    liczba_kobiet integer,
    grupa_wiekowa text(15),
    data_aktualizacji date,
    id_miasta integer,
    foreign key (id_miasta) references miasta(id_miasta)
);
--sqlite3 baza.db <baza_gus.sql
-- sqlite3 baza.db
-- sqlite>.table - wyświetla tabele
--sqlite3>.schema - wyświetla klauzule sql
--sqlite3>.quit - wychodzi z bazy
