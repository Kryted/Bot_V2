from src.functions import reading_employee, write_employee, add_new_employee, delete_old_employee, search_employee_data
from config import ROOT_DIR
import os
import pytest



file_path = os.path.join(ROOT_DIR, "tests", 'test_employee.json')

@pytest.fixture()
def test_reading_employee():    #фикстура считывает данные с json файла
    return reading_employee(file_path)


@pytest.fixture()
def test_write_employee():  #фикстура записывает данные сотрудников в json файл
    return write_employee({'tdryn4ik': ['Андрей Тарасов', 123456]}, file_path)

def tests_write_employee(test_write_employee, test_reading_employee):   #записывает данные сотрудников в json файл
    test_write_employee    #перезаписывает файл для тестов
    assert test_reading_employee == {'tdryn4ik': ['Андрей Тарасов', 123456]}

@pytest.fixture()
def test_add_new_employee():  #фикстура добавляет нового сотрудника в словарь сотрудников
    return add_new_employee("L_Art007", 'Артем Лазарев', 654321, file_path)    #добавляет нового сотрудника в словарь сотрудников


def tests_add_new_employee(test_write_employee, test_add_new_employee, test_reading_employee):#добавляет нового сотрудника в словарь сотрудников
    test_write_employee    #перезаписывает файл для тестов
    test_add_new_employee    #добавляет нового сотрудника
    assert test_reading_employee == {'tdryn4ik': ['Андрей Тарасов', 123456], 'L_Art007': ['Артем Лазарев', 654321]}    #проверяет словарь

@pytest.fixture()
def test_delete_old_employee():    #фикстура удалить старого сотрудника из словаря сотрудников
    return delete_old_employee("L_Art007", 'Артем Лазарев', 654321, file_path)

def tests_delete_old_employee(test_write_employee, test_add_new_employee, test_delete_old_employee, test_reading_employee):
    test_write_employee    #перезаписывает файл для тестов
    test_add_new_employee    #добавляет нового сотрудника
    test_delete_old_employee    #удаляет старого сотрудника
    assert test_reading_employee == {'tdryn4ik': ['Андрей Тарасов', 123456]}

@pytest.fixture()
def test_search_employee_data():
    return search_employee_data('tdryn4ik', file_path)

def tests_search_employee_data(test_write_employee, test_add_new_employee, test_search_employee_data):
    test_write_employee    #перезаписывает файл для тестов
    test_add_new_employee    #добавляет нового сотрудника
    assert test_search_employee_data == 'Андрей Тарасов'