from config import ROOT_DIR
import json
import os
file_path = os.path.join(ROOT_DIR, "data", 'employee.json')
def reading_employee(file_path):
    """
    считывает данные с json файла
    :param file_path путь до файла с сотрудниками
    :return: словарь с сотрудниками
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def write_employee(employee, file_path):
    """
    записывает данные сотрудников в json файл
    :param file_path путь до файла с сотрудниками
    :param employee: словарь сотруников
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(employee, file)


def add_new_employee(id_tg, fio, id_alfa, file_path):
    """
    добавляет нового сотрудника в словарь сотрудников
    :param id_tg: nik в телеграмме
    :param fio: фамилия и имя как в гугл таблице
    :param id_alfa: id в Альфабанке
    :param file_path путь до файла с сотрудниками
    """
    dict_employee = reading_employee(file_path)    #считывает данные о сотрудниках
    dict_employee[id_tg] = [fio, id_alfa]    #добавляетн ового сотрудниках
    write_employee(dict_employee, file_path)    #перезаписывает данные о сотрудниках
    return True    #сотрудник добавлен

def delete_old_employee(id_tg, fio, id_alfa, file_path):
    """
    удалить старого сотрудника из словаря сотрудников
    :param id_tg: nik в телеграмме
    :param fio: фамилия и имя как в гугл таблице
    :param id_alfa: id в Альфабанке
    идет проверка данных, если такой id_tg есть, и fio с id_alfa введены верно данные записывааются,
     и возвращается true, иначе False
     :param file_path путь до файла с сотрудниками
    """
    dict_employee = reading_employee(file_path)    #считывает данные о сотрудниках
    if id_tg in dict_employee and dict_employee[id_tg] == [fio, id_alfa]:
        del dict_employee[id_tg]    #удаляет сотрудниках
        write_employee(dict_employee, file_path)    #перезаписывает данные о сотрудниках
        return True    #сотрудник удален
    return False    #данные введены не венрно, или такого сотрудника не существует


def search_employee_data(username_tg, file_path):
    """
    ищет данные сотрудника по id телеграмма
    :param username_tg: id телеграмма, достается из чата тг
    :param file_path путь до файла с сотрудниками
    :return: данные о сотруднике (фио) для гугл таблицы
    """
    dict_employee = reading_employee(file_path)
    if username_tg in dict_employee:
        return dict_employee[username_tg][0]    #возвращает фио сотрудника
    return False    #этот сотрудник не зарегистрирован




# print(reading_employee(file_path))    #тест функция выводит всех сотрудников

##### не тестить функцию ниже!!!
# write_employee({'tdryn4ik': ['Андрей Тарасов', 123456]}, file_path)    #тест функция добавляет нового сотрудника
#
# add_new_employee("L_Art007", 'Артем Лазарев', 654321, file_path)    #тест добавляет нового сотрудника в словарь сотрудников
#
# delete_old_employee("L_Art007", 'Артем Лазарев', 654321, file_path)    #тест удаляет сотрудника
#
# print(search_employee_data('tdryn4ik', file_path))  #ищет данные сотрудника по id телеграмма