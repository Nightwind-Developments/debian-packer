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

from setuptools import setup
from debianpacker import mkdir_if_not_exist, DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH
import os

setup(
    name='debianpacker',
    version='0.0',
    py_modules=['debianpacker'],
    install_requires=[
        'Click',
        'deb-pkg-tools'
    ],
    entry_points='''
        [console_scripts]
        debianpacker=debianpacker:main
    ''',
)

# Creates Default Input & Output Directories
mkdir_if_not_exist(DEFAULT_INPUT_PATH)
mkdir_if_not_exist(DEFAULT_OUTPUT_PATH)
