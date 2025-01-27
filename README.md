# Bank Widget
Учебный проект sky.pro. Разработка виджета для банка

## Содержание
1. [sky.pro](https://my.sky.pro)
2. Проект находится в стадии разработки.
 
## Реализованные функции
1. **`get_mask_card_number`** -_Принимает на вход номер карты и возвращает ее маску_
2. **`get_mask_account`** - Принимает на вход номер счета и возвращает его маску
3. **`mask_account_card`** - Возвращает строку с замаскированным номером
4. **`get_date`** - Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'
5. **`filter_by_state`** - Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению
6. **`sort_by_date`** - Возвращает новый список, отсортированный по дате (date)
7. **`filter_by_currency`** - Принимает на вход список словарей, представляющих транзакции.
Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
8. **`transaction_descriptions`** - Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
9. **`card_number_generator`** - Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999

## Реализованные декораторы
1. **`log`** -_Логирует выполнения функции, а также ее результаты или возникшие ошибки_

## Тесты проекта
Добавлено тестирование функций через pytest.


~~~
File        	        function        	statements	        missing     	excluded	      coverage
src\masks.py	        get_mask_card_number        4	                0           	0                	100%
src\masks.py	        get_mask_account	    4	                0              	0	                100%
src\processing.py       filter_by_state 	    1               	0	        0	                100%
src\processing.py       sort_by_date	            1	                0           	0	                100%
src\widget.py	        mask_account_card   	    4               	0	        0           	        100%
src\widget.py	        get_date	            8                   0           	0           	        100%
src\generators.py	filter_by_currency	    2           	0	        0	                100%
src\generators.py	transaction_descriptions    2           	0	        0	                100%
src\generators.py	card_number_generator	    3               	0	        0	                100%
src\decorators.py	log	                    3	                0               0	                100%
src\decorators.py	log.decorator               2 	            	0       	0	                100%
src\decorators.py	log.decorator.inner	    12	                0	        0   	                100%
Total	 	                                    58              	0	        0                       100%
~~~~


## Инструкция по установке
1. Выполнить клонирование репозитория [BankWidget](https://github.com/MikSol777/progect-bank-wiget) себе на компьютер
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry
3. Выполнить установку пакетов из списка зависимостей в файле _pyproject.toml_.
