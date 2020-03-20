# [...] likes to round each student's grade according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    roundedGradesList = list()
    for grade in range(len(grades)):
        lastDigit = grades[grade]%10
        if (5 - lastDigit) in (1,2) and grades[grade] >= 38:
            grades[grade] += (5 - lastDigit)
        if (5 - lastDigit) in (-3,-4) and grades[grade] >= 38:
            grades[grade] += (10 - lastDigit)
        roundedGradesList.append(grades[grade])
    return roundedGradesList

grades = [73,67,38,33]
print(gradingStudents(grades))