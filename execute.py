from numerals import *


def check_input(name, option):
    """Check input"""
    while True:
        print('\nPlease choose {}:'.format(name))
        print('(Enter q anytime to exit)')
        print('\t1. {}'.format(option[0]))
        print('\t2. {}'.format(option[1]))
        info = input('\tEnter a number (1/2): ')
        if info == 'q':
            print('\nGoodbye!')
            return False
        if info not in ['1', '2']:
            print('\nPlease choose again!')
            continue
        return info


while True:
    n = int(input('\nPlease enter a number: '))
    print('\nWelcome to Artificial Speak!')
    step_1 = check_input('a language numerals',
                         ['Vietnamese Numerals', 'English Numerals'])
    if step_1 == '1':
        step_2 = check_input('a region', ['North', 'South'])
        if step_2 == '1':
            step_3 = check_input('an action', ['Generate', 'Generate & Say'])
            if step_3 == '1':
                print('\n', integer_to_vietnamese_numeral(n))
            elif step_3 == '2':
                print('\n',
                      integer_to_vietnamese_numeral(n, activate_tts=True))
        if step_2 == '2':
            step_3 = check_input('an action', ['Generate', 'Generate & Say'])
            if step_3 == '1':
                print('\n', integer_to_vietnamese_numeral(n, 'south'))
            elif step_3 == '2':
                print('\n', integer_to_vietnamese_numeral(n, 'south',
                                                          activate_tts=True))
    if step_1 == '2':
        step_2 = check_input('an action', ['Generate', 'Generate & Say'])
        if step_2 == '1':
            print('\n', integer_to_english_numeral(n))
        elif step_2 == '2':
            print('\n', integer_to_english_numeral(n, activate_tts=True))
    if input('One more time... (y/any key): ') == 'y':
        continue
    else:
        print('\nGoodbye!')
    break
