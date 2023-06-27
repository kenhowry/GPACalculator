from gpa import GPA_Calc, Course
import pytest

@pytest.fixture
def gpa_calc_fixture():
    # Create an instance of GPA_Calc with appropriate arguments
    major = "Computer Science"
    minor = "Mathematics"
    return GPA_Calc(major, minor)

def test_repeating_class_replace(gpa_calc_fixture):
    gpa_calc = gpa_calc_fixture

    other_calc = GPA_Calc(gpa_calc.major, gpa_calc.minor)
    other_calc.addCourse(gpa_calc.major, "A", 3)

    gpa_calc.repeating_class(other_calc, "replace")

    assert gpa_calc.overall_gpa(gpa_calc.courses) == 0.0

def test_repeating_class_average(gpa_calc_fixture):
    gpa_calc = gpa_calc_fixture

    other_calc = GPA_Calc(gpa_calc.major, gpa_calc.minor)
    other_calc.addCourse(gpa_calc.major, "A-", 3)

    gpa_calc.repeating_class(other_calc, "average")

    assert gpa_calc.overall_gpa(gpa_calc.courses) == 0.0
