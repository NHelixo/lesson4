import os
import django
from django.core.exceptions import ObjectDoesNotExist

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
django.setup()

from app.models import Subject, Student, Teacher, Grade, Schedule, Class


def add_subject():
    print("\nДодавання предмета")
    name = input("Введіть назву предмета: ").strip().lower()

    if not name:
        print("Назва предмета не може бути порожньою")
        return
    
    # якщо предмет з такою назвою вже існує
    if Subject.objects.filter(name = name).exists():
        print("Предмет з такою назвою вже існує")
        return
    
    subject = Subject(name = name)
    subject.save()
    print(f"Предмет {name} успішно додано!")


def add_student():
    print("Додавання студента")
    name = input("Введіть ім'я студента: ").strip().lower()
    surname = input("Введіть прізвище студента: ").strip().lower()
    class_name = input("Введіть назву класу: ").strip().lower()

    if Student.objects.filter(name=name, surname=surname).exists():
        print("Учень з таким прізвищем і ім'ям вже існує!")

    if not all([name, surname, class_name]):
        print("Обов'язкові поля не можуть бути порожні!")
        return
    
    try:
        class_n = Class.objects.get(name = class_name)

    except ObjectDoesNotExist:
        print(f"Клас '{class_name}' не знайдено!")
        return

    Student(name=name, surname=surname, class_name=class_n).save()

    print(f"Учень з ім'ям {name} і прізвищем {surname} був доданий в клас {class_name}!")


def add_teacher():
    print("\nДодавання вчителя")
    name = input("Введіть ім'я вчителя: ").strip()
    surname = input("Введіть прізвище вчителя: ").strip()
    subject_name = input("Введіть назву предмета: ").strip()

    if not all([name, surname, subject_name]):
        print("Обов'язкові поля не можуть бути порожніми!")
        return

    # дивимось чи є в "школі" предмет, який буде викладати новий вчитель
    try:
        subject = Subject.objects.get(name = subject_name)
    except ObjectDoesNotExist:
        print(f"Предмет '{subject_name}' не знайдено!")
        return

    # створюємо та зберігаємо вчителя
    try:
        teacher = Teacher(
            name=name,
            surname=surname,
            subject=subject
        )
        teacher.save()
        print(f"Вчитель '{name} {surname}' успішно додано!")
    except Exception as e:
        print(f"Помилка при додаванні вчителя: {e}")


def add_class():
    print("Додавання класа")
    name = input("Введіть назву класу: ")
    
    if not name:
        print("Назва не може бути порожня!")
        return

    if Class.objects.filter(name = name).exists():
        print("Клас з такою назвою вже існує!")
        return

    Class(name=name).save()
    print("Клас додано!")


def add_grade():
    print("Додавання оцінки")

    grade = input("Введіть оцінку: ")
    subject = input("Введіть предмет: ")
    student_id = input("Введіть id студента: ")

    if not all([grade, subject, student_id]):
        print("Обов'язкові поля не можуть бути порожні!")

    try:
        subject = Subject.objects.get(name = subject)
    except ObjectDoesNotExist:
        print(f"Предмет '{subject}' не знайдено!")
        return

    try:
        student = Student.objects.get(id = student_id)
    except ObjectDoesNotExist:
        print(f"Учня з id: '{student}' не знайдено!")
        return

    Grade(grade=grade, subject=subject, student=student).save()
    print(f"Оцінку {grade} додано учню з id: {student_id}!")


def add_schedule():
    print("Додавання предмета в розклад")
    
    class_n = input("Введіть клас: ")
    subject = input("Введіть предмет: ")
    teacher = input("Введіть викладача: ")
    weekday = input("Введіть день тижня: ").lower()
    lesson_num = int(input("Введіть номер уроку: "))

    if Schedule.objects.filter(weekday=weekday, lesson_num=lesson_num).exists():
        print(f"Урок №{lesson_num} у {weekday} вже існує!")
        return
    
    try:
        class_name = Class.objects.get(name=class_n)
    except ObjectDoesNotExist:
        print(f"Клас з назвою '{class_n}' не знайдено!")

    try:
        subject_name = Subject.objects.get(name=subject)
    except ObjectDoesNotExist:
        print(f"Предмет з назвою '{subject}' не знайдено!")    

    try:
        teacher_name = Teacher.objects.get(name=teacher)
    except ObjectDoesNotExist:
        print(f"Викладача з ім'ям '{teacher}' не знайдено!")

    Schedule(class_name=class_name, subject=subject_name, teacher=teacher_name, weekday=weekday, lesson_num=lesson_num).save()
    print(f"Предмет '{subject}' в класі '{class_n}' який викладає вчитель {teacher} успішно додано до розкладу!")



def main():
    while True:
        print("\nКонсольний інтерфейс управління шкільним розкладом")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вийти")

        choice = input("Виберіть опцію (1-7): ").strip()

        if choice == '1':
            add_subject()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            add_class()
        elif choice == '4':
            add_student()
        elif choice == '5':
            add_schedule()
        elif choice == '6':
            add_grade()
        elif choice == '7':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")


if __name__ == '__main__':
    main()
