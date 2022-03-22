line = "--------------------------------------------------------------"
# methods
numbers = []
# append()
numbers.append(123)
numbers.append(123)
numbers.append(123)
print("append result: ", numbers)
# insert() insert element by index

print(numbers)
numbers.insert(2, "number")
print("insert result: ", numbers)
numbers[2] = "new number"


# count - numbers of element
count_of_element = numbers.count(123)
print("count result: ", count_of_element)
# sort
numbers = [123, 45, 7, -10]
print(numbers)
numbers.sort()
print("sort result: ", numbers)

list_strings = ["a_word", "b_word", "a_word"]
print(list_strings)
list_strings.sort()
print("result of sort strings: ", list_strings)

# copy 
numbers_empty = []
numbers_empty = numbers.copy()
print(numbers_empty)
# pop, remove
numbers.remove(45)
print(numbers)
# numbers.remove(10)

print("before pop: ", numbers)
numbers.pop()
print("after pop: ", numbers)

# clear , extend

print("before clear: ", numbers)
numbers.clear()
print("after clear: ", numbers)

my_list = ["one", "two"]
my_list_two = ["four", "five"]

print("before extend: ", my_list_two)
my_list_two.extend(my_list)
print("after extend: ", my_list_two)

# slice list[start:stop:step]
numbers = list(range(20))
print(numbers)

numbers_two = numbers[0:10:1]
print(numbers_two)
numbers_two = numbers[5:13:1]
print(numbers_two)
# a,b,c = list_one

numbers = list(range(20))
print(line)
new_numbers = []
for i in numbers:
    if i % 2 == 0:
        new_numbers.append(i)
print(new_numbers)
