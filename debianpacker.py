#!/usr/bin/env python

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


# Mapped File Record class
class Mapped:
    def __init__(self, map_record):
        self.name = map_record[KEY_NAME]
        self.path = map_record[KEY_PATH]

    def get_name(self):
        return self.name

    def get_deb_path(self):
        return self.path

    def print_details(self):
        print("Name: " + self.name)
        print("Path: " + self.path + "\n")


# Prints all the stored Mapped Record details
def print_all_details():
    for i in mapped_files:
        i.print_details()


# Main Function to run on Start
@click.command()
@click.option('-f', '--file_map', type=click.Path('r'), default=DEFAULT_FILE_MAP)
def main(file_map):
    click.echo("Welcome to " + APP_NAME + "by " + APP_AUTHOR)

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
