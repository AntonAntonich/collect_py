# tuple
# creation
# constr
my_tuple = (10, 12, 3, "word",)
print("type: ", type(my_tuple))
print("tuple: ", my_tuple)
# coma
tuple_numb = (10)
print(type((tuple_numb)))
tuple_numb = (10,)
print(type((tuple_numb)))

# decomposition into variables
my_tuple = ("word_one", 555, 'a',)

word, number, character = my_tuple
print(word)
print(number)
print(character)
# immutable
# my_tuple[0] = 5
list_id = ("id_one", "id_two",)
# code
#list_id[0] = "default"
# code
list_id[0]
print(list_id[0])

list_id_new = []
for i in list_id:
    list_id_new.append(i)
list_id_new = list(list_id)
list_id_new[0] = "def"
print(list_id_new)
my_tuple_new = tuple(list_id_new)
print(my_tuple_new)
