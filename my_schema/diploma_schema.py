import sys
import os
# Додаємо теку tests до шляхів пошуку, щоб імпортувати helpers
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests')))

from helpers import S, F

ATTRS = S("exam_date grade student_id student_name subject_code subject_title")

FDS = F("""
    student_id -> student_name;
    subject_code -> subject_title;
    student_id subject_code -> exam_date grade
""")

KEYS = {
    S("student_id subject_code")
}

NORMAL_FORM = "3NF"

PARTS = [
    S("student_id student_name"),
    S("subject_code subject_title"),
    S("student_id subject_code exam_date grade")
]