# Step 1: Ask for the number of students
num_students = int(input("Enter the number of students: "))

# Step 2: Create an empty list to hold the data
students = []

# Step 3: Use a loop to collect name and score for each student
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score of {name}: "))  # Use float to allow decimal scores
    students.append([name, score])

# Step 4: Print the final list
print("Student List:", students)

# Sort students by score in descending order (highest score first)
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)

# Print sorted list
print("Students sorted by score:")
for name, score in students_sorted:
    print(f"{name}: {score}")