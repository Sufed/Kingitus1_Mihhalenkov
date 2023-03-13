    x = "ru"   # задаем язык по умолчанию
    for f in nimi:  # проходим по каждой букве в строке nimi
        if f.isalpha():  # проверяем, является ли символ буквой
            if f.lower() in tähestik:  # если буква есть в словаре tähestik как русская буква
                x = "ru"  # то язык остается русским
            elif f.lower() in tähestik.values():  # если буква есть в значении словаря tähestik как английская буква
                x = "eng"  # то язык становится английским
            break  # прерываем цикл, так как язык уже определен
    
    numder_nimi = 0  # инициализируем переменную для хранения результата суммирования числового значения каждой буквы в имени
    for f in nimi:  # проходим по каждой букве в строке nimi
        if f.isalpha():  # проверяем, является ли символ буквой
            numder_nimi += tähestik[f.lower()]  # добавляем числовое значение буквы в переменную numder_nimi
         
    if  numder_nimi > 9:  # если сумма числовых значений букв имени больше 9
        numbrid = [int(numbri) for numbri in str(numder_nimi)]  # то преобразуем это число в список цифр
        numder_nimi = sum(numbrid)  # и складываем все цифры в этом списке
    
    return numder_nimi  # возвращаем результат суммирования числовых значений букв в имени, возможно преобразованный в одну цифру при необходимости

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
        
# Функция для проверки знания слов
def test_words():
    total_words = len(rus_words)
    correct_answers = 0
    for i in range(total_words):
        random_index = random.randint(0, total_words-1)
        word = rus_words[random_index]
        print("Введите перевод слова", word, ":")
        user_translation = input()
        if user_translation == est_words[random_index]:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неправильно. Правильный ответ:", est_words[random_index])
    print("Тестирование завершено. Вы ответили правильно на", correct_answers, "из", total_words, "слов. Результат:", round(correct_answers/total_words*100, 2), "%")
