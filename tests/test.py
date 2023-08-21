import pytest
from utils import get_load_data_base, get_executed, get_sorted_operations, print_operation


@pytest.fixture
def sample_data():
	return [{'id': 441945886, 'state': 'CANCELLED', 'date': '2019-08-26T10:50:58.294041',
			 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
			 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
			 'to': 'Счет 64686473678894779589'},
			{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
			 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
			 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
			 'to': 'Счет 35383033474447895560'}]


def test_load_data_from_file(sample_data):
	data = get_load_data_base('test_load_data.json')
	non_existing_file = get_load_data_base('')
	assert data == sample_data
	assert non_existing_file == 'Файл не найден'


def test_get_executed(sample_data):
	assert get_executed(sample_data) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
										  'operationAmount': {'amount': '8221.37',
															  'currency': {'name': 'USD', 'code': 'USD'}},
										  'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
										  'to': 'Счет 35383033474447895560'}]


@pytest.fixture
def data_sort():
	return [
		{'date': '2022-01-02', 'state': 'EXECUTED'},
		{'date': '2022-01-01', 'state': 'EXECUTED'}
	]


def test_get_sorted_operations(data_sort):
	expected_result = [
		{'date': '2022-01-02', 'state': 'EXECUTED'},
		{'date': '2022-01-01', 'state': 'EXECUTED'}
	]
	assert get_sorted_operations(data_sort) == expected_result


@pytest.fixture
def lst():
	return [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
			 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
			 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}
			]


def test_print_operation(lst):
	res = '08.12.2019 Открытие вклада\n\
Неизвестно -> Счет **5907\n\
41096.24 USD\n\n'
	assert print_operation(lst) == res


@pytest.fixture
def lst_is_not_None():
	return [{'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
			 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
			 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
			 'to': 'Счет 35158586384610753655'}]


def test_print_operation(lst_is_not_None):
	res = '07.12.2019 Перевод организации\n\
Visa Classic 2842 87** **** 9012 -> Счет **3655\n\
48150.39 USD\n\n'
	assert print_operation(lst_is_not_None) == res
