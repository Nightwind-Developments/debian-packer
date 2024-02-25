#!/usr/bin/env python

#  Copyright (C) 2020  Nightwind Future Industries Ltd. (NZ)
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License,
#  or any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.
#  If not, see <https://www.gnu.org/licenses/>.

import os
import shutil
import json
import click
import deb_pkg_tools.package

# App Details
APP_NAME = "Debian Packer"
APP_AUTHOR = "Nightwind Future Industries Limited"
APP_TITLE = "{} - Copyright (C) 2020 {}".format(APP_NAME, APP_AUTHOR)
APP_LICENSE_1 = "This program comes with ABSOLUTELY NO WARRANTY"
APP_LICENSE_2 = "This is free software and you are welcome to redistribute it under certain conditions."
APP_LICENSE_3 = "For more information, run this program with the following arguments '-l' or '--license'"

# Generic Package Name
GENERIC_PKG_NAME = "package"

# Default Location of File Map file
DEFAULT_FILE_MAP = "examples/example-map.json"
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

# GitHub Actions Output Environment File
HELP_GHO = ("Path to environment file where GitHub Actions Outputs are appended to to set Action Environment "
            "Variables. Its alias is usually '$GITHUB_OUTPUT'.")

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

    return pkg_name


# Build Package Tree
def build_package_tree():
    for i in range(len(mapped_files)):
        r = mapped_files[i]
        file_in = input_src + PATH_SEP + r.get_name()
        #file_out_prefix = PACKAGE_TREE_LOC + PATH_SEP + get_package_name() + PATH_SEP + r.get_deb_path()
        file_out_prefix = PACKAGE_TREE_LOC + PATH_SEP + get_package_name() + r.get_deb_path()
        file_out = file_out_prefix + r.get_name()
        print("Input: " + file_in)
        print("Output: " + file_out + "\n")
        try:
            shutil.copy(file_in, file_out)
        except IOError as io_err:
            os.makedirs(os.path.dirname(file_out_prefix))
            shutil.copy(file_in, file_out)


def get_final_package_path():
    return output_src + PATH_SEP + get_package_name() + FILE_EXT


# Generate Package
def run_package_generation():
    deb_pkg_tools.package.build_package(PACKAGE_TREE_LOC + PATH_SEP + get_package_name(), output_src)


# Main Function to run on Start
@click.command()
@click.option('-n', '--pkg_name', type=click.STRING, default=GENERIC_PKG_NAME, help=HELP_PKG_NAME)
@click.option('-v', '--pkg_version', type=click.STRING, help=HELP_PKG_VER)
@click.option('-a', '--pkg_arch', type=click.STRING, help=HELP_PKG_ARCH)
@click.option('-m', '--pkg_file_map', type=click.File('r'), default=DEFAULT_FILE_MAP, help=HELP_FILE_MAP)
@click.option('-i', '--input', type=click.Path(exists=True, readable=True), default=DEFAULT_INPUT_PATH, help=HELP_IP)
@click.option('-o', '--output', type=click.Path(exists=False, writable=True), default=DEFAULT_OUTPUT_PATH, help=HELP_OP)
@click.option('-gho', '--github_output', type=click.Path(exists=True, writable=True), help=HELP_GHO)
def main(pkg_name, pkg_version, pkg_arch, pkg_file_map, input, output, github_output):
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

    # Opens the GitHub Environments File (replaces ::set-output)
    global gh_outputs_file_path
    gh_outputs_file_path = github_output
    gh_env_file = open(gh_outputs_file_path, "a")

    # Loads JSON File as a local variable
    the_map = json.load(pkg_file_map)

    # Makes the folder where the Package Tree will be constructed
    mkdir_if_not_exist(PACKAGE_TREE_LOC)

    # Ensures Package Tree is empty
    shutil.rmtree(PACKAGE_TREE_LOC)

    # Makes the folder where the Package Output will be saved
    mkdir_if_not_exist(output_src)

    # Ensures Package Output is empty first
    #shutil.rmtree(output_src)

    # Iterates through the JSON Array from File,
    # Converts JSON objects as 'Mapped' objects,
    # Saves to Local List, 'mapped_files'
    for i in the_map:
        mapped_files.append(Mapped(i))

    #print_all_details()

    build_package_tree()

    print("Output File Name: " + get_package_name())

    run_package_generation()

    print("Completed!")

    # Sets a GitHub Actions output variable
    gh_env_file.write("{generated_package_path}={" + get_final_package_path() + "}\n")
    gh_env_file.close()


# Ensures Main Function is to be run first
if __name__ == "__main__":
    main()
