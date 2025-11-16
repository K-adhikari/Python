# Create three dictionaries each for one student

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


# Put the dictionaries in a list

students = [lloyd, alice, tyler]


# Print name, homework, quizzes, and tests for each student from the list

for student in students:
  for key, value in student.items():
    print("{}".format(value))


# Write a function to calculate average

def average(numbers):
  total = float(sum(numbers))
  average_value = total / len(numbers)
  return average_value


# Get average and return the weighted values with 10% from homework, 30% from quizzes, and 60% from tests

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])

  return homework * 0.1 + quizzes * 0.3 + tests * 0.6
  

# Write new function for letter grade

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
    

# Get the letter grade for each student

print (get_letter_grade(get_average(lloyd)))
print (get_letter_grade(get_average(alice)))
print (get_letter_grade(get_average(tyler)))


# Calculate the average of class

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)


# Determine the average grade and letter grade for the class

avg = get_class_average(students)
print avg
print(get_letter_grade(avg))
