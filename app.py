def calculate_result(marks):
    if marks < 0 or marks > 100:
        return "INVALID"

    if marks >= 40:
        return "PASS"
    else:
        return "FAIL"


def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "INVALID"

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


if __name__ == "__main__":
    marks = 85

    result = calculate_result(marks)
    grade = calculate_grade(marks)

    print("Student Marks:", marks)
    print("Result:", result)
    print("Grade:", grade)