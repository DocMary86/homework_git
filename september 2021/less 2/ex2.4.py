'''Марина Кожарская
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

user_input = input('Offer: ')

words = user_input.split()
for num, word in enumerate (words):
    print(f'#{num} - {word[:10]}')
