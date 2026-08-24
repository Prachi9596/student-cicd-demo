from app import calculate_result, calculate_grade


def test_pass_student():
    assert calculate_result(75) == "PASS"


def test_fail_student():
    assert calculate_result(30) == "FAIL"


def test_invalid_marks():
    assert calculate_result(105) == "INVALID"


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_f():
    assert calculate_grade(35) == "F"