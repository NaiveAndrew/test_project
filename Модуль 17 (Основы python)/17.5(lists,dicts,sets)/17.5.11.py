book = {}
book ['title'] = input ("Введите название книги: ")
book ['author'] = input ("Введите автора книги: ")
book ['year'] = int(input ("Введите год выпуска книги: "))
print (book)

#Вариант решения с сайта:
title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год издания:"))

book = {'title': title,
        'author': author,
        'year': year}

print(book)