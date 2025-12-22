def calculate_grade(marks):

    if marks >= 90:
        return "A+", "Outstanding performance! Keep shining! "
    elif marks >= 80:
        return "A", "Great job! You are doing excellent! "
    elif marks >= 70:
        return "B", "Good work! Stay consistent! "
    elif marks >= 60:
        return "C", "Nice effort! You can achieve more with practice! "
    elif marks >= 50:
        return "D", "You passed! Keep improving! "
    else:
        return "F", "Don't give up. Study hard and success will come! "




# Input Student Name
student_name = input("Enter student name: ")

#
while True:
    try:
        marks = int(input("Enter marks (0 - 100): "))

        if 0 <= marks <= 100:     # valid marks range
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.\n")

    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")


# Calculate grade using function
grade, message = calculate_grade(marks)

# Final Output
print("\n===== RESULT =====")
print(f"Student Name: {student_name}")
print(f"Marks Scored: {marks}")
print(f"Grade: {grade}")
print(f"Feedback: {message}")
print("\nProgram finished successfully!")
