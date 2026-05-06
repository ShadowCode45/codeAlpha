import matplotlib.pyplot as plt

# Step 1: Data
students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

# Step 2: Bar Chart
plt.bar(students, marks)

# Step 3: Labels & Title
plt.title("Student Marks Visualization")
plt.xlabel("Students")
plt.ylabel("Marks")

# Step 4: Show values on top
for i in range(len(students)):
    plt.text(i, marks[i] + 1, str(marks[i]), ha='center')

# Step 5: Grid (optional)
plt.grid(axis='y')

# Step 6: Show Graph
plt.show()