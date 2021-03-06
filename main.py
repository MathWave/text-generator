import os
import random
from tkinter import *


def CreateText(n): #функция создания текста от количества строк

    dictionary = {}  # изначально словарь пустой
    lastword = ''  # последнее слово пустое
    for file in os.listdir(path='.'):  # для каждого файла в директории
        if file[len(file) - 4:len(file)] == '.txt':  # если файл имеет расширение .txt
            for line in open(file, 'r'):  # проверяем каждую его строку
                words = re.compile('[^,-.0-9a-zA-Zа-яА-Я ]').sub('', line).split()  # выкидываем неалфавитные символы
                if words != []:  # если слова в строке остались
                    if lastword != '':  # если последнее слово предыдущей строки не пустое
                        words = [lastword] + words  # добавляем его в начало текущей
                    for i in range(len(words) - 1):  # для чисел от 0 до размера строки -1
                        if words[i] not in dictionary:  # если данного ключа нет в словаре
                            dictionary[words[i]] = {words[i + 1]: 1}  # добавляем его
                        elif words[i + 1] not in dictionary[words[i]]:  # если у данного ключа нет значения
                            dictionary[words[i]][words[i + 1]] = 1  # добавляем и присуждаем 1
                        else:  # иначе
                            dictionary[words[i]][words[i + 1]] += 1  # увеличиваем на 1
                    lastword = words[len(words) - 1]  # запоминаем последнее слово

    text = ''  # итоговая фраза изначальна равна пустой строке
    for i in range(n):
        if i == 0 or word1 not in list(dictionary.keys()):#если i равно 0 или слово не является первым в какой-либо паре
            word1 = random.choice(list(dictionary.keys())) #тогда слово рандомно выбирается из ключей словаря
            text += word1 + ' ' #и добавляется к итоговой фразе
        else: #в противном случае
            definitions = [] #создаем список значений
            for key in list(dictionary[word1].keys()): #для каждого значения в словаре
                for j in range(dictionary[word1][key]): #добавляем его значение столько раз,
                    definitions.append(key)             #сколько эта пара встречается в список definitions
            word2 = random.choice(definitions) #из получившегося списка случайно выбираем слово
            text += word2 + ' ' #добавляем его к итоговой фразе
            word1 = word2 #теперь второе слово становится первым
    return text #возвращаем итоговую фразу


def PrintText():
    canvas.delete('all')
    canvas.create_text(10, 200, width=980, anchor=W, fill='white', text=CreateText(int(entry_amount.get())))


root = Tk()
root.title('TextGenerator by MathWave')
root.geometry('1000x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=1000, height=400, bg='black')
canvas.pack(side='bottom')

label_amount = Label(root, text='Количество слов в генерируемом тексте: ')
label_amount.place(x=0, y=10)

entry_amount = Entry(root)
entry_amount.place(x=300, y=10)

btn_gen = Button(root, text='Сгенерировать текст!')
btn_gen.bind('<Button-1>', lambda event: PrintText())
btn_gen.place(x=10, y=40)

root.mainloop()
