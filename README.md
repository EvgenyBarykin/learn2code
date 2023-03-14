# Lesson 1

## GITHUB

- зарегались на github.com
- создали репозиторий
- создали ключ ssh

```bash
ssh -keygen -t ed25519 -C "@mail"
```
- сохранили ключи
- закинули публичный ключ на GitHub (https://github.com/settings/keys)

установили инструменты разработчика 
```bash
xcode-select --install
```

- клонировали репозиторий на комп

```bash
git clone https://github.com/settings/keys
```
- открыли его в Visual Code
- Поставили HomeBrew (для установки разных вещей на Мac) - пакетный менеджер

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- выполнили три команды которые он просит
- и установили питон
```bash
brew install python
```
- добавили новый интерпретатор в Visual code через путь к папке с ним

## Решили задачку с leet code
- написали функцию
- сохранили все на github
```bash
git status
git add
git commit -m
git push
```
# Lesson 2

- написали бинарный поиск
- познакомились с О() нотацией

# Lesson 3

## Сортировка

В зависимости от использования памяти:
- внутренняя
- внешняя

Важное свойство - устойчивость:
- устойчивая сортировка не меняет относительно положение одинаковых элементов

Пример сортировок:
- сортировка пузырьком: О(n^2) элементы меняются попарно, если левый больше правого
- шейкерная сортировка: O(n^2) вариант сортировки пузырьком, при котором мы идем по массиву то слева направо, то справа налево; границы рабочей части массива устанавливаютс в месте последнего обмена

## Merge sort (сортировка слиянием): 
O(n log n)
-  разделяем на несколько маленьких, сортируем, объединяем. Будет выгоднее, чем сортировать все, елси слияние не очень затратно по вычислениям.

Оффтоп: если у функции внутри класса есть декоратор @classmethod то ее можно вызывать напрямую из класса без объекта
``` 
Class Solution:
    @classmethod
    def test(cls):
        print('hello')
Solution.test()
```

- встроенный в Python sort() сортирует комбинацией merge sort и других методов. Называется TimSort

## посмотреть
- как узнать сколько места занимаем merge sort
- узнать почему нам достаточно n проходов, а не больше

в след раз: попробуем сделать быструю сортировку. можно заранее про нее и TimSort прочитать

# Miscellaneous

## Работа с текстовым редактором VIM:
- нажать i
- написать то что требуется до или после строчек со знаком #, для выхода нажать Esc
- для выхода написать :wq, нажать enter 

## Cмена текстового редактора в git

```
git config --global core.editor "ЛЮБОЙ ТЕКСТОВЫЙ РЕДАКТОР"

git config --global core.editor "nano"
```
- проверим, что сменился:
```
git config -l --show-scope
```
### Запуск интерактивного интерпретатора в терминале:
```
python3
```
- для выхода: нажать ctrl + D

# Lesson 4

## Области видимости
- чтобы использовать переменную вне функции, ее передают в качестве аргумента def local(spam)

- посмотреть mutable и immutable переменные,
Все типы данных в Python относятся к одной из 2-х категорий: изменяемые (mutable) и неизменяемые (unmutable).

Неизменяемые объекты:

числовые данные (int, float),
bool,
None,
символьные строки (class 'str'),
кортежи (tuple).

Изменяемые объекты:

списки (list),
множества (set),
словари (dict).

- почитать про области видимости

- если объявить переменную внутри функции и написать nonlocal var, то будет искать на уровень выше и менять значение переменной на уровень выше

- global var - будет искать в самом внешнем уровне и менять ее значение

## немного про классы
- когда класс создается, он вызывает функцию __init__ и можно задать ей разные параметры
```
def __init__(self, value) -> None:
        self.value = value
```

- функция __repr__ говорит, что появляется, когда объект пытаются напечатать (print)

## хороший способ вставить переменные в строку
- print(f'str {var}') - (посмотреть как экранировать фигурные скобки если хочешь их напечатать)

## уборщик мусора
В питоне есть garbage collector которй находит и удаляет переменные на которые нет ссылок или те, которые ссылаются только друг на друга 

## в след раз:
- перенесем все внутрь класса линкедлист
- сделаем итератор и генератор для класса лист
- посмотреть хэндбуки и конспекты итмо по сортировкам
    