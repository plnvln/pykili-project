#Эта программа - рабочий материал для записи порошков в формат JSON.
#Файлы этого формата будут открываться ботом и выводиться в него в ответ на кнопки.
#Сейчас эта программа выглядит так, будто бы мы хотим записать в JSON сто порошков из файла "Новости"

import json
import re
import random

def intro():
    element = '3'
    if element == '1':
          element = 'Руслан.txt'
    elif element == '2':
          element = 'Лорка.txt'
    elif element == '3':
          element = 'Новости.txt'
    elif element == '4':
          element = 'Земфира.txt'
    elif element == '5':
          element = 'Смешарики.txt'
    return element

#st - регулярное выражение для поиска ударных слогов
#unst - для поиска безударных

def opener(element):
    with open(element, encoding='utf-8') as file:
        text = file.read()
    return text

def first_third(text):
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию](?!\')[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    pattern1 = ' '+ unst + st + unst + st + unst + unst + unst + st + unst + ' '
    pattern2 = ' '+ unst + st + unst + st + unst + st + unst + st + unst + ' '
    result1 = re.findall(pattern1, text)
    result2 = re.findall(pattern2, text)
    result = result1 + result2
    result_1 = random.choice(result)
    result_3 = random.choice(result)
    return result_1, result_3

def second_and_fourth(text):
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию][^\'][цкнгшщзхфвпрлджчсмтьбъ]* ?'
    pattern1 = ' '+unst + st + unst + st + unst + unst + unst + st +' '
    pattern2 = ' '+unst + st + unst + st + unst + st + unst + st +' '
    result1_2 = re.findall(pattern1, text)
    result2_2 = re.findall(pattern2, text)
    result_2 = result1_2 + result2_2
    result_2 = random.choice(result_2)
    pattern_rhyme = st + '$'
    rhyme = re.search(pattern_rhyme, result_2)
    if rhyme:
        rhyme = rhyme.group()
        rhyme_find = ' ' + unst + rhyme
        fourthsearcher = re.findall(rhyme_find, text)
        fourthsearcher = ' '.join(fourthsearcher)
        pattern = unst + st
        result_4 = re.findall(pattern, fourthsearcher)
        result_4 = random.choice(result_4)
        return result_2, result_4

def retryer(text):
    try:
        result = second_and_fourth(text)
    except IndexError:
        result = retryer(text)
    return result

def main():
    element = intro()
    text = opener(element)
    try: 
        string_1 = first_third(text)[0]
        string_3 = first_third(text)[1]
        string_2_4 = retryer(text)
        poem = list ()
        poem.append(string_1)
        poem.append(string_2_4[0])
        poem.append(string_3)
        poem.append(string_2_4[1])
        poem = '\n'.join(poem)
        poem = poem.replace('\'', '')
        return poem
    except Exception:
        print('ooops, I did it again!')

def jsoner():
	print('Hello')
	poems = []
	for i in range(100):
		poems.append(main())
	with open('Новости.json', 'w', encoding = 'utf-8') as f:
		print('i\'m here')
		json.dump(poems, f, ensure_ascii = False)
		
print('hahaha')
jsoner() 


