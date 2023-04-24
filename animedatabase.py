import sqlite3
import random

from texttable import Texttable


class AnimeDatabase:
    def __init__(self, name):
        self._name = name
        self._con = None
        self._cur = None

    def connect(self):
        self._con = sqlite3.connect(f'{self._name}')
        self._cur = self._con.cursor()

    def disconnect(self):
        self._con.close()
        self._cur.close()

    def create_table(self):
        self._cur.execute("""
            create table if not exists animes
                (
                id integer primary key autoincrement,
                name_ text,
                sport text,
                finished_airing integer,
                rating real,
                seen integer default  0
                );
        """)
        self._con.commit()

    def insert_row(self, name, sport, finished_airing, rating):
        self._cur.execute("""
            insert into animes (name_,sport,finished_airing,rating)
            values (?,?,?,?);
            """, (name, sport, finished_airing, rating))
        self._con.commit()

    def delete_row(self, anime_id):
        self._cur.execute("delete from animes where id=?", (anime_id,))
        self._con.commit()

    def mark_as_seen(self, anime_id):
        self._cur.execute("update animes set seen=1 where id=?", (anime_id,))
        self._con.commit()

    def select_random(self):
        self._cur.execute("select * from animes where finished_airing=1 and seen=0")
        rows = self._cur.fetchall()
        if not rows:
            print("An anime that has finished airing and is not seen by you could not be found")
        else:
            print(self.__print_table([random.choice(rows)]))

    def select_by_sport(self, sport):
        res = self._cur.execute("select * from animes where sport=?", (sport,))
        print(self.__print_table(res.fetchall()))

    def view_all(self):
        res = self._cur.execute("select * from animes")
        print(self.__print_table(res.fetchall()))

    def __print_table(self, data):
        table = Texttable()
        table.set_cols_align(["l", "r", "c", "c", "r", "c"])
        table.set_cols_valign(["t", "m", "b", "b", "m", "b"])
        table.add_rows([["Id", "Name", "Sport", "Finished Airing", "Rating", "Seen"]])
        for row in data:
            table.add_row(row)
        return table.draw()
