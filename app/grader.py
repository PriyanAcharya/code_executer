def grade_submission(student_output: str, expected_output: str):
    if student_output.strip() == expected_output.strip():
        return {"score": 100, "passed": True}
    else:
        return {"score": 0, "passed": False}
