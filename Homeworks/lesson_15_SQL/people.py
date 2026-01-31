from database import connection, cursor


def create_people(name, surname):
   query = f"INSERT INTO people (name, surname) VALUES ('{name}', '{surname}');"
   cursor.execute(query)
   connection.commit()
   connection.close()
