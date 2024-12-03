my_dict = {'Вася': 1990, 'Коля': 1995, 'Настя': 1994}
print(my_dict, my_dict['Вася'], my_dict.get('Оля'), sep='\n')
my_dict.update({'Маша': 2000, 'Юля': 2001})
print(my_dict.pop('Вася'))
print(my_dict)

my_set = {1, 'String', 3, 4, 5.2, 1, 1, 'String',3, 5.2}
print(my_set)
list_ = [5,6]
my_set.update(list_)
my_set.discard(1)
print(my_set)