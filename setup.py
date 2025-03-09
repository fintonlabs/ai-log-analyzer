from setuptools import setup, find_packages

setup(
    name='log-analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.2',
        'pandas==1.3.3',
        'scikit-learn==0.24.2',
    ],
    entry_points={
        'console_scripts': [
            'log-analyzer = log_analyzer.main:run',
        ],
    },
)