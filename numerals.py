from time import sleep

from pygame import init
from pygame.mixer import Sound


# Waypoint 1, 2, 3, 4: Generate & Say Vietnamese Numerals.
def convert_number_3_digits_vi(n):
    """Generate Vietnamese Numerals with number has 3 digits."""
    digit = {0: '', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm', 6: 'sáu',
             7: 'bảy', 8: 'tám', 9: 'chín'}

    # Translate hundred.
    if n:
        if n // 100 > 0:
            hundred = digit[n // 100] + ' trăm'
        else:
            hundred = 'không trăm'
    else:
        hundred = ''

    # Translate ten and one.
    if n % 100 // 10 > 1:
        ten = digit[n % 100 // 10] + ' mươi'
        if n % 10 != 1:
            one = digit[n % 10]
        else:
            one = 'mốt'
    elif n % 100 // 10 == 1:
        ten = 'mười'
        if n % 10 == 5:
            one = 'lăm'
        else:
            one = digit[n % 10]
    else:
        if n % 10 > 0:
            ten = 'linh'
        else:
            ten = ''
        one = digit[n % 10]

    # Join hundred, ten and one.
    number = [digit for digit in [hundred, ten, one] if digit]
    return ' '.join(number)


def integer_to_vietnamese_numeral(n, region='north', activate_tts=False):
    """Generate and Say English Numerals."""
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n == 0:
        return 'không'
    if n < 0:
        raise ValueError('Not a positive integer')
    if n > 999999999999:
        raise OverflowError('Integer greater than 999,999,999,999')
    if region is None:
        region = 'north'
    elif not isinstance(region, str):
        raise TypeError('Argument "region" is not a string')
    elif region != 'north' and region != 'south':
        raise ValueError('Argument "region" has not a correct value')
    if activate_tts is None:
        pass
    elif not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')

    # Translate billion, million thousand and one.
    ones = convert_number_3_digits_vi(n % 1000)
    thousand = convert_number_3_digits_vi(n % 1000000 // 1000)
    million = convert_number_3_digits_vi(n % 1000000000 // 1000000)
    billion = convert_number_3_digits_vi(n // 1000000000)

    # Join billion, million thousand and one.
    prefixs = [(billion, ' tỷ'), (million, ' triệu'),
               (thousand, ' nghìn'), (ones, '')]
    number = [digit + prefix for digit, prefix in prefixs if digit]
    if number[0][:11] == 'không trăm ':
        number[0] = number[0].replace('không trăm ', '')
    if number[0][:5] == 'linh ':
        number[0] = number[0].replace('linh ', '')
    number = ' '.join(number)

    # Change region.
    if region == 'south':
        number = number.replace('linh', 'lẻ').replace('nghìn', 'ngàn')

    # Say numeral.
    speech_dict = {"không": 'khong', "linh": 'linh', "lẻ": "le", "một": 'mot1',
                   "mốt": 'mot2', "hai": 'hai', "ba": 'ba', "bốn": 'bon',
                   "năm": 'nam', "lăm": 'lam', "sáu": 'sau', "bảy": 'bay',
                   "tám": 'tam', "chín": 'chin', "mười": 'muoi1',
                   "mươi": "muoi2", "trăm": "tram", 'nghìn': 'nghin',
                   "ngàn": "ngan", 'triệu': 'trieu', 'tỷ': 'ty'}
    if activate_tts:
        init()
        for word in number.split():
            path = './sounds/vi/{}/{}.ogg'.format(region, speech_dict[word])
            Sound(path).play()
            sleep(len(word) / 7)
    return number


# Waypoint 5, 6: Generate & Say English Numerals.
def convert_number_3_digits(n):
    """Generate English Numerals with number has 3 digits."""
    digit = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
             7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
            7: 'seventy', 8: 'eighty', 9: 'ninety'}
    teen = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'}

    # Translate hundred.
    if n // 100 > 0:
        hundred = digit[n // 100] + ' hundred'
    else:
        hundred = ''

    # Translate ten and one.
    if n % 100 // 10 > 1:
        one = ''
        if n % 10 > 0:
            ten = tens[n % 100 // 10] + '-' + digit[n % 10]
        else:
            ten = tens[n % 100 // 10]
    elif n % 100 // 10 == 1:
        one = ''
        ten = teen[n % 100]
    else:
        ten = ''
        if n % 10 > 0:
            one = digit[n % 10]
        else:
            one = ''

    # Join hundred, ten and one.
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
    if activate_tts is None:
        pass
    elif not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')

    # Translate billion, million thousand and one.
    ones = convert_number_3_digits(n % 1000)
    thousand = convert_number_3_digits(n % 1000000 // 1000)
    million = convert_number_3_digits(n % 1000000000 // 1000000)
    billion = convert_number_3_digits(n // 1000000000)

    # Join billion, million thousand and one.
    prefixs = [(billion, ' billion'), (million, ' million'),
               (thousand, ' thousand'), (ones, '')]
    number = [digit + prefix for digit, prefix in prefixs if digit]
    for x in range(len(number)):
        if x < len(number) - 1:
            number[x] += ' and'
    number = ' '.join(number)

    # Say numeral.
    if activate_tts:
        init()
        for word in number.replace('-', ' ').split():
            path = './sounds/en/{}.ogg'.format(word)
            Sound(path).play()
            sleep(len(word) / 7)
    return number
