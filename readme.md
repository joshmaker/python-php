# Python PHP
Have you ever wished that the Python standard library had the power and flexibilty of PHP? Now it is as simple as `import php`

## Installation
Python PHP can be installed using pip
```
$ pip install -e git+git@github.com:theatlantic/joshmaker/python-php#egg=python-php
```

## Usage
To access PHP functions in Python, simply import the php module and get started.
```python
import php

php.str_replace('Python', 'PHP', 'Hello World of Python')
# Output: u'Hello World of Python'
```
Python PHP supports the following types: int, string, list, and dictionaries

## Testing
Of course Python-PHP has unit tests! How else would we know that it is safe to use? Run tests with `$ python tests.py`

## Compatibility
Python-PHP is currently only compatible with Python 2.7

## Is this really a good idea
What could possibly go wrong?