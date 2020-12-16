#!/usr/bin/env python

import os
import shutil
import json
import click

# App Details
APP_NAME = "Debian Packer"
APP_AUTHOR = "Nightwind Developments"

# Default Location of File Map file
DEFAULT_FILE_MAP = "example-map.json"

# JSON Map File Keys
KEY_NAME = "name"
KEY_PATH = "path"

# List of Mapped File Records
mapped_files = list()

# Target Architecture
arch = str()

# Version
version = str()


# Mapped File Record class
class Mapped:
    def __init__(self, map_record):
        self.name = map_record[KEY_NAME]
        self.path = map_record[KEY_PATH]

    def get_name(self):
        return self.name

    def get_deb_path(self):
        return self.path

    def print_details(self, offset1="", offset2=""):
        print(offset1 + "Name: " + self.name)
        print(offset2 + "Path: " + self.path + "\n")


# Prints all the stored Mapped Record details
def print_all_details():
    print("Stored Mapped File Records:")
    for i in range(len(mapped_files)):
        mapped_files[i].print_details(str(i) + ".\t", "\t")


# Main Function to run on Start
@click.command()
@click.option('-m', '--file_map', type=click.Path('r'), default=DEFAULT_FILE_MAP)
def main(file_map):
    click.echo("Welcome to " + APP_NAME + " by " + APP_AUTHOR + "\n")

    # Loads JSON File as a local variable
    with open(file_map) as f:
        the_map = json.load(f)

    # Iterates through the JSON Array from File,
    # Converts JSON objects as 'Mapped' objects,
    # Saves to Local List, 'mapped_files'
    for i in the_map:
        mapped_files.append(Mapped(i))

    print_all_details()


if __name__ == "__main__":
    main()
