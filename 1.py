# Создать класс SmartList, который расширяет функциональность обычного списка Python.
#  Класс должен поддерживать дополнительные операции и автоматическое отслеживание изменений.

# Требования к классу:
# 1. Наследование: Класс должен наследоваться от стандартного list.
# 2. История изменений: Автоматическое сохранение состояния списка перед каждым изменением. Методы append и pop
# 3. Откат изменений: Метод undo() для восстановления предыдущего состояния.
# 4. Дополнительные методы:
#    - find_indices(value): возвращает все индексы, по которым встречается указанное значение.
#    - frequency(): возвращает словарь с частотой встречаемости каждого элемента.
# 5. Специальные операции:
#    - __add__: объединение двух SmartList (возвращает новый SmartList).
#    - __call__: фильтрация списка по условию (возвращает новый SmartListstr __str__: красивое строковое представление.


from typing import Iterable


class SmartList(list):
    def __init__(self, iterable: Iterable):
        super().__init__(iterable)
        self.backup_list = [list(self)]

    
    def undo(self):
        pass

    def append(self, item):
        super().append(item)
        self.backup_list.append(list(self))


    def pop(self, index):
        super().pop(index)
        self.backup_list.append(list(self))

    
    def __add__(self, lst):
        return SmartList(super().__add__(lst))

    def __call__(self, ):
        return self.backup_list[-1]

a = SmartList('asd')





print('ap', a.backup_list)

print(a)
a.append(1)
print('bkp', a.backup_list)
print(a)
a.append(2)
print('bkp', a.backup_list)
print(a)

b = a + SmartList('b')

print('b bkp', b.backup_list)