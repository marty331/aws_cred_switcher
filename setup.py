from setuptools import setup

setup(
    name='cred_switch',
    version='0.1',
    description='AWS Cred Switcher',
    author='Marty Ballard',
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        cred_switch=cred.cred_switch:change_type
    ''',
    )
