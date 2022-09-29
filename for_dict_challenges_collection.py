from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names_count = Counter([student['first_name'] for student in students])
for name in names_count:
    print(f'{name}: {names_count[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_count = Counter([student['first_name'] for student in students])
name_max = names_count.most_common(1)
print(f'Самое частое имя среди учеников: {name_max[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for numb, group in enumerate(school_students, 1):
    names_count = Counter([student['first_name'] for student in group])
    name_max = names_count.most_common(1)
    print(f'Самое частое имя в классе {numb}: {name_max[0][0]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for group in school:
    names = [student['first_name'] for student in group['students']]
    gend_count = Counter(['boy' if is_male[name] else 'girl' for name in names])
    print(f'Класс {group["class"]}: девочки {gend_count["girl"]}, мальчики {gend_count["boy"]}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
boys_class, boys_count = 'uncnown', 0
girls_class, girls_count = 'uncnown', 0
for group in school:
    names = [student['first_name'] for student in group['students']]
    gend_count = Counter(['boy' if is_male[name] else 'girl' for name in names])
    if gend_count['boy'] > boys_count:
        boys_class = group['class']
        boys_count = gend_count['boy']
    if gend_count['girl'] > boys_count:
        girls_class = group['class']
        girls_count = gend_count['girl']
print(f'Больше всего мальчиков в классе {boys_class}')
print(f'Больше всего девочек в классе {girls_class}') 
