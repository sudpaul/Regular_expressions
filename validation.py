# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:44:36 2016

@author: Sudipta
"""

"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re

def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string))

def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r'^\-?\d+$', string))

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    return bool(re.search(r'-?\d+\/[1-9]+$', string))

def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    return bool(re.search(r'\d{4}\-[0-9|1-2]{2}\-[1-3]{2})', string)

def is_number(string):
    """Return True iff the string represents a decimal number."""
    return bool(re.search(r'^-?(\d+\.?\d+|\.\d+)$', string))


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
    return bool(re.search(r'[0-9A-F]',string))
