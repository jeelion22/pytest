import pytest
from source.school import Teacher, ClassRoom, Student, TooManyStudents


@pytest.fixture
def teacher():
    return Teacher("Prof. Snape")


@pytest.fixture
def students():
    return [Student(f"Student_{i}") for i in range(5)]


@pytest.fixture
def classroom(teacher, students):
    return ClassRoom(teacher, students, "Potions")


def test_add_student(classroom):
    new_student = Student("New Student")
    classroom.add_student(new_student)
    assert new_student in classroom.students


def test_add_too_many_students(classroom):
    with pytest.raises(TooManyStudents):
        for i in range(10):
            classroom.add_student(Student(f"Student_{i}"))


def test_remove_student(classroom, students):
    student_to_remove = students[0]
    classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in classroom.students


def test_change_teacher(classroom, teacher):
    new_teacher = Teacher("Prof. McGonagall")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher


# Mark the test as slow
@pytest.mark.slow
def test_complex_operation(classroom):
    # Write a test that involves a complex operation
    pass
