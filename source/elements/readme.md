###Файл `__init__.py`
Файл `__init__.py` нужен для импорта элементов (классов, методов) из файлов по умолчанию

Так, строка `from .BaseElement import BaseElement` означает сделать импорт класса BaseElement из файла BaseElement

Это нужно для того, чтобы при использовании этого класса из другого файла можно было писать не так:

`from source.elements.BaseElement import BaseElement`

`BaseElement(parameter_one, parameter_two, ...`

а так:

`from source.elements import BaseElement`

`BaseElement(parameter_one, parameter_two, ...)`

###Файл `BaseElement.py`
Данный файл содержит в себе методы, которые могут быть применены на любой странице браузера
