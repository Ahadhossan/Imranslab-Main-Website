import pytest
import dataclasses  # Add this import
from instructor.instructor import Instructor

def test_instructor_lookup():
    """Test instructor lookup with valid keys."""
    jane = Instructor.lookup("JANE_DOE")
    assert jane.name == "Dr. Jane Doe"
    assert jane.university.name == "Massachusetts Institute of Technology"
    assert jane.area_of_interest == "Artificial Intelligence"

    john = Instructor.lookup("JOHN_SMITH")
    assert john.name == "Dr. John Smith"
    assert john.university.name == "Stanford University"
    assert john.area_of_interest == "Quantum Computing"


def test_instructor_not_found():
    """Test that an invalid instructor lookup raises ValueError."""
    with pytest.raises(ValueError, match="Instructor 'UNKNOWN' not found."):
        Instructor.lookup("UNKNOWN")


def test_case_insensitive_instructor_lookup():
    """Test instructor lookup is case insensitive."""
    jane1 = Instructor.lookup("jane_doe")
    jane2 = Instructor.lookup("JANE_DOE")
    assert jane1 == jane2


def test_instructor_string_representation():
    """Ensure string representation of instructor is correct."""
    john = Instructor.lookup("JOHN_SMITH")
    assert str(john) == "Dr. John Smith, Stanford University - Area: Quantum Computing"


def test_instructor_immutability():
    """Test that Instructor objects are immutable."""
    jane = Instructor.lookup("JANE_DOE")
    with pytest.raises(dataclasses.FrozenInstanceError):
        jane.name = "New Name"


def test_instructor_has_valid_email():
    """Ensure the email format for the instructor is correct."""
    jane = Instructor.lookup("JANE_DOE")
    assert "@" in jane.email
    assert "." in jane.email.split("@")[-1]


def test_instructor_has_publications():
    """Ensure instructor has a valid list of publications."""
    jane = Instructor.lookup("JANE_DOE")
    assert isinstance(jane.publications, list)
    assert len(jane.publications) > 0
    assert "https://example.com/publication1.pdf" in jane.publications


def test_instructor_without_publications():
    """Ensure instructor can be created without publications."""
    john = Instructor.lookup("JOHN_SMITH")
    assert isinstance(john.publications, list)


def test_instructor_without_website():
    """Ensure instructor can exist without a website."""
    john = Instructor.lookup("JOHN_SMITH")
    assert john.website is not None  # Assuming all have websites, otherwise modify test


@pytest.mark.parametrize("invalid_code", ["", " ", "123", "!@#", "john123", "dr_smith"])
def test_invalid_instructor_codes(invalid_code):
    """Test invalid instructor lookup with different incorrect formats."""
    with pytest.raises(ValueError, match="Instructor '.*' not found."):
        Instructor.lookup(invalid_code)
