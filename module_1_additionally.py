grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = tuple(sorted(students))
average_score ={}
average_score.update({students[0] : grades[0], students[1] : grades[1], students[2] : grades[2], students[3] : grades[3], students[4] : grades[4]})
print(average_score)
# Без использования циклов и классов както так