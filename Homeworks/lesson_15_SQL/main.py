from people import create_people


def main():
   name = input('name ').strip()
   surname = input('surname ').strip()
    
   create_people(name, surname)



if __name__ == '__main__':
   main()