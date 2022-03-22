# set
# creation
# constr
# frozenset
my_set = {"value", "value1", "value1", "value1", "value1"}
print(my_set)

my_list = ["value", "value1", "value1", "value1", "value1"]
print("list: ", my_list)
my_set = set(my_list)
print("set: ", my_set)

# immutable_set
my_frozen_set = frozenset(my_list)
print("frozen set: ", my_frozen_set)

# set_id[0] = "default" - error

# add, remove, discard, clear
print("before add: ", my_set)
my_set.add("adding file")
print("after add: ", my_set)

print(my_frozen_set)

print(my_frozen_set)

print("before remove: ", my_set)
my_set.remove("value")
print("after remove: ", my_set)

# my_set.remove("asdasd")


print("before discard: ", my_set)
my_set.discard("asdasd")
print("after discard: ", my_set)

# copy, union

my_set = {"one", "two", "free"}
my_set_two = {"four", "five"}

my_result = my_set.copy()
print(my_result)
my_result = my_set_two.copy()
print(my_result)

my_result = my_set.union(my_set_two)
print(my_result)
# intersection, difference
my_set = {"one", "two", "free", "eight"}
my_set_two = {"free", "four", "five", "eight"}
print("intersection result: ", my_set.intersection(my_set_two))

print("difference result: ", my_set.difference(my_set_two))

# subset, superset

my_result_set = my_set.union(my_set_two)
print("set one", my_set)
print("set two", my_set_two)
print("set result", my_result_set)


print("is set subset ", my_set.issubset(my_result_set))
print("is set subset ", my_set.issubset({"asdads", "asdasd", "123123"}))

print("is superset", my_result_set.issuperset(my_set_two))