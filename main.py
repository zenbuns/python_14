import csv
import math
import random
import re


max = int(input("Enter max people per group: "))

class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name  = last_name
        self.age        = age

    def first_name(self):
        return self.__first_name

persons = []

path = 'school.csv'

def validate_data(path):

    file = open(path, "r", encoding="utf-8")
    regex = r"^[a-zA-Z ÕõÄäÖöÜü-]*$"
    for line in file.readlines():
        data = line.split(",")
        print(data)
        if len(data) == 3:
            if re.match(regex, data[0]) and re.match(regex, data[1]):
                if "\n" in data[2] and 0 <= int(data[2].strip()) <= 100:
                    continue
                else:
                    return False
            else:
                return False
        else:
            return False
    return True



with open(path, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if len(row) == 0:
            break
        persons.append(Person(row[0], row[1], row[2]))

n = 0
n = n + 1

#random.shuffle(persons)

group_nr = math.ceil(len(persons) / max)

def make_groups(group_nr):
    groups = []
    for i in range (0, group_nr):
        groups.append([])
    return groups

groups = make_groups(group_nr)

def divide_groups(persons, max, groups):
    for num in range(max):
        for i in range(len(groups)):
            if len(persons) == 0:
                break
            person = random.choice(persons)
            groups[i].append(person)
            persons.remove(person)
    return groups

groups = divide_groups(persons, max, groups)

def write_csv(groups):
    for i in range(len(groups)):
        _out = open(f"Grupp_{i+1}.csv", "w", newline="")
        with _out as f:
            for isik in groups[i]:
                f.write(f"{isik._Person__first_name},{isik.last_name},{isik.age}"'\n')

write_csv(groups)

# testid
def test_divide_groups():
    max = 5
    persons = [i for i in range(20)]
    groups = make_groups(4)
    if len(divide_groups(persons, max, groups)) == 4:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    i = 1
    for item in divide_groups(persons, max, groups):
        if len(item) in range(4, 6):
            print(f"Group {i}: Test 2 passed")
        else:
            print(f"Group {i}: Test 2 failed")
        i += 1

def test_validate_name():
    test_case = ["M4rtin,App0,20", "Martin,Appo,120", "Appo,Martin,30"]
    regex = r"^[a-zA-z ÕõÄäÖöÜü]*$"
    for item in test_case:
        data = item.split(",")
        if len(data) == 3:
            if re.match(regex, data[0]) and re.match(regex, data[1]):
                if 0 <= int(data[2].strip()) <= 100:
                    print("Test 3 passed")
                else:
                    print("Test 3 failed")
            else:
                print("Test 3 failed")
        else:
            print("Test 3 failed")

def test_input_format():
    test_case = ["30,Martin,Appo\n", "Martin\n", "Martin,Appo,30\n"]
    regex = r"^[a-zA-z ÕõÄäÖöÜü]*$"
    for item in test_case:
        data = item.split(",")
        if len(data) == 3:
            if re.match(regex, data[0]) and re.match(regex, data[1]):
                if "\n" in data[2] and 0 <= int(data[2].strip()) <= 100:
                    print("Test 4 passed")
                else:
                    print("Test 4 failed")
            else:
                print("Test 4 failed")
        else:
            print("Test 4 failed")

test_divide_groups()
test_validate_name()
test_input_format()