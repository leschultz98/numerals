from time import sleep

from pygame import init
from pygame.mixer import Sound


# Waypoint 5, 6: Generate English Numerals & Say English Numerals
def convert_number_3_digits(n):
    """Generate English Numerals with number has 3 digits."""
    digit = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
             7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
            7: 'seventy', 8: 'eighty', 9: 'ninety'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen'}

    # Translate hundred
    if n // 100 > 0:
        hundred = digit[n // 100] + ' hundred'
    else:
        hundred = ''

    # Translate ten and one
    if n % 100 // 10 > 1:
        one = ''
        if n % 10 > 0:
            ten = tens[n % 100 // 10] + '-' + digit[n % 10]
        else:
            ten = tens[n % 100 // 10]
    elif n % 100 // 10 == 1:
        one = ''
        ten = teens[n % 100]
    else:
        ten = ''
        if n % 10 > 0:
            one = digit[n % 10]
        else:
            one = ''

    # Join hundred, ten and one
    number = [digit for digit in [hundred, ten, one] if digit]
    if len(number) > 1:
        number.insert(-1, 'and')
    return ' '.join(number)


def integer_to_english_numeral(n, activate_tts=False):
    """Generate and Say English Numerals."""
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n == 0:
        return 'zero'
    if n < 0:
        raise ValueError('Not a positive integer')
    if n > 999999999999:
        raise OverflowError('Integer greater than 999,999,999,999')
    if not isinstance(activate_tts, bool):
        if activate_tts is None:
            activate_tts = False
        else:
            raise TypeError

    # Translate billion, million thousand and one
    billion = convert_number_3_digits(n // 1000000000)
    million = convert_number_3_digits(n % 1000000000 // 1000000)
    thousand = convert_number_3_digits(n % 1000000 // 1000)
    ones = convert_number_3_digits(n % 1000)

    # Join billion, million thousand and one
    prefixs = [(billion, ' billion'), (million, ' million'),
               (thousand, ' thousand'), (ones, '')]
    number = [digit + prefix for digit, prefix in prefixs if digit]
    for x in range(len(number)):
        if x < len(number) - 1:
            number[x] += ' and'
    number = ' '.join(number)

    # Say numeral
    if activate_tts:
        init()
        for word in number.replace('-', ' ').split():
            path = './sounds/en/{}.ogg'.format(word)
            Sound(path).play()
            sleep(len(word) / 7)
    return number
