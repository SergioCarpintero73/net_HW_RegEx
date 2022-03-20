import csv
import re


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def get_right_number(contacts_list):
    number_pattern_raw = r'(\+7|8)?(\s*)?(\(*)(\d{3})?(\)*)?(\s|-?)(\d{3})(\s|-?)(\d{2})(\s|-?)(\d*)(\s*)?(\(*)?((' \
                         r'доб.|доб.)*)?(\s*)(\d*)?((\))*) '
    number_pattern_new = r'+7(\4)\7-\9-\11 \15\17'
    contacts_list_update = list()
    for data in contacts_list:
        data_string = ','.join(data)
        formatted_data = re.sub(number_pattern_raw, number_pattern_new, data_string)
        data_list = formatted_data.split(',')
        contacts_list_update.append(data_list)
    return contacts_list_update


def get_right_name_format(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_update = list()
    for data in contacts_list:
        data_string = ','.join(data)
        formatted_data = re.sub(name_pattern_raw, name_pattern_new, data_string)
        data_list = formatted_data.split(',')
        contacts_list_update.append(data_list)
    return contacts_list_update


def duplicates(contacts_list):
    doubled = contacts_list.copy()
    for i in range(len(contacts_list) - 1):
        for j in range(i + 1, len(contacts_list)):
            if contacts_list[i][0] == contacts_list[j][0] or contacts_list[i][1] == contacts_list[j][1]:
                doubled.remove(contacts_list[j])


def write_correct_file(contacts_list):
    with open("phonebook.csv", "w") as user_file:
        data_writer = csv.writer(user_file, delimiter=',')
        data_writer.writerows(contacts_list)


if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = get_right_number(contacts)
    contacts = get_right_name_format(contacts)
    duplicates(contacts)
    write_correct_file(contacts)
