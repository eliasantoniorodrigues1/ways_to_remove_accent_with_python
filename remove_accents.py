import unicodedata
import re


def remove_accents(string):
    normalizado = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalizado if not unicodedata.combining(c)])


def remove_accents_hard_way(texto: str):
    letra_especial = [
        'à', 'á', 'â', 'ã', 'ä', 'è', 'é', 'ê', 'ë', 'ì', 'í',
        'î', 'ï', 'ò', 'ó', 'ô', 'õ', 'ö', 'ù', 'ú', 'û', 'ü',
        'À', 'Á', 'Â', 'Ã', 'Ä', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í',
        'Î', 'Ò' 'Ó', 'Ô', 'Õ', 'Ö', 'Ù', 'Ú', 'Û', 'Ü', 'ç',
                      'Ç', 'ñ', 'Ñ'
    ]
    letra_substituicao = [
        'a', 'a', 'a', 'a', 'a', 'e', 'e', 'e', 'e',
        'i', 'i', 'i', 'i', 'o', 'o', 'o', 'o', 'o', 'u',
        'u', 'u', 'u', 'A', 'A', 'A', 'A', 'A', 'E', 'E',
        'E', 'E', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'U',
        'U', 'U', 'U', 'c', 'C', 'n', 'N'
    ]

    novo_texto = ''
    for letra in texto:
        if letra in letra_especial:
            # print(letra_especial.index[letra])
            idx = letra_especial.index(letra)
            nova_letra = letra_substituicao[idx]
            novo_texto += nova_letra
        else:
            novo_texto += letra
    return novo_texto

def remove_non_digit(str):
    return re.sub(r'\D', '', str)
