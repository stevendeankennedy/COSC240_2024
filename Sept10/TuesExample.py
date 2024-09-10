# This is just an example for using containers in Python
# Steve + everyone in the class
# 9/10/24

# List!
exam_grades = [90, 75.5, 86, 94, 100]

exam_average = sum(exam_grades) / len(exam_grades)

print(exam_grades)
print(f'The average is {exam_average}')


# Set!!
fruit_set = {"apple", "mango", "kiwi", "orange"}

print(fruit_set)
fruit_set.remove("kiwi")
fruit_set.pop()
fruit_set.add("grape")
print(fruit_set)


# Dictionary!!!
print("Now dictionary!\n")

class_colors = {
    "Chris" : "blue",
    "Covy" : "red",
    "Jackson" : "purple",
    "Deontae" : "green"
    }

class_colors["Chris"] = "red"
del class_colors["Covy"] # Sorry, Covy!!! 

# print a statement that includes a grade and a color
print(f'Some grade: {exam_grades[2]}, Some color: {class_colors["Chris"]}')
print(class_colors)
