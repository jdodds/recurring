from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='recurring',
    version='1.0.1',
    description='Run a function or other callable every N seconds',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jdodds/recurring',
    author='Jeremiah Dodds',
    author_email='jeremiah.dodds@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='scheduling repeating cron sched threads',
    packages=find_packages(exclude=['tests']),
    project_urls={
        'Issue Tracker': 'https://github.com/jdodds/recurring/issues',
        'Source': 'https://github.com/jdodds/recurring',
        'Docs': 'https://recurring.readthedocs.io',
    },
    python_requires='>=3.6',
    extras_require={
        'docs': ['m2r']
    },
)
