try:
    mark = float(input("Enter your mark(0:100):"))
    if mark >= 90 and mark <= 100:
        print("Grade: A")
    elif mark >= 80 and mark < 90:
        print("Grade: B")
    elif mark >= 70 and mark < 80:
        print("Grade: C")
    elif mark >= 60 and mark < 70:
        print("Grade: D")
    else:
        print("Grade: E")
#Exception handled using try and except block to capture invalid input and display an error message.
except Exception as e:
    print("Invalid input. Please enter a valid number between 0 and 100.", e)
