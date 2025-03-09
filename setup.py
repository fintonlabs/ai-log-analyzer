from setuptools import setup, find_packages

setup(
    name='log_monitor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'os',
        'time',
        'threading',
        'typing',
        'collections',
        'sklearn',
    ],
)