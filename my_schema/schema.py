"""Моя схема: атрибути, залежності, ключі, нормальна форма й декомпозиція (розділ 9 завдання).

Заповніть п'ять змінних внизу. Перевірка: python check_my_schema.py N (N - номер вашого набору 1..3).
"""


def S(text=""):
    """S("a b c") -> frozenset({"a", "b", "c"})."""
    return frozenset(text.split())


def F(text=""):
    """F("a b -> c; c -> d") -> список пар (frozenset, frozenset)."""
    result = []
    for part in text.split(";"):
        if part.strip():
            left, right = part.split("->")
            result.append((S(left), S(right)))
    return result


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