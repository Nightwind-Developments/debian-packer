from setuptools import setup

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
