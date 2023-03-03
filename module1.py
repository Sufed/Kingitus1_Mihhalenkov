import random
import os

# функция для чтения слов из файла
def loe_failist(filename):
    fail=open(filename,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

est_words = loe_failist('est.txt')
rus_words = loe_failist('rus.txt')

# функция для записи слов в файл
def write_file(words, filename):
    f=open(filename,'w',encoding="utf-8-sig")
    for line in words:
        f.write(line+'\n')
    f.close()


# функция для перевода слов с эстонского на русский
def est_to_rus(word, est_words, rus_words):
    if word in est_words:
        index = est_words.index(word)
        return rus_words[index]
    else:
        return None

# функция для перевода слов с русского на эстонский
def rus_to_est(word, est_words, rus_words):
    if word in rus_words:
        index = rus_words.index(word)
        return est_words[index]
    else:
        return None

# функция для добавления нового слова в словарь
def add_word(word, est_words, rus_words):
    if word not in est_words:
        est_words.append(word)
        rus_word = input('Введите перевод слова на русский: ')
        rus_words.append(rus_word)
        write_file(est_words, 'est.txt')
        write_file(rus_words, 'rus.txt')

# функция для исправления ошибки в словаре
def fix_word(word, est_words, rus_words):
    if word in est_words:
        index = est_words.index(word)
        new_rus_word = input('Введите новый перевод слова на русский: ')
        rus_words[index] = new_rus_word
        write_file(rus_words, 'rus.txt')
    elif word in rus_words:
        index = rus_words.index(word)
        new_est_word = input('Введите новый перевод слова на эстонский: ')
        est_words[index] = new_est_word
        write_file(est_words, 'est.txt')
