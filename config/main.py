#!/usr/bin/env python3
__author__ = ("Naushad Shukoor",)
__credits__ = ["Naushad Shukoor"]
__version__ = "1.0.0"
__maintainer__ = "Naushad Shukoor"
__email__ = "naushadshukoor@gmail.com"
__status__ = "Development"

# Sytem Libraries
from pathlib import Path

# CONFIG
data_dir = "data"
bins_dir = f"{data_dir}/bins"
json_dir = f"{data_dir}/json"

Path(bins_dir).mkdir(parents=True, exist_ok=True)
Path(json_dir).mkdir(parents=True, exist_ok=True)

person_bin_file_path = f"{bins_dir}/person_bin"
person_json_file_path = f"{json_dir}/person.json"

persons_bin_file_path = f"{bins_dir}/persons_bin"
persons_json_file_path = f"{json_dir}/persons.json"
