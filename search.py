# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:44:26 2016

@author: Sudipta
"""

"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path."""
    return filename.split('.')[-1]

def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    return [dictionary if re.search(r'[aeiou]{4}', dictionary) else None]

def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    return [match.group() for match in re.finditer(r'[A-F]$', dictionary, re.IGNORECASE)]

def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    return [match.group() for match in re.finditer(r'^[aeiou]{6,}', dictionary, re.IGNORECASE)]

def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    pat = re.sub('_', '.', partial_word)
    return re.findall(pat, dictionary, re.IGNORECASE)

def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    
    return re.findall(letter{5}, dictionary)

def abbreviate(phrase):
    """Return an acronym for the given phrase."""
    abbrev = [m.group().upper() for m in re.finditer(r'\b\w|[A-Z]?',phrase)]
    return ''.join(abbrev)

def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""
    return [m.group() for m in re.finditer(r'\b(\w)(\w)\w\2\1\b', dictionary)]

def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """


def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
