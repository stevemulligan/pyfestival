#!/usr/bin/env python
from distutils.core import setup, Extension
import os

festival_include = os.environ.get("FESTIVAL_INCLUDE", '/usr/include/festival')
speech_tools_include = os.environ.get("SPEECH_INCLUDE", '/usr/include/speech_tools')
festival_lib = os.environ.get("FESTIVAL_LIB", '/usr/lib')
speech_lib = os.environ.get("SPEECH_LIB", '/usr/lib')

festival_classifiers = [
"Programming Language :: Python :: 2",
"Programming Language :: Python :: 3",
"Intended Audience :: Developers",
"License :: OSI Approved :: BSD License",
"Topic :: Software Development :: Libraries",
"Topic :: Utilities",
"Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
"Topic :: Multimedia :: Sound/Audio :: Speech"
]

long_description = """A Python wrapper around the Festival Speech Synthesis System:
http://www.cstr.ed.ac.uk/projects/festival/

pyfestival creates a C module built on top of the festival source code, making it a self-contained Python library
(there is no need to run festival-server alongside).

pyfestival supports (and is tested on) Python 2.7+ including Python 3
"""

setup(
    name='pyfestival',
    description='Python Festival module',
    long_description=long_description,
    url="https://github.com/techiaith/pyfestival",
    author="Patrick Robertson",
    author_email="techiaith@bangor.ac.uk",
    license="BSD",
    py_modules=['festival'],
    ext_modules=[
        Extension(
            '_festival',
            ['_festival.cpp'],
            include_dirs=[festival_include, speech_tools_include],
            library_dirs=[festival_lib, speech_lib],
            libraries=['Festival', 'estools', 'estbase', 'eststring'],
        ),
    ],
    platforms=["*nix"],
    bugtrack_url="https://github.com/techiaith/pyfestival/issues",
    version="0.5",
)
