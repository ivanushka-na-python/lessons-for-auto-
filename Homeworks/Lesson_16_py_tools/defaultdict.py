import os
import collections
# print(os.listdir('.'))  # Покажет все файлы в текущей папке



file_path = os.path.join(os.path.dirname(__file__), 'test4.txt')
with open(file_path) as file_reading:
    file = list(map(lambda x: x.replace('\n', ''), file_reading.readlines())) # убрали /n для перевода на новую строку который 

names_and_nums = collections.defaultdict(list)
for line in file:
    name, num = line.split(':')
    names_and_nums[name].append(num)

print(names_and_nums)
