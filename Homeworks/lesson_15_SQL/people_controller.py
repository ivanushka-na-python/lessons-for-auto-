from database import connection, cursor



class PeopleController:
   
   @classmethod
   def create_people(cls, name, surname):
      query = '''
      INSERT INTO
         people (name, surname) 
      VALUES 
         (%s, %s);
      '''
      cursor.execute(query, (name, surname))
      connection.commit()
      connection.close()


   @classmethod
   def read_people(cls):
      query = '''
      SELECT
         * 
      FROM 
         people;
      '''
      cursor.execute(query)
      data = cursor.fetchall()
      connection.close()
      return data

   @classmethod
   def read_one_people(cls, name, surname):
      query = f'''
      SELECT 
         * 
      FROM 
         people 
      WHERE 
         name = '{name}' 
      AND 
         surname = '{surname}';
      '''
      cursor.execute(query)
      data = cursor.fetchone()
      connection.close()
      return data


   @classmethod
   def update_people(cls, id, name, surname):
      query = f'''
      UPDATE 
         people 
      SET 
         name = '{name}', 
         surname = '{surname}' 
      WHERE 
         id = {id};
      '''
      cursor.execute(query)
      connection.commit()
      connection.close()
      
   @classmethod
   def delete_people(cls, id):
      query = f"DELETE FROM people WHERE id = {id};"
      cursor.execute(query)
      connection.commit()
      connection.close()