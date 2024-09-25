def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 4, 8)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, True, 'string']

values_dict = {'a': False, 'b': 6, 'c': 'stroka'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['strochka', 8]

print_params(*values_list_2, 42)