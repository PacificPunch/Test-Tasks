import json

def fill_values(obj, values):
    if isinstance(obj, dict):
        if 'id' in obj:
            test_id = obj['id']
            for value in values:
                if value['id'] == test_id:
                    obj['value'] = value['value']
                    break
        for child in obj.values():
            fill_values(child, values)
    elif isinstance(obj, list):
        for item in obj:
            fill_values(item, values)

def main(tests_path, values_path, report_path):
    with open(tests_path, 'r') as f:
        tests = json.load(f)

    with open(values_path, 'r') as f:
        values = json.load(f)['values']

    fill_values(tests, values)

    with open(report_path, 'w') as f:
        json.dump(tests, f, indent=2)

if __name__ == '__main__':
    main('tests.json', 'values.json', 'report.json')

print("file report formed")