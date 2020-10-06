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

# Third Party Libraries
# https://googleapis.dev/python/protobuf/latest/google/protobuf/json_format.html
from google.protobuf.json_format import MessageToDict,MessageToJson

# Project File Imports
from config.main import person_bin_file_path,person_json_file_path, persons_bin_file_path, persons_json_file_path
from util.printer import printStylizedHeader, printRepresentations, printObjectAndType
from protos.generated import person_pb2

printStylizedHeader("Decoding -> person")

# Initialize person proto object(message)
person = person_pb2.Person()

# Read the binary file
with open(person_bin_file_path,"rb") as f:
    person.ParseFromString(f.read())

printObjectAndType("person(in binary) deserialized", person)
printObjectAndType("convert person to Dict using MessageToDict(from google.protobuf.json_format)", MessageToDict(person))
printObjectAndType("convert person to JSON using MessageToJson(from google.protobuf.json_format)", MessageToJson(person))

# Read the JSON file
with open(person_json_file_path,"r") as f:
    printObjectAndType("person(in JSON file) read back",json.loads(f.read()))

printStylizedHeader("Decoding -> persons (person array)")

# Initialize persons proto object(message)
persons = person_pb2.Persons()

# Read the binary file
with open(persons_bin_file_path,"rb") as f:
    persons.ParseFromString(f.read())

printObjectAndType("persons(in binary) deserialized", persons)
printObjectAndType("convert person to Dict using MessageToDict(from google.protobuf.json_format)", MessageToDict(persons))
printObjectAndType("convert person to JSON using MessageToJson(from google.protobuf.json_format)", MessageToJson(persons))

persons_dict = MessageToDict(persons)
printObjectAndType("Printing value of 'persons' key from the Dict",persons_dict["persons"])

# Read the JSON file
with open(persons_json_file_path,"r") as f:
    printObjectAndType("persons(in JSON file) read back",json.loads(f.read()))
