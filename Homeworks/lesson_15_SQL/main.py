from people_controller import PeopleController
from people import People
from api import SocketApi
import os

def main():


   try:
      while True:
         client = SocketApi(2023)

         if client.method == 'GET':
            match client.route:
               case '/people':
                  data = PeopleController.read_people()
                  client.send_json(data)
               case '/people/18':
                  data = PeopleController.read_one_people('Dima', 'Kvadrat')
                  client.send_json(data)
               case '/macos':
                  client.send_raw_html('<h1>macos<h1/>')
         

   except KeyboardInterrupt:
      print('Shutdown...')


if __name__ == '__main__':
   main()