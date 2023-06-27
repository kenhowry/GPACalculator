from gpa import GPA_Calc

def testone():
    student = GPA_Calc("COMP", "MATH")
    assert student.locate_file("873256025") == f"Transcript file sucessfully located."

def testtwo():
    student = GPA_Calc("COMP", "MATH")
    assert student.locate_file("873256029") == "File not located. Enter the information again."