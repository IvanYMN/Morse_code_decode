import morse
import sys
import pyperclip


def code_morse(text):
    text += ' '
    morse_code = ''
    char_text = ''
    for char in text:
        if char != ' ':
            i = 0
            char_text += char
            if char_text == 'SOS':
                morse_code += morse.MORSE_CODE_REVERSE[char_text]
                return morse_code
        else:
            i += 1
            if i == 2:
                morse_code += ' '
            else:
                try:
                    for c in char_text:
                        morse_code += morse.MORSE_CODE_REVERSE[c]
                        morse_code += ' '
                except KeyError:
                    continue
                char_text = ''
                morse_code += '   '
    return morse_code


def decode_morse(morse_code):
    morse_code += ' '
    decode_morse_code = ''
    char_text = ''
    for char in morse_code:
        if char != ' ':
            i = 0
            char_text += char
        else:
            i += 1
            if i == 2:
                decode_morse_code += ' '
            else:
                try:
                    decode_morse_code += morse.MORSE_CODE[char_text]
                except KeyError:
                    continue
                char_text = ''
    return decode_morse_code


if __name__ == '__main__':
    print("""
    █▀▄▀█ █▀█ █▀█ █▀ █▀▀   █▀▀ █▀█ █ █▀█ ▀█▀
    █░▀░█ █▄█ █▀▄ ▄█ ██▄   █▄▄ █▀▄ █ █▀▀ ░█░
    
    Coded by Ivan Yamanchev
    """)
    print("""
    Что будем делать? Кодировать или декодировать?
    1) Кодировать
    2) Декодировать
    q) Выйти
    """)
    while True:
        user_choice = input('>>> ')
        if user_choice == '1':  # Операция кодирования
            print('Введите фразу для кодирования в азбуку Морзе')
            user_input_to_code = input('> ')
            output = code_morse(user_input_to_code.upper())
            print(output)
            pyperclip.copy(output)
            print('Вывод программы скопирован в буфер обмена...')
            continue
        elif user_choice == '2':  # Операция декодирования
            print('Введите фразу на азбуке Морза для декодирования')
            user_input_to_decode = input('> ')
            output = decode_morse(user_input_to_decode)
            print(output)
            pyperclip.copy(output)
            print('Вывод программы скопирован в буфер обмена...')
            continue
        elif user_choice == 'q':
            print('Выход из программы...')
            sys.exit()
