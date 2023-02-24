import unicodedata
import re


def remove_acentos(string):
    normalizado = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalizado if not unicodedata.combining(c)])


def remove_non_digit(str):
    return re.sub(r'\D', '', str)