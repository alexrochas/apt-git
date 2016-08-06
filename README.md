# apt-git
>Apt-get like tool for github repositories

[![Build Status](https://travis-ci.org/alexrochas/apt-git.svg?branch=master)](https://travis-ci.org/alexrochas/apt-git)

Apt-git exists to give final user a tool similar to apt-get. With apt-git you will be able to search and clone github projects from your terminal. 

## Installation

Linux:

```sh
pip3 install apt-git
```

## Usage example

Once installed apt-git you could search github repos
```sh
apt-git search :repo
```

The output if you search for example 'python' will be similar to
```sh
~$ apt-git search python
awesome-python - A curated list of awesome Python frameworks, libraries, software and resources
python-guide - Python best practices guidebook, written for Humans. 
python-patterns - A collection of design patterns/idioms in Python
python-machine-learning-book - The "Python Machine Learning" book code repository and info resource
python-mode - Vim python-mode. PyLint, Rope, Pydoc, breakpoints from box.
python-prompt-toolkit - Library for building powerful interactive command lines in Python
python_koans - Python Koans - Learn Python through TDD
pythonpy - the swiss army knife of the command line
python-oauth2 - A fully tested, abstract interface to creating OAuth clients and servers.
python-social-auth - Social auth made simple
```

And once you encounter the repo you want, just "install it"
```sh
apt-git install :owner/:repo
```

A directory will be created with the project clone.

## Release History

* 0.0.1
    * Work in progress
    * Clone function
    * Search function

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
