import re
import random

def intro():
    print('Здравствуй, дорогой друг. Я - генератор стишков-"пирожков", и я предлагаю тебе познакомиться с моим творчеством. Но для начала выбери фандом: \n 1) "Руслан и Людмила" А.С.Пушкин \n 2) Стихотворения Фредерико Гарсия Лорки \n 3) Актуальные новости (недоступно сейчас) \n 4) Тексты песен Земфиры (недоступно сейчас) \n 5) Песенки и стихотворения из "Смешариков" ')
    element = input()
    while element != '1' and element != '2' and element != '3' and element != '4' and element != '5':
        print('Неправильно выбран фандом. Попробуйте ещё раз!')
        element = input()
    if element == '1':
          element = 'Руслан.txt'
    elif element == '2':
          element = 'lorka.txt'
    elif element == '3':
          element = 'Новости.txt'
    elif element == '4':
          element = 'гибрид.txt'
    elif element == '5':
          element = 'Смешарики.txt'
    return element

def opener(element):
    with open(element, encoding='utf-8') as file:
        text = file.read()
    return text

#st - stressed - регулярное выражение для поиска ударных слогов
#unst - unstressed - для поиска безударных

def first_third(text):
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию][^\'][цкнгшщзхфвпрлджчсмтьбъ]* ?'
    pattern1 = ' '+ unst + st + unst + st + unst + unst + unst + st + unst + ' '
    pattern2 = ' '+ unst + st + unst + st + unst + st + unst + st + unst + ' '
    result1 = re.findall(pattern1, text)
    result2 = re.findall(pattern2, text)
    result = result1 + result2
    result = random.choice(result)
    return result

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
    string_1 = first_third(text)
    string_3 = first_third(text)
    string_2_4 = retryer(text)

    poem = list ()
    poem.append(string_1)
    poem.append(string_2_4[0])
    poem.append(string_3)
    poem.append(string_2_4[1])
    poem = '\n'.join(poem)
    #print(poem)
    poem = poem.replace('\'','')
    print(poem)


if __name__ == '__main__':
    main()  
