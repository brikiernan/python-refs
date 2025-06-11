from imports.homework_service import calculate_homework_avg


homework_grades = {"math": 85, "science": 90, "history": 78, "english": 88, "art": 92}

homework_avg = calculate_homework_avg(homework_grades)

print(f"The average homework grade is: {homework_avg}")
