immutable_var = (1, 2, "String", False)
print(immutable_var)
# immutable_var [0] = 5
# print(immutable_var)
# Кортеж относится к неизменяемым типам данных, но может содержать изменяемые элементы(строки, списки)
mutable_list = [1,2,"string", True]
mutable_list.append(5)
mutable_list.reverse()
print(mutable_list)