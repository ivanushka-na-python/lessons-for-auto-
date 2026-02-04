# faker - 
from faker import Faker

fake = Faker(locale='ru_RU')

for i in range(50): 
    print(fake.name())