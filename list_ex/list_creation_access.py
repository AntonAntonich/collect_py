# creation
# constructor
numbers = [1, 2, 3, 4]
languages = ["java", "python", "go"]
print("list of numbers", numbers)

# method
python = list("python")
print("list: ", python)

word = ["word"]

word_two = list("word")

print("word: ", len(word))
print("word_two: ", len(word_two))

# list_method = list("python", "java")  # --error

# mono type

bullet = "bullet"
bullets = [bullet] * 9
# print("bullets: ", bullets)

# range numbers
numbers = list(range(10))
print(numbers)
numbers = list(range(0, 10, 3))
print(numbers)
numbers = list(range(19, 0, -2))
print(numbers)
# generator
numbers = []
[numbers.append(i) for i in range(0, 10, 2)]
print(numbers)
# access
# access matrix
languages = ["java", "python", "go", "c#", "c++", "c"]
print(languages[2])
print(languages[-1])
print(languages[-2])
# cycles
# output
for value in languages:
    print(value, end="-")
# change
numbers = list(range(0, 21, 4))
print()
print(numbers)
for index in range(0, len(numbers) - 1, 1):
    numbers[index] *= 2
print(numbers)
