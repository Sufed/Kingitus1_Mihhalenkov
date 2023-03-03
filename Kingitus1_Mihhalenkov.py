import random
import os
from module1 import *

est_words = loe_failist('est.txt')
rus_words = loe_failist('rus.txt')

while True:
    print("")
    print('Меню:')
    print('1. Перевод с эстонского на русский')
    print('2. Перевод с русского на эстонский')
    print('3. Добавление нового слова в словарь')
    print('4. Исправление ошибки в словаре')
    print('5. Выход')
    choice = input('Выберите действие: ')

    if choice == '1':
        est_word = input('Введите слово на эстонском: ')
        rus_word = est_to_rus(est_word, est_words, rus_words)
        if rus_word:
            print('Перевод:', rus_word)
        else:
            print('Слово не найдено в словаре.')
            add = input('Добавить его в словарь? (y/n): ')
            if add == 'y':
                add_word(est_word, est_words, rus_words)

    elif choice == '2':
        rus_word = input('Введите слово на русском: ')
        est_word = rus_to_est(rus_word, est_words, rus_words)
        if est_word:
            print('Перевод:', est_word)
        else:
            print('Слово не найдено в словаре.')
            add = input('Добавить его в словарь? (y/n): ')
            if add == 'y':
                add_word(rus_word, rus_words, est_words)

    elif choice == '3':
        word = input('Введите новое слово на эстонском: ')
        add_word(word, est_words, rus_words)

    elif choice == '4':
        word = input('Введите слово для исправления: ')
        fix_word(word, est_words, rus_words)

    elif choice == '5':
        break

    else:
        print('Неверный выбор. Попробуйте еще раз.')

