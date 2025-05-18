# Задача №3 выполнено

import sys
import json
tests_path, values_path, reports_path = sys.argv[1:]
# print(tests_path, values_path, reports_path)

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
    print(tests)

with open(values_path, 'r', encoding='utf-8') as file2:
    values = json.load(file2)
    print(values)

fill_values(tests, values)

with open(reports_path, 'w', encoding='utf-8') as file3:
    json.dump(tests, file3, indent=2, ensure_ascii=False)
# print('ok')
