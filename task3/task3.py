# Задача №3 выполнено

import sys
import json
from pathlib import Path

if len(sys.argv) != 4:
    raise Exception('Разрешено передавать только 3 аргумента:'
        ' путь к values.json, путь к tests.json и путь к reports.json')
values_path, tests_path, reports_path = sys.argv[1:]
# print(values_path, tests_path, reports_path)

values_path = Path(values_path)
tests_path = Path(tests_path)
reports_path = Path(reports_path)

def recursive_fill(items_list, values_dict):
    for item in items_list:
        if item['id'] in values_dict and not item['value']:
            item['value'] = values_dict[item['id']]
        if 'values' in item:
            recursive_fill(item['values'], values_dict)

def fill_values(tests, values):
    values_dict = {}
    for item in values['values']:
        values_dict[item['id']] = item['value']
    recursive_fill(tests['tests'], values_dict)


with open(tests_path, 'r', encoding='utf-8') as file1:
    tests = json.load(file1)

with open(values_path, 'r', encoding='utf-8') as file2:
    values = json.load(file2)

fill_values(tests, values)

with open(reports_path, 'w', encoding='utf-8') as file3:
    json.dump(tests, file3, indent=2, ensure_ascii=False)
# print('ok можно проверить report.json')

