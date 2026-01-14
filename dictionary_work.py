#let's do some dict work.

dict_1 = {'a':1, 'b':2, 'c':3, 'd':4}

print(dict_1['a'])
print(dict_1.keys())
print(type(dict_1.keys()))
print(type(dict_1.values()))

key_list = list(dict_1.keys())
print(key_list)

value_list = list(dict_1.values())
print(value_list)

var1 = ''
for i in range(len(key_list)):
    var1 = var1 + key_list[i]

print(var1)

var2 = 0
for i in range(len(value_list)):
    var2 = var2 + value_list[i]

print(var2)