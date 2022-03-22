# dictionaries
my_dict = {"key_one": "value_one", "key_two": "value_2"}
print(type(my_dict))
print(my_dict)
# items() returning tuples

for key, value in my_dict.items():
    print("key: ", key)
    print("value: ", value)

for key in my_dict.keys():
    print("key: ", key)

for value in my_dict.values():
    print("value: ", value)

    # checking key
    for key in my_dict.keys():
        if key == "key_one":
            print(my_dict[key])

# get with default

print(my_dict.get("key_one"))
print(my_dict.get("key_on", "default"))

# pop, update
print("before pop in dict: ", my_dict)
# print(my_dict.pop("key_one"))
print("after pop in dict: ", my_dict)

# complex dict
my_compl_dict = {
    "object_one": {
        "parameter_one": 1,
        "parameter_two": 2
    },
    "object_two": {
        "parameter_one": 1,
        "parameter_two": 2
    }
}

print(my_compl_dict)
# access
# dict[key][sub_key]
print(my_compl_dict["object_one"]["parameter_one"])
