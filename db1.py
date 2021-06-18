import sqlalchemy as db

engine = db.create_engine('sqlite:///sakila.db')
connection = engine.connect()
metadata = db.MetaData()
filmTable = db.Table('film', metadata, autoload=True, autoload_with=engine)

while True:

    print("1. Lista alla filmer")
    print("2. Skapa ny film")
    print("3. Uppdatera film")
    print("0. Avsluta")
    selection = input("Välj action")
    if selection == "0":
        break
    if selection == "1":
        s = filmTable.select().where(filmTable.c.film_id > 0)
        for film in connection.execute(s):
            length = film[filmTable.c.length]
            title = film[filmTable.c.title]
            release_year = film[filmTable.c.release_year]

            print(f"{title} {release_year}")

