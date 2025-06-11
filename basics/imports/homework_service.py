from typing import Dict


def calculate_homework_avg(homework_grades: Dict[str, int]) -> float:
    """
    Calculate the average of homework grades.

    :param homework_grades: Dict of homework grades.
    :type homework_grades: Dict[str, int]

    :return: Average of the homework grades.
    """
    sum_of_grades = 0
    for grade in homework_grades.values():
        sum_of_grades += grade
    return sum_of_grades / len(homework_grades)
