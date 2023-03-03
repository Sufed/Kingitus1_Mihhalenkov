import random
import os
from module1 import *

est_words = loe_failist('est.txt')
rus_words = loe_failist('rus.txt')

while True:
    print("")
    print('����:')
    print('1. ������� � ���������� �� �������')
    print('2. ������� � �������� �� ���������')
    print('3. ���������� ������ ����� � �������')
    print('4. ����������� ������ � �������')
    print('5. �����')
    choice = input('�������� ��������: ')

    if choice == '1':
        est_word = input('������� ����� �� ���������: ')
        rus_word = est_to_rus(est_word, est_words, rus_words)
        if rus_word:
            print('�������:', rus_word)
        else:
            print('����� �� ������� � �������.')
            add = input('�������� ��� � �������? (y/n): ')
            if add == 'y':
                add_word(est_word, est_words, rus_words)

    elif choice == '2':
        rus_word = input('������� ����� �� �������: ')
        est_word = rus_to_est(rus_word, est_words, rus_words)
        if est_word:
            print('�������:', est_word)
        else:
            print('����� �� ������� � �������.')
            add = input('�������� ��� � �������? (y/n): ')
            if add == 'y':
                add_word(rus_word, rus_words, est_words)

    elif choice == '3':
        word = input('������� ����� ����� �� ���������: ')
        add_word(word, est_words, rus_words)

    elif choice == '4':
        word = input('������� ����� ��� �����������: ')
        fix_word(word, est_words, rus_words)

    elif choice == '5':
        break

    else:
        print('�������� �����. ���������� ��� ���.')

