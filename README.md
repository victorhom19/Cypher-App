# Cypher-App
Сервис, позволяющий зашифровать и расшифровать текстовую последовательность при помощи нескольких алгоритмов шифрования.

Доступные алгоритмы шифрования:
* Шифр Цезаря
* Шифр Атбаша
* Шифр Виженера
* Шифр Вернама
* Подстановочный шифр

## Шифр Цезаря:
Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите.

Путь запроса:

    http://localhost:8000/caesar-cypher/[encrypt/decrypt]?plaintext=[Исходное сообщение]&shift=[Смещение]
### Пример:
Исходное сообщение: **hello**, смещение: **2**

Шифрация:

    http://localhost:8000/caesar-cypher/encrypt?plaintext=hello&key=2
    >>> "ifmmp"

Дешифрация:
    
    http://localhost:8000/caesar-cypher/decrypt?plaintext=ifmmp&key=2
    >>> "hello"


## Шифр Атбаша:
Атбаш — простой шифр подстановки для алфавитного письма. Правило шифрования состоит в замене i-й буквы алфавита буквой с номером n-i+1, где n — число букв в алфавите.

Путь запроса:

    http://localhost:8000/atbash-cypher/[encrypt/decrypt]?plaintext=[Исходное сообщение]
### Пример:
Исходное сообщение: **hello**

Шифрация:

    http://localhost:8000/atbash-cypher/encrypt?plaintext=hello
    >>> "svool"

Дешифрация:
    
    http://localhost:8000/atbash-cypher/decrypt?plaintext=svool
    >>> "hello"


## Шифр Виженера:
Шифр Виженера состоит из последовательности нескольких шифров Цезаря с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов, называемая таблица Виженера. Применительно к латинскому алфавиту таблица Виженера составляется из строк по 26 символов, причём каждая следующая строка сдвигается на несколько позиций. Таким образом, в таблице получается 26 различных шифров Цезаря.


Путь запроса:

    http://localhost:8000/atbash-cypher/[encrypt/decrypt]?plaintext=[Исходное сообщение]&key=[Ключ]
### Пример:
Исходное сообщение: **hello**, ключ: **lemon**

Шифрация:

    http://localhost:8000/vigenere-cypher/decrypt?plaintext=hello&key=lemon
    >>> "sixzb"

Дешифрация:
    
    http://localhost:8000/vigenere-cypher/decrypt?plaintext=sixzb&key=lemon
    >>> "hello"

## Шифр Вернама:
Шифр является разновидностью криптосистемы одноразовых блокнотов. В нём используется булева функция «исключающее или». Шифр Вернама является примером системы с абсолютной криптографической стойкостью. При этом он считается одной из простейших криптосистем.


Путь запроса:

    http://localhost:8000/vernam-cypher/[encrypt/decrypt]?plaintext=[Исходное сообщение]&key=[Ключ]
### Пример:
Исходное сообщение: **hello**, ключ: **lemon**

Шифрация:

    http://localhost:8000/vernam-cypher/encrypt?plaintext=hello&key=lemon
    >>> "12 0 7 5 3"

Дешифрация:
    
    http://localhost:8000/vernam-cypher/decrypt?plaintext=12%200%207%205%203&key=lemon
    >>> "hello"

## Подстановочный шифр:
Шифр, при котором каждый символ открытого текста заменяется на некоторый, фиксированный при данном ключе символ того же алфавита.


Путь запроса:

    http://localhost:8000/substitution-cypher/[encrypt/decrypt]?plaintext=[Исходное сообщение]&key_alphabet=[Ключ]
### Пример:
Исходное сообщение: **hello**, ключ-алфавит: **zebrascdfghijklmnopqtuvwxy**

Шифрация:

    http://localhost:8000/substitution-cypher/encrypt?plaintext=hello&key_alphabet=zebrascdfghijklmnopqtuvwxy
    >>> "daiil"

Дешифрация:
    
    http://localhost:8000/vernam-cypher/decrypt?plaintext=12%200%207%205%203&key=lemon
    >>> "hello"


## Docker
Создание образа:

    docker build -t cypher-app-img .
Создание контейнера:

    docker create -p 8000:8000 --name cypher-app-container

Запуск контейнера:

    docker start cypher-app-container
