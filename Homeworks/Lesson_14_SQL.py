# database 
'''всегда проверять нужно ли условие для выполнения запроса'''

'''insert into students (name, second_name, group_id) values ('jorge', 'Washington', '1')''' 

'''select * from ... order by id desc limit 1, 1 (первое число - пропусти столько записей, второе число отдай столько записей )'''

'''update ... set name = 'new_name' where id = 2'''

'''delete from ... where id = 2'''

'''select * from students join books on students.id = books.taken_by_student_id'''