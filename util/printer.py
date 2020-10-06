#!/usr/bin/env python3
__author__ = "Naushad Shukoor",
__credits__ = ["Naushad Shukoor",]
__version__ = "1.0.0"
__maintainer__ = "Naushad Shukoor"
__email__ = "naushadshukoor@gmail.com"
__status__ = "Development"

def printStylizedHeader(string):
    print(f"""
{'#'*120}
{string}
{'#'*120}
    """)

def printRepresentations(name1,value1,name2,value2):
    print(f"""
'{name1}' representation:
{'-'*120}
{value1}
{'-'*120}


'{name2}' representation:
{'-'*120}
{value2}
{'-'*120}

    """)

def printSummary(person_json_file_size,person_bin_file_size,persons_json_file_size,persons_bin_file_size):
    print(f"""
{'#'*120}
Summary
{'#'*120}

person(json):{person_json_file_size} bytes, person(binary):{person_bin_file_size} bytes ------> ({round(person_bin_file_size/person_json_file_size,2)}% reduction in storage size)

persons(json):{persons_json_file_size} bytes, persons(binary):{persons_bin_file_size} bytes ------> ({round(persons_bin_file_size/persons_json_file_size,2)}% reduction in storage size)
    """)

def printObjectAndType(name,object):
    print(f"""
{name}:
{'-'*120}
{object}
{'-'*120}
type -> {type(object)}
    """)