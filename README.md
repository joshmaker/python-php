# Python PHP
Have you ever wished that the Python standard library had the power and flexibility of PHP? Now it is as simple as `import php`

## Installation
Python PHP can be installed using pip
```
$ pip install -e git+git@github.com:joshmaker/python-php.git#egg=python-php
```

## Usage
To access PHP functions in Python, simply import the php module and get started.
```python
import php

php.str_replace('Python', 'PHP', 'Hello World of Python')
# Output: u'Hello World of PHP'
```
Python PHP supports the following types: int, string, list, and dictionaries

## Testing
Of course Python-PHP has unit tests! How else would we know that it is safe to use? 
Run tests with `$ python tests.py`
To test with python 2.6+ and 3.3+ type `$ tox`

## Compatibility
Python-PHP is compatible with all relevant Python versions: 2.6, 2.7, 3.3, 3.4 and 3.5

## Is this really a good idea?
What could possibly go wrong?  OK, probably a lot of things. First release on April Fools Day 2016, this project was designed as a tongue-in-cheek coding exercise intended more for mirth than productivity. Using this in production is probably a very bad idea.
