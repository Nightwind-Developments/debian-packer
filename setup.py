from setuptools import setup
from debianpacker import DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH
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


if not os.path.exists(DEFAULT_INPUT_PATH):
    os.mkdir(DEFAULT_INPUT_PATH)

if not os.path.exists(DEFAULT_OUTPUT_PATH):
    os.mkdir(DEFAULT_OUTPUT_PATH)
