#!/usr/bin/env python

import os
import shutil
import json
import click
import deb_pkg_tools.package

# App Details
APP_NAME = "Debian Packer"
APP_AUTHOR = "Nightwind Developments"

# Generic Package Name
GENERIC_PKG_NAME = "package"

# Default Location of File Map file
DEFAULT_FILE_MAP = "example-map.json"
HELP_FILE_MAP = "Path to the compatible JSON file with all the file mappings."

# Temporary Package Tree
PACKAGE_TREE_LOC = "./temporary"

# Default Location of Sources to Include in Package
input_src = str()
DEFAULT_INPUT_PATH = "./input"
HELP_IP = "Path to directory with files to include in generated package."

# Default Output Location for Package
output_src = str()
DEFAULT_OUTPUT_PATH = "./output"
HELP_OP = "Path to directory where the package will be written to."

# JSON Map File Keys
KEY_NAME = "name"
KEY_PATH = "path"

# Debian Package File Extension
FILE_EXT = ".deb"

# File Name Separator
FN_SEP = "_"

# Path Separator
PATH_SEP = "/"

# List of Mapped File Records
mapped_files = list()

# Package Application Name
basic_name = str()
HELP_PKG_NAME = "Base File Name for Package."

# Version
version = str()
HELP_PKG_VER = "Package version number/code."

# Target Architecture
arch = str()
HELP_PKG_ARCH = "Label of target architecture."

# Full File Name of the Generated Package
pkg_full_name = str()


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


# Makes a new directory if it does not exist
def mkdir_if_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


# Prints all the stored Mapped Record details
def print_all_details():
    print("Stored Mapped File Records:")
    for i in range(len(mapped_files)):
        mapped_files[i].print_details(str(i) + ".\t", "\t")


# Generates File Name of the Package
def get_package_name():
    global basic_name
    global version
    global arch
    pkg_name = basic_name

    if version is not None:
        pkg_name += FN_SEP + version

    if arch is not None:
        pkg_name += FN_SEP + arch

    pkg_name += FILE_EXT

    return pkg_name


# Build Package Tree
def build_package_tree():
    for i in range(len(mapped_files)):
        r = mapped_files[i]
        file_in = input_src + PATH_SEP + r.get_name()
        file_out = PACKAGE_TREE_LOC + r.get_deb_path() + PATH_SEP + r.get_name()
        print("Input: " + file_in)
        print("Output: " + file_out)
        try:
            shutil.copy(file_in, file_out)
        except IOError as io_err:
            os.makedirs(os.path.dirname(file_out))
            shutil.copy(file_in, file_out)


# Generate Package
def run_package_generation():
    deb_pkg_tools.package.build_package(PACKAGE_TREE_LOC, output_src)


# Main Function to run on Start
@click.command()
@click.option('-n', '--pkg_name', type=click.STRING, default=GENERIC_PKG_NAME, help=HELP_PKG_NAME)
@click.option('-v', '--pkg_version', type=click.STRING, help=HELP_PKG_VER)
@click.option('-a', '--pkg_arch', type=click.STRING, help=HELP_PKG_ARCH)
@click.option('-m', '--pkg_file_map', type=click.File('r'), default=DEFAULT_FILE_MAP, help=HELP_FILE_MAP)
@click.option('-i', '--input', type=click.Path(exists=True, readable=True), default=DEFAULT_INPUT_PATH, help=HELP_IP)
@click.option('-o', '--output', type=click.Path(exists=False, writable=True), default=DEFAULT_OUTPUT_PATH, help=HELP_OP)
def main(pkg_name, pkg_version, pkg_arch, pkg_file_map, input, output):
    click.echo("Welcome to " + APP_NAME + " by " + APP_AUTHOR + "\n")

    # Saves the Package Variables
    global basic_name
    basic_name = pkg_name
    global version
    version = pkg_version
    global arch
    arch = pkg_arch

    global input_src
    input_src = input
    print("Input Prefix: " + input_src)
    global output_src
    output_src = output
    print("Output Prefix: " + output_src + "\n")

    # Loads JSON File as a local variable
    the_map = json.load(pkg_file_map)

    # Makes the folder where the Package Tree will be constructed
    mkdir_if_not_exist(PACKAGE_TREE_LOC)

    shutil.rmtree(PACKAGE_TREE_LOC)

    # Iterates through the JSON Array from File,
    # Converts JSON objects as 'Mapped' objects,
    # Saves to Local List, 'mapped_files'
    for i in the_map:
        mapped_files.append(Mapped(i))

    #print_all_details()

    build_package_tree()

    print("Output File Name: " + get_package_name())

    run_package_generation()


# Ensures Main Function is to be run first
if __name__ == "__main__":
    main()
