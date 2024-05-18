from src.functions import reading_employee, write_employee, add_new_employee, delete_old_employee, search_employee_data
from config import ROOT_DIR
import json
import os
import pytest
from io import StringIO
import pathlib

file_path = os.path.join(ROOT_DIR, "tests", 'test_employee.json')

@pytest.fixture()
def test_reading_employee():
    return reading_employee()


@pytest.fixture()
def test_write_employee():
    return write_employee({'tdryn4ik': ['Андрей Тарасов', 123456]})

@pytest.fixture
def for_work_with_api(monkeypatch):
    file_path = StringIO(os.path.join(ROOT_DIR, "data", 'employee.json'))
    monkeypatch.setattr('sys.stdin', file_path)

def tests_write_employee(test_write_employee, test_reading_employee, for_work_with_api):
    test_write_employee
    assert test_reading_employee == {'tdryn4ik': ['Андрей Тарасов', 123456]}

@pytest.fixture()
def test_add_new_employee():
    return add_new_employee("L_Art007", 'Артем Лазарев', 654321)

