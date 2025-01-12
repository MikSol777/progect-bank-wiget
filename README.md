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

## Тесты проекта
Добавлено тестирование функций через pytest.


~~~
File        	        function        	statements	        missing     	excluded	      coverage
src\__init__.py	        (no function)       	    0	                0           	0	                100%
src\masks.py	        get_mask_card_number        4	                0           	0                	100%
src\masks.py	        get_mask_account	    4	                0              	0	                100%
src\masks.py	        (no function)	            2	                0           	0                 	100%
src\processing.py       filter_by_state 	    1               	0	        0	                100%
src\processing.py       sort_by_date	            1	                0           	0	                100%
src\processing.py       (no function)               2	                0           	0                	100%
src\widget.py	        mask_account_card   	    4               	0	        0           	        100%
src\widget.py	        get_date	            8                   0           	0           	        100%
src\widget.py	        (no function)	            3                   0	        0	                100%
Total	 	                                    29              	0	        0                       100%
~~~~


## Инструкция по установке
1. Выполнить клонирование репозитория [BankWidget](https://github.com/MikSol777/progect-bank-wiget) себе на компьютер
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry
3. Выполнить установку пакетов из списка зависимостей в файле _pyproject.toml_.
