grade = float(input())


def grading():
    grade_text = ""

    if 2 <= grade <= 2.99:
        grade_text = "Fail"
    elif 3 <= grade <= 3.49:
        grade_text = "Poor"
    elif 3.50 <= grade <= 4.49:
        grade_text = "Good"
    elif 4.50 <= grade <= 5.49:
        grade_text = "Very Good"
    elif 5.50 <= grade <= 6:
        grade_text = "Excellent"

    print(grade_text)


grading()
