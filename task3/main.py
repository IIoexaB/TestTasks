import json
import sys

def generate_report(values_file, tests_file, report_file):

    try:
        with open(values_file, 'r') as f:
            values = json.load(f)
    except FileNotFoundError:
        print(f"Файл '{values_file}' не найден!")
        return


    try:
        with open(tests_file, 'r') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print(f"Файл '{tests_file}' не найден!")
        return


    report = fill_report(tests, values)

    try:
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=4)
    except FileNotFoundError:
        print(f"Не удалось записать данные в файл '{report_file}'!")


def fill_report(tests, values):

    for key, value in tests.items():
        if isinstance(value, dict):
            tests[key] = fill_report(value, values)
        elif isinstance(value, list):
            tests[key] = [fill_report(item, values) if isinstance(item, dict) else item for item in value]
        else:
            if key in values:
                tests[key] = values[key]
    return tests


if __name__ == "__main__":


    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    generate_report(values_file, tests_file, report_file)