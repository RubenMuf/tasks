# Задача №3 выполнено
import json
# values = 'values.json'
# tests = 'tests.json'
# report = 'report.json'

values = input()
tests = input()
report = input()

try:
    with open(values, encoding='utf-8') as file, open(tests, encoding='utf-8') as file1, open(report, 'w') as file2:

        values_file = eval(file.read())
        tests_json = eval(file1.read())

        '''Понятно, что тут нужна рекурсия, но вложенность настолько беспорядочная,
        что решил закостылить. Памяти конечно жуть сколько. '''
        js = json.dumps(tests_json)
        while '\"values\":' in js:
            js = js.replace('\"values\":', '')
        while '[' in js:
            js = js.replace('[', '')
        while ']' in js:
            js = js.replace(']', '')
        while '  ' in js:
            js = js.replace( '  ', ' ')
        while '\", {\"' in js:
            js = js.replace('\", {\"', '\"}, {\"')
        while '}}' in js:
            js = js.replace('}}', '}')
        js = js.replace('{\"tests\": ', '')
        js = '[' + js + ']'
        # print(js)

        res = eval(js)

        for i in res:
            i['value'] = i.get('value', '')
        # print(res)

        for i in values_file['values']:
            for j in res:
                if i['id'] == j['id']:
                    j['value'] = i['value']

        res = {"tests": res}
        json.dump(res, file2, indent=2)

except FileNotFoundError:
     print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)