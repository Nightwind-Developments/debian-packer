from setuptools import setup
from debianpacker import mkdir_if_not_exist, DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH
import os

setup(
    name='debianpacker',
    version='0.0',
    py_modules=['debianpacker'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        debianpacker=debianpacker:main
    ''',
)

# Creates Default Input & Output Directories
mkdir_if_not_exist(DEFAULT_INPUT_PATH)
mkdir_if_not_exist(DEFAULT_OUTPUT_PATH)
