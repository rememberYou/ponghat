#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name="ponghat",
    version="1.0.0",
    description="Pong game using functionalities from the Sense HAT",
    author="Terencio Agozzino",
    author_email="terencio.agozzino@gmail.com",
    license="MIT",
    keywords = "ai emulator game hat mit pong pong-game python sensehat \
    sense-hat raspberry wall",
    url="https://github.com/rememberYou/ponghat",
    packages=find_packages(),
    long_description=long_description,
    scripts=['ponghat.py'],
    project_urls={
        'Source': 'https://github.com/rememberYou/ponghat',
        'Tracker': 'https://github.com/rememberYou/ponghat/issues',
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
