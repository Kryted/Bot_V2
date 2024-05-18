from config import ROOT_DIR
import json

def reading_employee():
    """
    считывает данные с json файла
    :return: словарь с сотрудниками
    """
    with open('employee.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def write_employee(employee):
    """
    записывает данные сотрудников в json файл
    :param employee: словарь сотруников
    """
    with open('employee.json', 'w', encoding='utf-8') as file:
        json.dump(employee, file)


def add_new_employee(id_tg, fio, id_alfa):
    """
    добавляет нового сотрудника в словарь сотрудников
    :param id_tg: nik в телеграмме
    :param fio: фамилия и имя как в гугл таблице
    :param id_alfa: id в Альфабанке
    """
    dict_employee = reading_employee()    #считывает данные о сотрудниках
    dict_employee[id_tg] = [fio, id_alfa]    #добавляетн ового сотрудниках
    write_employee(dict_employee)    #перезаписывает данные о сотрудниках
    return True    #сотрудник добавлен

def delete_old_employee(id_tg, fio, id_alfa):
    """
    удалить старого сотрудника из словаря сотрудников
    :param id_tg: nik в телеграмме
    :param fio: фамилия и имя как в гугл таблице
    :param id_alfa: id в Альфабанке
    идет проверка данных, если такой id_tg есть, и fio с id_alfa введены верно данные записывааются,
     и возвращается true, иначе False
    """
    dict_employee = reading_employee()    #считывает данные о сотрудниках
    if id_tg in dict_employee and dict_employee[id_tg] == [fio, id_alfa]:
        del dict_employee[id_tg]    #удаляет сотрудниках
        write_employee(dict_employee)    #перезаписывает данные о сотрудниках
        return True    #сотрудник удален
    return False    #данные введены не венрно, или такого сотрудника не существует


def search_employee_data(username_tg):
    """
    ищет данные сотрудника по id телеграмма
    :param username_tg: id телеграмма, достается из чата тг
    :return: данные о сотруднике (фио) для гугл таблицы
    """
    dict_employee = reading_employee()
    if username_tg in dict_employee:
        return dict_employee[username_tg][0]    #возвращает фио сотрудника
    return False    #этот сотрудник не зарегистрирован








# artem_employee = {"L_Art007": ['Артем Лазарев', 654321]}
# employee = {'tdryn4ik': ['Андрей Тарасов', 123456]}
# write_employee(employee)
# print(reading_employee())

# add_new_employee("L_Art007", 'Артем Лазарев', 654321)

print(search_employee_data('tdryn4ik'))