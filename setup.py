from setuptools import setup

setup(
    name="cli2",
    version='0.1',
    py_modules=['cli2'],
    install_requires=[
        'Click==6.7',
    ],
    entry_points='''
        [console_scripts]
        cli2=cli2:cli
    ''',
)
