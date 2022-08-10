# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове: {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"Количество букв 'а' в слове: {word.lower().count('а')}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
cnt = 0
vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
for i in word.lower():
    if i in vowels:
        cnt += 1
print(f'Количество гласных букв в слове = {cnt}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении: {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for i in list_sentence:
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
average_length = 0
for i in list_sentence:
    average_length += len(i)
print(average_length/len(list_sentence))