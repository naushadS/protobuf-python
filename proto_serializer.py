#!/usr/bin/env python3
__author__ = "Naushad Shukoor",
__credits__ = ["Naushad Shukoor",]
__version__ = "1.0.0"
__maintainer__ = "Naushad Shukoor"
__email__ = "naushadshukoor@gmail.com"
__status__ = "Development"

# Sytem Libraries
import os
import json

# Project File Imports
from protos.generated import person_pb2
from config.main import person_bin_file_path,person_json_file_path, persons_bin_file_path, persons_json_file_path
from util.printer import printStylizedHeader, printRepresentations, printSummary

printStylizedHeader("Encoding -> person")

# Create a python dictionary representing a JSON object to be converted to JSON later
person_dict = {"firstName":"Naushad","lastName":"Shukoor","age":25,"email":"naushadshukoor@gmail.com"}

printRepresentations("person in python-dictionary form", person_dict, "person in json form", json.dumps(person_dict))

# Convert Dictionary to JSON and write to the disk
with open(person_json_file_path,"w") as f:
    f.write(json.dumps(person_dict))

# Takes about 95 bytes on the disk
person_json_file_size = int(os.stat(person_json_file_path).st_size)
print(f"Took {person_json_file_size} bytes to store json data in json format\n")

# Initialize person proto object(message)
person = person_pb2.Person()

# Set person properties (as defined in proto definition)
person.firstName = "Naushad"
person.lastName = "Shukoor"
person.age = 25
person.email = "naushadshukoor@gmail.com"

printRepresentations("person in proto form",person,"person in binary form",person.SerializeToString())

# Serialize proto message to a binary and write file on the disk
with open(person_bin_file_path, "wb") as f:
    f.write(person.SerializeToString())

# Takes about 46 bytes on the disk
person_bin_file_size = int(os.stat(person_bin_file_path).st_size)
print(f"Took {person_bin_file_size} bytes to store serialized data(using protobuf) in binary format\n")

printStylizedHeader('Encoding -> persons (person array)')

# Create a python list of dictionaries representing a JSON array of objects to be converted to JSON later
persons_list = [{"firstName":"Naushad","lastName":"Shukoor","age":25,"email":"naushadshukoor@gmail.com"},{"firstName":"John","lastName":"Doe","age":26,"email":"johndoe@mail.com"},{"firstName":"Bruce","lastName":"Wayne","age":27,"email":"brucewayne@mail.com"},{"firstName":"Clark","lastName":"Kent","age":28,"email":"clarkkent@mail.com"},{"firstName":"Peter","lastName":"Parker","age":29,"email":"peterparker@mail.com"}]

printRepresentations("persons in python-list form", persons_list, "persons in JSON form", json.dumps(persons_list))

# Convert the python list to JSON and write to the disk
with open(persons_json_file_path,"w") as f:
    f.write(json.dumps(persons_list))

# Takes about 443 bytes on the disk
persons_json_file_size = int(os.stat(persons_json_file_path).st_size)
print(f"Took {persons_json_file_size} bytes to store json data in json format\n")

# Initialize persons proto object(message)
persons = person_pb2.Persons()

# Start adding multiple persons to the persons object(message)
naushad = persons.persons.add()

naushad.firstName = "Naushad"
naushad.lastName = "Shukoor"
naushad.age = 25
naushad.email = "naushadshukoor@gmail.com"

john = persons.persons.add()

john.firstName = "John"
john.lastName = "Doe"
john.age = 26
john.email = "johndoe@mail.com"

bruce = persons.persons.add()

bruce.firstName = "Bruce"
bruce.lastName = "Wayne"
bruce.age = 27
bruce.email = "brucewayne@mail.com"

clark = persons.persons.add()

clark.firstName = "Clark"
clark.lastName = "Kent"
clark.age = 28
clark.email = "clarkkent@mail.com"

peter = persons.persons.add()

peter.firstName = "Peter"
peter.lastName = "Parker"
peter.age = 29
peter.email = "peterparker@mail.com"

printRepresentations("persons in proto form", persons, "persons in binary form", persons.SerializeToString())

# Serialize proto message to a binary and write file on the disk
with open(persons_bin_file_path,"wb") as f:
    f.write(persons.SerializeToString())

# Takes about 198 bytes on disk
persons_bin_file_size = int(os.stat(persons_bin_file_path).st_size)
print(f"Took {persons_bin_file_size} bytes to store serialized data(using protobuf) in binary format\n")

printSummary(person_json_file_size,person_bin_file_size,persons_json_file_size,persons_bin_file_size)