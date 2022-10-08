#модули для основной работы с системой
import sys
import os
import platform 

#наименование ОС от sys
print(f'Тип операционной системы: {sys.platform} ')
#возвращает текущий логин пользователя
print(f'Текущий логин пользователя: {os.getlogin()} ')
#показывает текущий путь
print(f'Текущий путь: {os.getcwd()}')
#размер выбранного файла в байтах
name_file = 'stack_160922.py'
print(f'Размер файла {name_file} равен {sys.getsizeof(name_file)} байтов')
print('_______________________________')

#модуль platform
print(f'Архитектура ОС {platform.architecture()}')
print(f'Тип машины {platform.machine()}')
print(f'Сетевое имя компьютера {platform.node()}')
print(f'Сведения о базовой платформе {platform.platform()}')
print(f'Реальное имя процессора {platform.processor()}')
print(f'Номер и дата сборки Python {platform.python_build()}')
print(f'Версия компилятора {platform.python_compiler()}')
print(f'Реализация Python {platform.python_implementation()}')
print(f'Версия Python как строка {platform.python_version()}')
print(f'Сведения о выпуске системы {platform.release()}')
print(f'Имя операционной системы {platform.system()}')
print(f'Версия выпуска системы {platform.version()}')
print(f'Сведения команды терминала uname {platform.uname()}')






