import csv
import os
import matplotlib.pyplot as plt
from people import Student
from school import SchoolClass


def make_test_files():
    # Видаляємо старі маленькі файли, щоб програма створила нові з великою кількістю дітей
    if os.path.exists('classes.csv'): os.remove('classes.csv')
    if os.path.exists('students.csv'): os.remove('students.csv')

    with open('classes.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['grade', 'letter'])
        writer.writerows([[1, 'А'], [7, 'А'], [7, 'Б'], [9, 'В'], [11, 'А']])

    with open('students.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['last_name', 'first_name', 'middle_name', 'birth_year', 'gender', 'average_grade', 'class_name'])
        writer.writerows([

            ['Ільницький', 'Тарас', 'Григорович', 2019, 'Х', 11.2, '1-А'],
            ['Нікітюк', 'Ліна', 'Василівна', 2019, 'Д', 11.9, '1-А'],
            ['Мельник', 'Дмитро', 'Ігорович', 2020, 'Х', 9.5, '1-А'],
            ['Бойко', 'Анна', 'Сергіївна', 2019, 'Д', 10.2, '1-А'],
            ['Ковальчук', 'Олексій', 'Петрович', 2020, 'Х', 8.7, '1-А'],
            ['Олійник', 'Марія', 'Олегівна', 2019, 'Д', 11.5, '1-А'],

            ['Степанюк', 'Іван', 'Якович', 2014, 'Х', 10.5, '7-А'],
            ['Леся', 'пашкевич', 'Петрівна', 2014, 'Д', 12.0, '7-А'],
            ['Кравченко', 'Артем', 'Віталійович', 2013, 'Х', 7.8, '7-А'],
            ['Поліщук', 'Діана', 'Олександрівна', 2014, 'Д', 9.2, '7-А'],
            ['Ткаченко', 'Владислав', 'Максимович', 2014, 'Х', 10.0, '7-А'],

            ['Хмельницький', 'Григорій', 'Савич', 2014, 'Х', 9.8, '7-Б'],
            ['Лисенко', 'Софія', 'Михайлівна', 2014, 'Д', 11.1, '7-Б'],
            ['Мороз', 'Ярослав', 'Юрійович', 2013, 'Х', 6.5, '7-Б'],
            ['Швець', 'Анастасія', 'Вадимівна', 2014, 'Д', 8.9, '7-Б'],
            ['Павленко', 'Микита', 'Андрійович', 2014, 'Х', 7.4, '7-Б'],

            ['Микита', 'Василь', 'Семенович', 2012, 'Х', 10.1, '9-В'],
            ['Симоненко', 'Олена', 'Анатоліївна', 2011, 'Д', 11.3, '9-В'],
            ['Козак', 'Богдан', 'Русланович', 2012, 'Х', 8.2, '9-В'],
            ['Шевчук', 'Вероніка', 'Дмитрівна', 2012, 'Д', 9.6, '9-В'],
            ['Марченко', 'Ілля', 'Євгенович', 2011, 'Х', 7.9, '9-В'],

            ['Тичина', 'Павло', 'Григорович', 2010, 'Х', 8.5, '11-А'],
            ['Гончар', 'Юлія', 'Володимирівна', 2009, 'Д', 11.7, '11-А'],
            ['Рябов', 'Кирило', 'Сергійович', 2010, 'Х', 9.0, '11-А'],
            ['Клименко', 'Ольга', 'Миколаївна', 2009, 'Д', 10.4, '11-А']
        ])


def load_data(school_obj):
    with open('classes.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            school_obj.add_class(SchoolClass(row['grade'], row['letter']))

    with open('students.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            st = Student(row['last_name'], row['first_name'], row['middle_name'],
                         row['birth_year'], row['gender'], row['average_grade'])
            for c in school_obj.classes_list:
                if c.get_class_name() == row['class_name']:
                    c.add_student(st)


def show_stats(school_obj):
    all_st = []
    for c in school_obj.classes_list:
        for s in c.students_list:
            all_st.append(s)

    total = len(all_st)
    print("\n--- СТАТИСТИКА: " + school_obj.name + " ---")
    print("a. Кількість учнів всього: " + str(total))

    if total == 0:
        return

    boys = 0
    for s in all_st:
        if s.gender == 'Х':
            boys += 1

    girls = total - boys
    print("b. Хлопців: " + str(round(boys / total * 100, 1)) + "%, Дівчат: " + str(round(girls / total * 100, 1)) + "%")
    print("c. Середня кількість у класі: " + str(round(total / len(school_obj.classes_list), 2)))

    max_c = school_obj.classes_list[0]
    min_c = school_obj.classes_list[0]
    for c in school_obj.classes_list:
        if len(c.students_list) > len(max_c.students_list):
            max_c = c
        if len(c.students_list) < len(min_c.students_list):
            min_c = c

    print("d. Макс учнів: " + str(len(max_c.students_list)) + " (" + max_c.get_class_name() + ")")
    print("e. Мін учнів: " + str(len(min_c.students_list)) + " (" + min_c.get_class_name() + ")")


def draw_plots(school_obj):
    all_st = []
    for c in school_obj.classes_list:
        all_st.extend(c.students_list)

    fig, axs = plt.subplots(2, 2, figsize=(11, 7))
    fig.suptitle('Графіки для заліку - ' + school_obj.name)

    grades_dict = {}
    for c in school_obj.classes_list:
        grades_dict[str(c.grade)] = grades_dict.get(str(c.grade), 0) + len(c.students_list)
    x1 = sorted(grades_dict.keys(), key=int)
    y1 = [grades_dict[g] for g in x1]
    axs[0, 0].bar(x1, y1, color='blue')
    axs[0, 0].set_title('Учні по паралелях')

    let_dict = {}
    for c in school_obj.classes_list:
        let_dict[c.letter] = let_dict.get(c.letter, 0) + len(c.students_list)
    x2 = sorted(let_dict.keys())
    y2 = [let_dict[l] for l in x2]
    axs[0, 1].bar(x2, y2, color='orange')
    axs[0, 1].set_title('Учні по вертикалях')

    years_dict = {}
    for s in all_st:
        years_dict[s.birth_year] = years_dict.get(s.birth_year, 0) + 1
    x3 = sorted(years_dict.keys())
    y3 = [years_dict[y] for y in x3]
    axs[1, 0].plot(x3, y3, marker='o', color='red', linestyle='-')
    axs[1, 0].set_title('За роками народження')

    x4 = []
    y4 = []
    for c in school_obj.classes_list:
        for s in c.students_list:
            x4.append(c.get_class_name())
            y4.append(s.average_grade)
    axs[1, 1].scatter(x4, y4, color='green', alpha=0.8)
    axs[1, 1].set_title('Оцінки від класів')

    plt.tight_layout()
    plt.show()