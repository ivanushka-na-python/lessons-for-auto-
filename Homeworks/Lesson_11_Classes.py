# классы в питоне 
class Group: # не ставим скобки, потому что материнский класс + это абстрактный класс, потому что в нем есть абстрактный метод 
   pupils = True
   school_name = 42
   director = 'Ivanovna'

   def __init__(self, title, pupils_count, group_leader): # метод, который запустится когда мы ссылаемся на объект класса от обычного объекта
      # кароч это индивидуальные атрибуты для объектов first_a и т.д. которые мы передаем через связывание объекта с классом
      self.title = title
      self.pupils_count = pupils_count
      self.group_leader = group_leader
      
      pass

   def study(self): # это кароч метод - хз че это такое, типо в параметре нужно указать self
      print('sit and read')
   def move(self):
      pass # (это абстрактный метод) говорим что в методах дочерних классов будет реализовано, однако сейчас не реализуется

class PrimaryGroup(Group): # ставим скобки, потому что этот класс дочерний от материнского Group 
   max_age = 11 
   min_age = 6 
   area = 'left'

   def __init__(self, title, pupils_count, group_leader, room): # в дочерний класс нужно затащить материнские атрибуты + добавить свой, который будет тянуться из этого класса 
      super().__init__(title, pupils_count, group_leader)
      self.room = room

   def move(self):
      print('run fast')

class HighGroup(Group):
   max_age = 18 
   min_age = 14 
   def move(self):
      print('go slowly')

# объект класса = объект типа = представитель класса = экземпляр класса  

first_a = PrimaryGroup('1a', 42, 'IA', 34) # объект класса PrimaryGroup
first_b = PrimaryGroup('1b', 20, 'VA', 35) # передаем индивидуальные атрибуты в метод __init__ дочернего метода 
eleven_a = HighGroup('11a', 10, 'UT')

# можем обращаться к атрибутам материнского класса через дочерний класс + через точку обращаемся к атрибутом самого класса 
print(first_a.pupils)
print(first_a.area)
print(eleven_a.max_age)
print(first_a.group_leader) #
print(eleven_a.group_leader)
print(first_b.room)


first_a.study()
eleven_a.study()
first_a.move()
eleven_a.move()

