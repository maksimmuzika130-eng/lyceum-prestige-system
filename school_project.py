import csv
from school import School
from people import Director, Teacher, Guard
from stats import make_test_files, load_data, show_stats, draw_plots


def main():
    make_test_files()

    my_lyceum = School("Васильківський ліцей Престиж №9")

    print("================== СЦЕНАРІЙ 1 ==================")
    load_data(my_lyceum)
    show_stats(my_lyceum)
    draw_plots(my_lyceum)

    print("\n>>> Робимо перевід учнів до наступних класів...")
    my_lyceum.promote_all()

    show_stats(my_lyceum)
    draw_plots(my_lyceum)

    print("================== СЦЕНАРІЙ 2 ==================")
    d = Director("Шагова 0.П.", 21000, 20, 5)
    t1 = Teacher("Чепурний О.А.", 19000, 15)
    t2 = Teacher("ШАРАНОВА Н.М.", 19000, 5)
    g = Guard("Яловенко О.В.", 18000, 8)

    my_lyceum.add_employee(d)
    my_lyceum.add_employee(t1)
    my_lyceum.add_employee(t2)
    my_lyceum.add_employee(g)

    out_file = 'calculated_salaries.csv'
    with open(out_file, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ПІБ', 'Посада', 'Базова ставка', 'Зарплата'])

        print("\nРозраховані зарплати:")
        for emp in my_lyceum.employees_list:
            money = emp.calculate_salary()
            pos = emp.__class__.__name__
            w.writerow([emp.full_name, pos, emp.base_salary, money])
            print("- " + pos + ": " + emp.full_name + " | Зарплата: " + str(money) + " грн")

    print("\nУсі розрахунки записано в файл: " + out_file)

if __name__ == '__main__':
    main()