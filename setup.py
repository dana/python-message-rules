#! /usr/bin/env python

import setuptools

from message_rules import __version__ as version
from os import path

here = path.abspath(path.dirname(__file__))


with open('HISTORY.rst') as f:
    history = f.read()

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

description = 'Fast, simple message rules'

setuptools.setup(
    name='message-rules',
    version=version,
    description='{0}\n\n{1}'.format(description, history),
    long_description=long_description,
    author='Dana M. Diederich',
    author_email='dana@realms.org',
    url='https://github.com/dana/python-message-rules',
    packages=['message_rules'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['sys', 'pytest']
    },
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ]
)
