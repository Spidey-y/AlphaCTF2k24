from typing import Union
from neo4j import GraphDatabase
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

class MovieDetails:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.clear_database()
        self.initialize_database()

    def close(self):
        self.driver.close()
        
    def clear_database(self):
        with self.driver.session() as session:
            session.write_transaction(self._clear_database)

    def initialize_database(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_data, title="The Matrix", release_year=1999)
            session.write_transaction(self._create_data, title="Interstellar", release_year=2014)
            session.write_transaction(self._create_data, title="The Shawshank Redemption", release_year=1994)
            session.write_transaction(self._create_data, title="The Godfather", release_year=1972)
            session.write_transaction(self._create_data, title="Taxi Driver", release_year=1976)
            session.write_transaction(self._create_data, title="Drive", release_year=2011)
            session.write_transaction(self._create_flag, flag_value="AlphaCTF{N0_w4y_Y0u_h4ck3D_mY_m4trix}")

    @staticmethod
    def _clear_database(tx):
        tx.run("MATCH (n) DETACH DELETE n")

    @staticmethod
    def _return_data(tx):
        result = tx.run("MATCH (m:Movie) RETURN {title: m.title, release_year: m.release_year} AS res")
        return result.values()

    @staticmethod
    def _create_data(tx, title, release_year):
        result = tx.run("CREATE (m:Movie {title: $title, release_year: $release_year})", title=title, release_year=release_year)
        return result.values()

    @staticmethod
    def _create_flag(tx, flag_value):
        result = tx.run("CREATE (:Flag {value: $flag_value})", flag_value=flag_value)
        return result.values()

    @staticmethod
    def _search_movies(tx, search_term):
        query = (
            f"MATCH (m:Movie) WHERE toLower(m.title) CONTAINS toLower('{search_term}') "
            "RETURN {title: m.title, release_year: m.release_year} AS res"
        )
        result = tx.run(query)
        return result.values()

app = FastAPI()
uri = os.getenv('NEO4J_URI')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
obj = MovieDetails(uri, user, password)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1><a href=/docs>FastAPI</a></h1>"

@app.get("/data")
def read_item():
    with obj.driver.session() as session:
        result = session.write_transaction(obj._return_data)
    return result

@app.get("/search")
def search_movies(name: str):
    with obj.driver.session() as session:
        result = session.read_transaction(obj._search_movies, search_term=name)
    return result
